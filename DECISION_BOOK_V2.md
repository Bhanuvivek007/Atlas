# DECISION_BOOK_V2.md

# Atlas Architecture Decisions – Version 2

## Status

**Accepted**

---

# Objective

This document records the architectural decisions for the **Application Layer** of Atlas.

Version 1 established the domain language.

Version 2 establishes how requests flow through the application and how application components collaborate.

---

# Architecture

```
Boundary
    │
    ▼
ConversationManager
    │
    ▼
ReasoningEngine
    │
    ├── Teacher
    ├── MemoryEngine
    └── GenerationEngine
    │
    ▼
Response
```

---

# Decision 1 — Application Boundaries Create Requests

**Decision**

Requests are created by the application boundary (CLI, Voice, API).

**Reasoning**

The boundary knows:

* Raw user input
* Request source
* Timestamp
* Optional session identifier

ConversationManager should receive a complete Request rather than constructing one.

---

# Decision 2 — ConversationManager Owns Session Lifecycle

**Responsibilities**

* Receive Request
* Resolve or create Session
* Delegate reasoning
* Update Session metadata
* Return Response

**Non-Responsibilities**

* Intent detection
* Memory retrieval
* Teaching
* Prompt construction
* LLM interaction

ConversationManager is responsible for conversation orchestration only.

---

# Decision 3 — ReasoningEngine Owns Reasoning

ReasoningEngine determines how Atlas should satisfy a Request.

Its responsibilities are:

* Understand user intent
* Compose the appropriate reasoning pipeline
* Coordinate specialized capabilities
* Return the final Response

ReasoningEngine does **not** manage Sessions or interact directly with infrastructure.

---

# Decision 4 — Dynamic Reasoning Pipeline

The reasoning pipeline is selected dynamically based on the Request.

Examples:

Teaching

```
Memory
    ↓
Teacher
    ↓
Generation
```

Planning

```
Planner
    ↓
Generation
```

Research

```
Research
    ↓
Generation
```

The pipeline is determined at runtime.

---

# Decision 5 — Capabilities Have Single Responsibilities

Each capability is responsible for one concern.

Teacher

* Creates TeachingPlan

MemoryEngine

* Retrieves relevant memories

GenerationEngine

* Produces the final Response

No capability should perform another capability's responsibility.

---

# Decision 6 — Thinking and Speaking Are Separate

Atlas separates reasoning from communication.

Teacher does not generate natural language.

Teacher produces a TeachingPlan.

GenerationEngine converts structured reasoning into a Response.

This separation allows different presentation formats without changing reasoning logic.

---

# Decision 7 — Application Before Infrastructure

Application components define behavior.

Infrastructure provides implementations.

Examples:

* OpenAI
* SQLite
* Vector databases
* Embedding providers

These are implementation details and should not influence application architecture.

---

# Decision 8 — Stable Contracts Before Implementations

Application components are designed as contracts before behavior is implemented.

Current application contracts:

* ConversationManager
* ReasoningEngine
* Teacher
* MemoryEngine
* GenerationEngine

Implementation will be added after responsibilities and interactions are stable.

---

# Deferred Decisions

## ExecutionPlan

ReasoningEngine currently composes the reasoning pipeline internally.

A dedicated ExecutionPlan object may be introduced if orchestration becomes significantly more complex.

Deferred.

---

## Capability Registry

ReasoningEngine currently depends explicitly on its required capabilities.

A Capability Registry may be introduced when the number of capabilities grows enough to justify additional abstraction.

Deferred.

---

## Generator Interface

GenerationEngine currently represents the generation capability.

If multiple LLM providers or generators become necessary, introduce a Generator interface with infrastructure adapters such as:

* OpenAIGenerator
* AnthropicGenerator
* OllamaGenerator

Deferred until required.

---

## ReasoningResult

GenerationEngine currently has no dedicated structured input object.

A ReasoningResult (or similar) may be introduced once implementation reveals a stable data structure flowing into GenerationEngine.

Deferred.

---

# Engineering Principles

* Build architecture before implementation.
* Separate responsibilities clearly.
* Prefer composition over coupling.
* Keep application independent of infrastructure.
* Avoid abstractions until they solve a real problem.
* Prefer architectural stability over cosmetic improvements.
* Do not implement behavior before contracts are stable.

---

# Sprint Summary

Completed:

* Application layer architecture
* ConversationManager
* ReasoningEngine
* Teacher contract
* MemoryEngine contract
* GenerationEngine contract

Next milestone:

Implement the first vertical slice:

```
CLI
    ↓
Request
    ↓
ConversationManager
    ↓
ReasoningEngine
    ↓
Teacher
    ↓
GenerationEngine
    ↓
Response
```

The objective is to validate the architecture before expanding the system further.
