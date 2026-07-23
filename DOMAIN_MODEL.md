# DOMAIN_MODEL.md

# Domain Model

## Philosophy

Atlas is built around **domain objects**, not databases or APIs.

A domain object represents a concept that exists regardless of implementation.

For example:

* A `Request` exists whether input comes from CLI, voice, or mobile.
* A `Memory` exists whether data is stored in SQLite or PostgreSQL.
* A `TeachingPlan` exists whether GPT, Claude, or a local model generates the final response.

Implementation details should never change the domain.

---

# Domain Objects

Sprint 1 introduces five core domain objects.

```text
Request

Response

Memory

Session

TeachingPlan
```

These become the language spoken throughout Atlas.

---

# Request

Represents one user interaction.

Responsibilities

* Capture user input
* Preserve metadata
* Pass structured information into the system

Attributes

```python
Request

id

text

source

timestamp

session_id
```

Example

```python
Request(
    text="Teach me deadlocks",
    source="CLI",
    session_id="os-001"
)
```

A Request never contains business logic.

---

# Response

Represents Atlas' final output.

Responsibilities

* Return information to the user
* Suggest next actions
* Preserve consistency across interfaces

Attributes

```python
Response

message

follow_up

actions
```

Example

```python
Response(
    message="Let's continue learning deadlocks.",
    follow_up=[
        "Quiz me",
        "Continue",
        "Give another analogy"
    ]
)
```

---

# Memory

Represents one persistent piece of knowledge.

Responsibilities

* Store information
* Maintain confidence (if inferred)
* Track timestamps

Attributes

```python
Memory

id

category

content

confidence

created_at

updated_at
```

Categories

* Identity
* Learning
* Workspace
* Insight
* Decision

Example

```python
Memory(
    category="Insight",
    content="Learns well through analogies",
    confidence=0.91
)
```

---

# Session

Represents an active interaction.

Responsibilities

* Maintain conversational continuity
* Resume unfinished work
* Preserve temporary state

Attributes

```python
Session

id

topic

status

started_at

last_activity

current_step
```

Status

* ACTIVE
* PAUSED
* COMPLETED

Example

```python
Session(
    topic="Operating Systems",
    current_step="Condition Variables"
)
```

Sessions are temporary.

Learning Memory is permanent.

---

# TeachingPlan

Represents the teaching strategy.

Teacher returns a TeachingPlan.

Generation Engine converts it into language.

Responsibilities

* Define teaching approach
* Specify explanation style
* Control lesson flow

Attributes

```python
TeachingPlan

goal

strategy

difficulty

analogy

questions

expected_outcome
```

Example

```python
TeachingPlan(

goal="Teach Deadlocks",

strategy="Socratic",

difficulty="Intermediate",

analogy="Dining Philosophers",

questions=True
)
```

Notice

Teacher does **not** generate paragraphs.

Teacher generates plans.

---

# Relationships

```text
Conversation Manager

↓

Request

↓

Reasoning Engine

↓

TeachingPlan

↓

Generation Engine

↓

Response
```

Memory and Sessions provide context during reasoning.

---

# Domain Rules

## Request

Immutable.

Never modified after creation.

---

## Response

Represents the final output.

Contains no internal reasoning.

---

## Memory

Can evolve over time.

Confidence may increase or decrease.

---

## Session

Exists only while a task is active.

Closed sessions become historical records.

---

## TeachingPlan

Must be deterministic.

Given identical context, Teacher should produce the same plan.

---

# Why Domain Objects First?

Atlas is designed around concepts, not technologies.

This allows us to change:

* Database
* LLM provider
* User interface
* Storage backend

without changing the heart of the system.

The domain remains stable while implementations evolve.

---

# Sprint 1 Goal

By the end of Sprint 1, every component should communicate exclusively through these domain objects.

No component should pass raw dictionaries or ad-hoc JSON between modules.

The domain model becomes the shared language of Atlas.
