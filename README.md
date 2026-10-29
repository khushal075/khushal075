<a href="https://khushal075.github.io/">
  <img src="assets/architecture-banner.svg" width="100%" alt="Khushal — Enterprise architecture and applied AI. Connecting business goals, architecture decisions, and working systems." />
</a>

<p align="center">
  <a href="https://khushal075.github.io/"><img src="assets/icons/portfolio.svg" width="18" height="18" alt="" /> &nbsp;<strong>Explore my portfolio ↗</strong></a> &nbsp; · &nbsp;
  <a href="https://khushal075.github.io/blog/"><img src="assets/icons/notes.svg" width="18" height="18" alt="" /> &nbsp;Architecture notes</a> &nbsp; · &nbsp;
  <a href="https://khushal075.github.io/#playground"><img src="assets/icons/playground.svg" width="18" height="18" alt="" /> &nbsp;Interactive playground</a> &nbsp; · &nbsp;
  <a href="https://linkedin.com/in/khushal108"><img src="assets/icons/linkedin.svg" width="18" height="18" alt="" /> &nbsp;LinkedIn</a>
</p>

## Business intent → architecture decisions → working evidence

I connect business priorities with **enterprise architecture and applied AI**: defining system boundaries, making tradeoffs explicit, and validating decisions in working software.

My foundation is **7+ years of production ownership across Python and Java**, spanning distributed backends, multi-tenant platforms, and real-time communication. Here I share the code and reasoning behind those decisions.

| The question I start with | What I make explicit |
| :--- | :--- |
| What are we promising the customer? | Service boundaries, recovery expectations, and cost to serve |
| What stays shared? | Tenant scope, resource contention, and failure domains |
| Where does AI add value? | Workflow boundaries, model integration, and execution controls |

## Explore the systems

<a href="https://github.com/khushal075/fast_multi_tenant"><img src="assets/tenancy.svg" width="49%" alt="fast_multi_tenant: FastAPI scaffold exploring tenant context and PostgreSQL row-level data separation. Open repository." /></a>
<a href="https://github.com/khushal075/presence_service"><img src="assets/presence.svg" width="49%" alt="presence_service: distributed presence with WebSockets and Redis. Open repository." /></a>
<br />
<a href="https://github.com/khushal075/crewos"><img src="assets/ai.svg" width="49%" alt="CrewOS: two-step LLM workflows with tenant-aware asynchronous execution. Open repository." /></a>
<a href="https://github.com/khushal075/streamlens"><img src="assets/observability.svg" width="49%" alt="StreamLens: a decoupled log-ingestion and observability pipeline. Open repository." /></a>

**Want to interact with a system?** [Disconnect a simulated node and watch presence state change in the playground →](https://khushal075.github.io/#playground)

## Latest architecture notes

<!-- BLOG:START -->
- [Efficient agents need a workflow, not just a stronger model](https://khushal075.github.io/blog/efficient-agents-need-a-workflow/)
- [An AI workflow needs execution boundaries](https://khushal075.github.io/blog/ai-execution-needs-boundaries/)
- [When a connection disappears, when is a user offline?](https://khushal075.github.io/blog/presence-is-a-decision/)
- [Tenant isolation is a business decision](https://khushal075.github.io/blog/tenant-isolation-is-a-business-decision/)
<!-- BLOG:END -->

[All articles →](https://khushal075.github.io/blog/) · [Subscribe via RSS](https://khushal075.github.io/rss.xml)

<sub>This reading list refreshes daily from my blog.</sub>

<details>
<summary><strong>Applied AI: what CrewOS demonstrates today</strong></summary>

CrewOS currently executes a **fixed two-step LLM workflow** with tenant authentication, task-ownership checks, tenant-specific Celery routing, bounded inference retries, and an OpenAI-compatible model adapter. Ollama is a local inference option.

Tool-using agent loops, persistent memory, durable checkpoints, approvals, and multi-agent evaluation are planned. The architecture articles discuss broader patterns separately from implemented project capabilities.

[Inspect the implementation →](https://github.com/khushal075/crewos)

</details>

<details>
<summary><strong>Production experience, toolkit, and education</strong></summary>

My work includes multi-tenant notification platforms, WebSocket communication and presence systems, client data-migration pipelines, and reusable platform libraries.

**Languages & frameworks:** Python · Java · FastAPI · Django · Spring Boot  
**Data & messaging:** PostgreSQL · Redis · Snowflake  
**Infrastructure:** AWS · GCP · Kubernetes · Docker · Prometheus · Grafana

**M.Tech — IIT Kanpur** (2012–2015)  
**B.Tech — Engineering College, Bikaner** (2007–2011)

</details>

---

**Let’s connect:** [LinkedIn](https://linkedin.com/in/khushal108) · [Email](mailto:khushal.jobss@gmail.com) · [Portfolio](https://khushal075.github.io/)

Open to conversations about enterprise architecture, Staff Engineer, and technical leadership opportunities.
