# ATLAS_DECISION_BOOK_V1

> Version: 1.0
>
> Purpose:
> This document captures the architectural decisions made while building Atlas.
>
> It records:
>
> * Why a decision was made.
> * Alternatives considered.
> * Future improvements.
> * Open questions.
> * Engineering principles.
>
> Good architecture is not just writing good code.
> It is preserving the reasoning behind the code.

---

# Engineering Principles

1. Model reality before writing code.
2. Facts should be immutable.
3. Mutable objects should exist only when the domain naturally changes.
4. Domain objects contain no business logic.
5. Prefer business terminology over technical terminology.
6. Every interaction enters Atlas as a `Request`.
7. Depend on abstractions, not implementations.
8. Build the simplest thing that works.
9. Don't implement tomorrow's features today.
10. Every architectural idea should be recorded before implementation.

---

# Accepted Decisions

## Request

### Decision

`Request` represents one user interaction with Atlas.

### Design

* Immutable (`@dataclass(frozen=True)`).
* Uses UUID as identity.
* `session_id` is optional.
* Created by ConversationManager.
* Contains no business logic.

### Reasoning

A Request represents a historical fact.

Facts should never change.

---

## Response

### Decision

`Response` represents Atlas' final communication back to the user.

### Current Design

* message
* follow_ups

### Reasoning

A Response should communicate information only.

It should not know about:

* model metadata
* token usage
* streaming
* infrastructure
* actions

Those belong elsewhere.

---

## Session

### Decision

A Session represents one continuous conversation.

### Design

* Mutable.
* ConversationManager owns it.
* Title is optional.
* Tracks start time and last activity.

### Reasoning

Unlike Requests, Sessions naturally evolve over time.

---

## Memory

### Decision

Memory represents processed knowledge rather than raw conversation.

### Design

* Mutable.
* Uses UUID.
* Stores content as text.
* Confidence ranges from 0.0 to 1.0.
* Categorized into:

  * Identity
  * Learning
  * Project
  * Observation

### Reasoning

Atlas remembers knowledge, not chat history.

Embeddings are intentionally excluded because they are an implementation detail of semantic search rather than part of the concept of memory.

---

## TeachingPlan

### Decision

Teacher should think before Generation writes.

### Design

Contains

* goal
* strategy
* instructions

Immutable.

### Reasoning

Reasoning and language generation are separate responsibilities.

Teacher decides **what** should be taught.

Generation decides **how** it should be written.

---

# Rejected Decisions

## Store Embeddings inside Memory

### Decision

Rejected.

### Reason

Embeddings are infrastructure.

Memory is a domain concept.

Changing embedding models should never require changing the Memory domain object.

---

# Deferred Decisions

## Rich FollowUp Object

Current

```text
follow_ups: list[str]
```

Future

```text
FollowUp
    display_text
    request_text
```

Reason

Allows concise UI while sending richer Requests internally.

---

## Session Owns Requests

Current

```text
Request
    session_id
```

Possible Future

```text
Session
 ├── Request
 ├── Request
 └── Request
```

Deferred until there is a clear benefit.

---

## Memory Importance

Possible future field

```text
importance: float
```

Difference

Confidence

> How certain Atlas is.

Importance

> How useful the memory is during reasoning.

---

## Structured Memory

Current

```
content: str
```

Future

Specialized memory types may be introduced if plain text becomes limiting.

Deferred.

---

## Response Actions

Possible future

* Create reminder
* Open calendar
* Launch planner
* Search web

Deferred.

---

## Streaming Responses

Generation Engine may stream responses.

Response remains the final completed object.

Deferred.

---

## Event Bus

Possible future architecture

```
TeachingCompleted

↓

Reflection

Analytics

Logger

Planner
```

Deferred.

---

## Trace System

Possible future

```
Request

↓

Trace

↓

Timeline
```

Events

* Request Created
* Memory Retrieved
* TeachingPlan Generated
* Response Generated
* Reflection Completed

Deferred.

---

## Future Interfaces

Potential abstractions

* CalendarService
* NotificationService
* SpeechRecognizer
* SpeechSynthesizer
* Planner
* ResearchEngine

Deferred.

---

## C++ Opportunities

Potential candidates

* Memory indexing
* Similarity search
* Scheduling
* Voice pipeline
* Local inference
* Knowledge graph traversal

Python remains the orchestration layer.

---

# Open Questions

* Should Session become the aggregate root?
* Should FollowUp become its own domain object?
* Should Response support structured actions?
* Should Reflection become asynchronous?
* Should Atlas support multiple active sessions?
* Should Memory become event sourced?
* Should Planner become an independent agent?
* How should long-term memory decay work?

---

# Sprint 1 Summary

## Completed

* Core domain model established.
* Atlas domain language defined.
* Engineering principles documented.

### Domain Objects

* Request
* Response
* Session
* Memory
* TeachingPlan

---

## Most Important Architectural Decisions

* Request is immutable.
* Response is immutable.
* Session is mutable.
* Memory stores processed knowledge.
* Embeddings belong to Infrastructure.
* Teaching is separated from language generation.
* Every interaction enters Atlas as a Request.

---

# Long-Term Vision

Atlas is intended to become a personal AI learning and productivity partner.

Core goals

* Teach effectively.
* Remember long-term context.
* Challenge assumptions.
* Improve critical thinking.
* Assist with planning.
* Coordinate specialized agents.
* Support voice-first interaction.
* Remain modular, secure, testable, and extensible.

---

> "Good software is not defined by the number of classes it contains.
>
> It is defined by how clearly those classes model reality."
