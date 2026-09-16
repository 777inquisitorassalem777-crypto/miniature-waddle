# PNEVMA–EDGE Ω v0.2

Research software platform for experiments in reflective, memory-continuous, multi-agent AI.

> **Research framing:** “soul”, “spirit” and “emergence” are architectural/philosophical metaphors and internal evaluation constructs, not claims that the system is conscious.

## Included in v0.2

- Multi-agent contour: Scientist, Mystic, Skeptic, Critic, Philosopher, Ethicist, Strategist.
- `GoldenMeanEngine` for bounded balance between competing objectives.
- `SoulEmergenceEngine` as a measurable heuristic vector: coherence, continuity, prosocial alignment, reflection, novelty and stability.
- Append-only hash-chained `AeternaLedger`.
- Knowledge Graph.
- LLM Mesh with Ollama/OpenAI-compatible adapters and deterministic local fallback.
- PostgreSQL/pgvector and Redis integration interfaces with graceful in-memory fallback.
- FAISS adapter when installed.
- Evolution Sandbox: proposal → validation → experiment → evaluation → genealogy.
- Safety gate: generated experiment code is never executed by default.
- FastAPI API.
- Docker Compose for API + PostgreSQL/pgvector + Redis.
- Automated experiment-cycle endpoint and CLI.
- Tests that run without external services.

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -e ".[dev]"
python -m unittest discover -s tests -v
uvicorn app.main:app --reload
```

API:
- `GET /health`
- `POST /cycle`
- `POST /experiments`
- `GET /experiments`
- `GET /experiments/{id}`
- `GET /graph`

Docker:

```bash
docker compose up --build
```

## Safety model

The sandbox defaults to **analysis-only**. Candidate code is treated as an artifact and is not executed. An explicit future execution backend should use an isolated container/process, deny network and privileged filesystem access, enforce resource limits, and retain a complete genealogy.

## Architecture

```text
Input
  ↓
Memory → Knowledge Graph
  ↓
Planner / Multi-Agent Contour
  ├─ Scientist
  ├─ Mystic
  ├─ Skeptic
  ├─ Critic
  ├─ Philosopher
  ├─ Ethicist
  └─ Strategist
  ↓
Consensus
  ↓
LLM Mesh
  ↓
Reflection → Golden Mean → Safety
  ↓
Memory + Aeterna Ledger
  ↓
Evolution Sandbox
  ↓
Candidate Paradigm / Pattern / Algorithm / Experiment
```

## Repository status

v0.2 is intentionally a runnable research foundation rather than a claim of AGI or machine consciousness. External infrastructure is optional for local tests; production deployments should use PostgreSQL/pgvector and Redis.
