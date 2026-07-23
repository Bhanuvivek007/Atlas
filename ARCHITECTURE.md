# ARCHITECTURE.md

# Atlas Architecture

## Vision

Atlas is a local-first AI thinking partner that helps users learn deeply, think critically, and manage their work through persistent memory and personalized reasoning.

Unlike traditional AI assistants, Atlas is built around **memory**, **reasoning**, and **adaptation**, rather than around a single LLM.

---

# High-Level Architecture

```text
                    User
                      │
                      ▼
            Conversation Manager
                      │
                      ▼
              Reasoning Engine
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
   Attention      Teacher      Planner
      Engine
         │
         ▼
    Memory Engine
         │
      SQLite DB
         ▲
         │
 Reflection Engine
         │
    Updates Memory

Teacher
      │
      ▼
Generation Engine
      │
      ▼
OpenAI / Claude / Gemini / Local Models
```

---

# Core Components

## Conversation Manager

Responsible for transforming user interactions into structured requests.

Responsibilities:

* Accept CLI input
* Maintain session context
* Produce `Request` objects

It does **not** perform reasoning.

---

## Reasoning Engine

Acts as Atlas' central coordinator.

Responsibilities:

* Understand user intent
* Decide which specialist to invoke
* Request relevant context
* Orchestrate the response pipeline

The Reasoning Engine never teaches or stores memory.

---

## Attention Engine

Determines which memories are relevant for the current request.

Responsibilities:

* Select memory categories
* Filter unnecessary context
* Minimize prompt size

Sprint 1 uses rule-based retrieval.

Future versions will support semantic retrieval.

---

## Memory Engine

Atlas' persistence layer.

Responsibilities:

* Store memory
* Retrieve memory
* Update memory
* Delete memory

Business logic is intentionally excluded.

---

## Teacher

Designs learning experiences.

Responsibilities:

* Decide teaching strategy
* Select explanation style
* Generate quizzes
* Adapt lessons using user insights

Teacher returns a `TeachingPlan`.

---

## Planner

Responsible for productivity.

Future responsibilities include:

* Daily planning
* Task prioritization
* Calendar integration
* Reminder generation

Planner is intentionally lightweight in Sprint 1.

---

## Reflection Engine

Learns from every interaction.

Responsibilities:

* Infer user patterns
* Update confidence scores
* Create Insights
* Improve personalization

Reflection runs after responses are delivered.

---

## Generation Engine

Provides a unified interface to language models.

Responsibilities:

* Build model requests
* Call provider APIs
* Return generated responses

Atlas should never depend on a specific LLM provider.

---

# Design Principles

## Local First

User knowledge belongs to the user.

---

## Memory Before Intelligence

A replaceable model should never own irreplaceable knowledge.

---

## Explicit Responsibilities

Every component has one responsibility.

---

## Testability

Each component should be independently testable.

---

## Extensibility

Adding new specialists should not require rewriting existing ones.

---

# Long-Term Evolution

Sprint 1

Central Brain

```text
Conversation
        │
Reasoning
        │
Teacher / Planner
```

Future

Distributed Specialists

```text
Teacher Agent

Planner Agent

Research Agent

Reflection Agent

Memory Agent
```

The public interfaces remain unchanged while implementation evolves.

---

# Success Criteria

Atlas should eventually:

* Remember users over years.
* Continue unfinished learning sessions.
* Adapt explanations.
* Challenge reasoning.
* Become more useful after every interaction.

Atlas is not designed to answer questions.

Atlas is designed to help users become better thinkers.
