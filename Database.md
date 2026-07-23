# DATABASE.md

## Philosophy

The database exists to persist Atlas's understanding of the user.

It is **not** a chat history database.

It stores knowledge, progress, context, and insights.

The application should work entirely with domain objects. The database is only a persistence layer.

---

# Database Overview

Sprint 1 consists of six tables.

```text
Identity
Learning
Workspace
Insights
Decisions
Sessions
```

Later versions may introduce:

* Conversations
* Documents
* Tasks
* Calendar
* Papers
* Goals
* Relationships
* Embeddings

Those are **not** part of Sprint 1.

---

# Table 1 — Identity

Purpose

Store facts explicitly told by the user.

Example

* Name
* Preferred explanation style
* Long-term goals
* Preferred programming language

Columns

```text
id

key

value

created_at

updated_at
```

Example

| key             | value                                |
| --------------- | ------------------------------------ |
| preferred_style | analogy                              |
| preferred_name  | Bhanu                                |
| goal            | Become an excellent systems engineer |

Identity changes infrequently.

---

# Table 2 — Learning

Purpose

Track learning progress.

Columns

```text
id

domain

topic

status

confidence

last_reviewed

created_at

updated_at
```

Status

```text
NOT_STARTED

IN_PROGRESS

COMPLETED
```

Example

| Topic              | Status      | Confidence |
| ------------------ | ----------- | ---------- |
| Mutex              | Completed   | 0.95       |
| Semaphore          | Completed   | 0.82       |
| Condition Variable | In Progress | 0.42       |

This table answers

> "Where is Bhanu in his learning journey?"

---

# Table 3 — Workspace

Purpose

Represent current working context.

Columns

```text
id

workspace_name

current_task

status

blocked_by

next_step

last_active

updated_at
```

Example

Workspace

Atlas

Current Task

Memory Engine

Blocked By

Database schema

Next Step

Implement Memory Engine

Workspace is highly dynamic.

Think of it as RAM.

---

# Table 4 — Insights

Purpose

Store inferred patterns.

Columns

```text
id

category

description

confidence

evidence_count

created_at

updated_at
```

Example

Category

Learning Style

Description

Learns best using analogies.

Confidence

0.91

Evidence

12

Notice

Insights are inferred.

The user never inserts them directly.

Reflection Engine creates them.

---

# Table 5 — Decisions

Purpose

Remember important decisions and why they were made.

Columns

```text
id

title

reason

context

created_at
```

Example

Decision

Build CLI first.

Reason

Need strong architecture before UI.

Context

Sprint Planning

Decision Memory answers

> "Why did we choose this?"

---

# Table 6 — Sessions

Purpose

Maintain temporary conversational state.

Columns

```text
id

topic

status

current_step

started_at

last_activity

closed_at
```

Status

```text
ACTIVE

PAUSED

COMPLETED
```

Example

Topic

Operating Systems

Current Step

Condition Variables

Status

Paused

Next time the user says

> Continue

Atlas resumes this session.

---

# Relationships

Sprint 1 intentionally keeps relationships simple.

```text
Identity

Learning

Workspace

Insights

Decisions

Sessions
```

Each table is independent.

Reasoning Engine combines them.

This keeps the schema simple while the application logic evolves.

---

# Memory Lifecycle

Different memories live for different durations.

| Memory    | Lifetime       |
| --------- | -------------- |
| Identity  | Years          |
| Learning  | Months / Years |
| Workspace | Days / Weeks   |
| Insights  | Months         |
| Decisions | Forever        |

This distinction is important.

Atlas should never treat Workspace the same way it treats Identity.

---

# Confidence

Only inferred memories have confidence.

Examples

Insights

```text
Confidence

0.93
```

Learning

```text
Confidence

0.74
```

Identity does not require confidence because it comes directly from the user.

Decisions also do not require confidence.

They happened.

---

# Future Extensions

Sprint 2+

Conversation History

```text
Conversation

id

session_id

speaker

message

timestamp
```

Documents

```text
Document

title

path

summary

embedding
```

Tasks

```text
Task

title

priority

deadline

status
```

Embeddings

```text
Embedding

memory_id

vector
```

These will support semantic search and Retrieval-Augmented Generation (RAG) in later versions.

---

# Database Principles

1. Store knowledge, not prompts.
2. Keep tables independent.
3. Domain objects own business logic.
4. Database stores state only.
5. Schema should be easy to migrate.
6. Optimize for clarity before optimization.

---

# Sprint 1 Deliverable

At the end of Sprint 1, Atlas should be capable of:

* remembering user preferences
* tracking learning progress
* maintaining active workspaces
* recording engineering decisions
* resuming learning sessions
* storing inferred insights

This is enough to support a persistent AI companion without unnecessary complexity.
