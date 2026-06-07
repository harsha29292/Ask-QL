<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:0F766E,100:2563EB&text=AskQL&fontColor=ffffff&fontSize=56&fontAlignY=38&desc=Schema-aware%20Natural%20Language%20to%20SQL&descAlignY=58&descSize=18" alt="AskQL logo banner" />

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img alt="Docker" src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img alt="Ollama" src="https://img.shields.io/badge/Ollama-LLM-000000?style=for-the-badge&logo=ollama&logoColor=white" />
</p>

<p>
AskQL turns natural-language analytics questions into safe, schema-aware SQL over PostgreSQL.
</p>

</div>

---

## What Is AskQL?

AskQL is a natural-language-to-SQL engine built around database structure, not just prompt engineering. It introspects a PostgreSQL schema, retrieves the most relevant tables, plans valid join paths, generates SQL, validates it, executes it, and returns a readable answer.

Example questions:

- "Top 5 paying customers"
- "Revenue this year"
- "Organizations with the most users"
- "Customers with active subscriptions and overdue invoices"

---

## Why It Exists

Most NL-to-SQL prototypes work on small schemas, then break as soon as the database becomes realistic. The hard part is not only generating SQL. The hard part is understanding the schema, choosing the right tables, planning joins, applying filters, and avoiding invalid or misleading queries.

AskQL tackles that problem with a schema-aware pipeline:

```text
User Query
   |
   v
Intent Parsing
   |
   v
Embedding Generation
   |
   v
Semantic Table Retrieval
   |
   v
Table Reranking
   |
   v
Schema Graph Join Planning
   |
   v
SQL Generation
   |
   v
Validation and Repair
   |
   v
PostgreSQL Execution
   |
   v
Readable Answer
```

---

## Core Features

- Automatic PostgreSQL schema introspection
- Schema graph construction from tables, columns, and foreign keys
- Semantic retrieval over schema metadata
- Table reranking to reduce irrelevant joins
- Intent parsing for aggregations, grouping, ranking, limits, and filters
- Dynamic join-path discovery
- SQL validation and repair flow
- Natural-language answer formatting
- FastAPI service layer
- Dockerized deployment
- Test coverage for pipeline, retrieval, joins, filters, validation, and query behavior

---

## Tech Stack

<p>
  <img alt="Python" src="https://skillicons.dev/icons?i=python" width="42" />
  <img alt="FastAPI" src="https://skillicons.dev/icons?i=fastapi" width="42" />
  <img alt="PostgreSQL" src="https://skillicons.dev/icons?i=postgresql" width="42" />
  <img alt="Docker" src="https://skillicons.dev/icons?i=docker" width="42" />
  <img alt="Git" src="https://skillicons.dev/icons?i=git" width="42" />
</p>

| Layer | Tools |
| --- | --- |
| API | FastAPI, Uvicorn |
| Database | PostgreSQL, psycopg2 |
| Embeddings / LLM | Ollama HTTP APIs |
| Retrieval | NumPy vector similarity, local embedding cache |
| Deployment | Docker, Docker Compose |
| Testing | Pytest |

---

## Repository Structure

```text
askql/
|-- app/
|   |-- api/              # FastAPI entrypoint
|   |-- core/             # Pipeline, retrieval, planning, validation, repair
|   |-- db/               # PostgreSQL execution and introspection
|   `-- llm/              # Ollama client
|-- database/             # Schema and seed helpers
|-- tests/                # Unit and integration-style tests
|-- Dockerfile
|-- docker-compose.yml
`-- requirements.txt
```

---

## Getting Started

### 1. Clone and install

```bash
git clone <your-repo-url>
cd askql
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment

Create a `.env` file:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
```

When running inside Docker and connecting to PostgreSQL on the host machine, use:

```env
DB_HOST=host.docker.internal
```

### 3. Start Ollama

AskQL currently calls Ollama at:

```text
http://host.docker.internal:11434
```

Make sure Ollama is running and the required generation / embedding models are available.

### 4. Run the API locally

```bash
uvicorn app.api.main:app --reload --host 0.0.0.0 --port 8000
```

Health check:

```bash
curl http://localhost:8000/health
```

---

## Docker

Build and run the service:

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:8000
```

---

## API Usage

### `GET /health`

```json
{
  "status": "healthy"
}
```

### `POST /query`

Request:

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d "{\"query\":\"top 5 paying customers\"}"
```

Response shape:

```json
{
  "query": "top 5 paying customers",
  "tables": ["customers", "payments", "invoices"],
  "sql": "SELECT ...",
  "answer": "1. Rowe, Cummings and Mays ($43,320.55)\n2. Williams and Sons ($33,482.82)"
}
```

---

## How It Works

### 1. Schema Introspection

AskQL reads tables, columns, foreign keys, and relationships directly from PostgreSQL. This creates a schema graph that becomes the source of truth for join planning.

```text
customers
   |
   v
invoices
   |
   v
payments
```

### 2. Schema RAG

The system embeds schema metadata and compares it with the user's question. This helps retrieve tables that are implied by the question, even when the table names are not mentioned directly.

For example, "highest revenue customers" may require both `invoices` and `payments`.

### 3. Intent Parsing

AskQL extracts structured intent from the user query:

- Aggregation: `COUNT`, `SUM`, `AVG`
- Ranking: ascending or descending
- Grouping entity
- Limit
- Status filters
- Date filters

### 4. Dynamic Join Planning

If two required tables do not connect directly, AskQL searches the schema graph for a valid path.

```text
customers -> invoices -> payments
```

### 5. SQL Validation and Answering

Generated SQL is checked before execution. Query results are then converted into a concise, human-readable response instead of returning raw rows only.

---

## Testing

Run the test suite:

```bash
pytest
```

The tests cover query planning, retrieval, reranking, filters, joins, validation, execution behavior, and answer formatting.

---

## Roadmap

- Support arbitrary PostgreSQL databases with minimal setup
- Add query caching
- Improve LLM-based SQL repair
- Add query explanations
- Add an interactive UI
- Expand the evaluation benchmark suite
- Support multi-tenant deployments

---

## Key Takeaway

AskQL evolved from simple semantic table lookup into a schema-aware retrieval and planning system for analytical SQL. The main lesson: reliable NL-to-SQL depends less on clever prompting and more on schema understanding, join planning, validation, and deployment discipline.
