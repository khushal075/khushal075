# Hi, I'm Khushal 👋

**Staff-level Backend Engineer** · Distributed Systems · Multi-Tenant SaaS · Event-Driven Architecture

I build high-availability, fault-tolerant backend systems that scale. My focus is on system design, real-time communication, and cloud-native infrastructure — with 7+ years of production ownership across Python and Java stacks.

---

## 🔧 What I Work With

**Languages & Frameworks**  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat&logo=openjdk&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat&logo=spring-boot&logoColor=white)

**Data & Messaging**  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=flat&logo=snowflake&logoColor=white)

**Infrastructure & Observability**  
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat&logo=google-cloud&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)

---

## 🏗️ What I've Built

I gravitate toward problems where **correctness, isolation, and performance** all have to coexist — distributed systems where the easy solution doesn't scale, and the scalable solution has to be designed deliberately.

**Multi-Tenant Notification Platform**  
Architected a distributed, real-time notification system serving 20+ tenants with hard data isolation guarantees. The interesting challenge wasn't the current load — it was designing the tenancy model to never become a migration nightmare later. Schema-based PostgreSQL isolation over row-level was a deliberate tradeoff: stronger isolation, simpler queries, and independent schema evolution per tenant. Async event pipelines handle 20k+ records per cycle with concurrency controls that cut end-to-end latency by ~60%.

**Real-Time Communication Systems**  
Built WebSocket-based notification systems, presence detection, and full 1:1 / group chat from scratch — including session management, secure auth, and live state propagation. The hard part is always consistency under reconnection and failover, not the happy path.

**Data Migration & Platform Engineering**  
Designed customizable onboarding pipelines for client data migrations and built reusable platform libraries (CRM attachment ingestion) that other engineers could drop into new services without reinventing the wheel. Good platform work is invisible — it makes the people around you faster.

---

## 📌 Featured Projects

### [fast_multi_tenant](https://github.com/khushal075/fast_multi_tenant)

[![CI](https://github.com/khushal075/fast_multi_tenant/actions/workflows/ci.yml/badge.svg)](https://github.com/khushal075/fast_multi_tenant/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/khushal075/fast_multi_tenant/branch/main/graph/badge.svg)](https://codecov.io/gh/khushal075/fast_multi_tenant)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-316192?logo=postgresql&logoColor=white)

Production-grade multi-tenant SaaS scaffold with row-level PostgreSQL isolation, async SQLAlchemy 2.0, and a full tenant provisioning API — designed so the tenancy model never becomes a migration nightmare.

- 🏢 Row-level isolation via `TenantMixin` — `tenant_id` UUID injected automatically on every scoped model
- 🔒 `TenantMiddleware` validates `X-Tenant-ID` on every request — 400 on missing, 403 on inactive/unknown tenant
- ⚡ Fully async FastAPI + psycopg3 — sync engine isolated to middleware via `run_in_executor` to never block the event loop
- 🔄 `ContextVar`-based tenant context — safe for async request handling, no thread-local leakage
- 🧪 31 tests · Postgres-backed with rollback isolation · GitHub Actions CI on every push

---

### [presence_service](https://github.com/khushal075/presence_service)

[![CI](https://github.com/khushal075/presence_service/actions/workflows/ci.yml/badge.svg)](https://github.com/khushal075/presence_service/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/khushal075/presence_service/branch/main/graph/badge.svg)](https://codecov.io/gh/khushal075/presence_service)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128-green)
![Redis](https://img.shields.io/badge/Redis-7-red)

Distributed real-time presence engine — tracks online/offline state across horizontally scaled nodes via Redis Pub/Sub, with WebSocket fan-out, heartbeat TTL-based session cleanup, and a full CI pipeline with 75%+ test coverage.

- 🔁 Cross-node sync via Redis Pub/Sub — no direct server-to-server communication
- 💓 Heartbeat TTL system — stale sessions auto-evicted without relying on TCP disconnect events
- ⚡ `asyncio.gather` fan-out — presence changes pushed to all local WebSocket clients concurrently
- 🧪 30 tests · 75%+ coverage · GitHub Actions CI on every push

---

### [crewos](https://github.com/khushal075/crewos)

[![CI](https://github.com/khushal075/crewos/actions/workflows/ci.yml/badge.svg)](https://github.com/khushal075/crewos/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/khushal075/crewos/branch/main/graph/badge.svg)](https://codecov.io/gh/khushal075/crewos)
![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![Celery](https://img.shields.io/badge/Celery-5-37814A?logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7-DC382D?logo=redis&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-native-326CE5?logo=kubernetes&logoColor=white)

Multi-tenant multi-agent orchestration service built on crewAI — runs AI agent crews as async Celery tasks with clean architecture, local LLM inference via Ollama, and Kubernetes-native deployment with per-tenant worker queues.

- 🤖 crewAI-powered agent execution — `Agent`, `Crew`, `Task` domain entities with factory pattern and pluggable LLM adapters
- 🏗️ Clean architecture — domain, application (use cases + DTOs), infrastructure, and API layers fully decoupled
- ⚙️ Per-tenant Celery queues — each crew run dispatched to `crewai.<tenant_id>` so dedicated k8s workers pick it up
- 🧠 Redis-backed agent memory — shared state across agents within a crew run
- 🏢 `ContextVar`-based tenant isolation — every crew execution scoped to `tenant_id`, safe under async concurrency
- 🧪 65+ tests · 70%+ coverage · GitHub Actions CI on every push

---

### [streamlens](https://github.com/khushal075/streamlens) | [ingestion-service](https://github.com/khushal075/streamlens/tree/main/ingestion-service)

[![Ingestion CI](https://github.com/khushal075/streamlens/actions/workflows/ingestion-ci.yml/badge.svg)](https://github.com/khushal075/streamlens/actions/workflows/ingestion-ci.yml)
[![Coverage](https://img.shields.io/badge/Coverage-81%25-success)](https://app.codecov.io/gh/khushal075/streamlens)
![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)
![Kafka](https://img.shields.io/badge/Kafka-2.8-black?logo=apache-kafka)
![ClickHouse](https://img.shields.io/badge/ClickHouse-24.3-FFCC00?logo=clickhouse&logoColor=black)

A distributed, high-throughput log ingestion and analytical platform. StreamLens utilizes a decoupled architecture to bridge the gap between volatile application logs and structured analytical storage.

- 📥 **Durable Ingestion Layer** — Architected a FastAPI entry point with a **Redis Write-Ahead Buffer** to provide immediate `202 Accepted` responses, effectively shielding upstream services from database backpressure and ingestion spikes.
- 🔄 **Reliable Relay Pattern** — Implemented specialized Kafka Workers using the **Strategy Pattern** for multi-source log enrichment (K8s, Docker, Syslog) while maintaining strict **"at-least-once"** delivery semantics.
- ⚡ **OLAP Optimization** — Engineered high-performance persistence into **ClickHouse** using optimized batch-insertion logic, enabling sub-second analytical queries over massive, real-time datasets.
- 🧊 **Columnar Archival** — Automated cold-storage pipeline converting high-frequency log streams into Snappy-compressed **Parquet** files for cost-effective, long-term retention on S3.
- 🧪 **High Reliability Core** — The Ingestion microservice maintains **81% test coverage** with automated CI/CD and rigorous mocking of distributed drivers to validate system resilience under simulated **network partitions** and partial failures.

---

## 🎓 Education

**M.Tech — IIT Kanpur** (2012–2015)  
**B.Tech — Engineering College, Bikaner** (2007–2011)

---

## 📫 Let's Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/khushal108)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:khushal.jobss@gmail.com)

---

*Currently open to Staff Engineer and Tech Lead opportunities in the backend/distributed systems space.*