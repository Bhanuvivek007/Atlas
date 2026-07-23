# Atlas

> **A local-first AI thinking partner that learns with you.**

Atlas is an AI companion designed to help users learn deeply, think critically, and work more effectively through persistent memory, personalized reasoning, and long-term context.

Rather than behaving like a stateless chatbot, Atlas continuously builds an understanding of how you learn, what you're working on, and how it can help you think more clearly.

---

## Why Atlas?

Most AI assistants answer questions.

Atlas asks a different question:

> **"How can I help this person become a better thinker?"**

Atlas remembers:

* Your learning journey
* Your current work
* Your long-term goals
* Your reasoning patterns
* Important decisions you've made

Over time, it adapts its teaching style, challenges your assumptions, and becomes a personalized learning and productivity partner.

---

## Core Philosophy

* 🧠 Memory before intelligence
* 🎯 Local-first architecture
* 📚 Personalized learning
* 🤔 Socratic questioning over direct answers
* 🔒 User-owned data
* 🧩 Modular architecture
* 🚀 Provider-independent AI

---

## Architecture

```text
User
 │
 ▼
Conversation Manager
 │
 ▼
Reasoning Engine
 │
 ├── Teacher
 ├── Planner
 ├── Research
 │
 ▼
Attention Engine
 │
 ▼
Memory Engine
 │
 ▼
SQLite

↓

Generation Engine

↓

LLM Provider
```

---

## Memory Model

Atlas maintains five different memory types:

| Memory    | Purpose                                    |
| --------- | ------------------------------------------ |
| Identity  | Facts explicitly shared by the user        |
| Learning  | Learning progress and mastery              |
| Workspace | Current projects and active context        |
| Insights  | Inferred reasoning and learning patterns   |
| Decisions | Important decisions and why they were made |

---

## Project Roadmap

### Sprint 1

* Domain models
* Memory Engine
* CLI Conversation Manager
* Teacher
* Generation Engine
* Reasoning Engine

### Sprint 2

* Reflection Engine
* Attention Engine improvements
* Workspace management
* Better session handling

### Sprint 3

* Planner
* Research module
* Voice interface
* Calendar integration

### Future

* Independent specialist agents
* Semantic memory retrieval
* Local model support
* Mobile companion
* Knowledge graph
* Multi-device synchronization

---

## Technology Stack

* Python
* SQLite
* SQLAlchemy
* OpenAI API (replaceable)
* pytest

Future versions may support PostgreSQL, local LLMs, vector databases, and distributed specialist agents.

---

## Engineering Principles

* Every component has one responsibility.
* Domain objects come before databases.
* Business logic never lives inside storage.
* LLM providers are implementation details.
* Build systems that improve with use.

---

## Vision

Atlas is not intended to replace human thinking.

Its purpose is to become a long-term thinking partner that helps users learn faster, reason more clearly, and make better decisions through continuous dialogue and personalized guidance.

---

## Status

🚧 **Early Development (Sprint 1)**

Current focus:

* Architecture
* Domain model
* Memory Engine

This project is being built incrementally with a strong emphasis on software architecture, maintainability, and long-term usability rather than rapid prototyping.
