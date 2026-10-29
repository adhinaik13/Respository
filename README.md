<div align="center">

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/animated-portfolio-dashboard-v2.svg?v=1" width="100%" alt="Readable animated portfolio dashboard with illustrated profile, bold identity, orbital system map, and four featured projects"/>

**SYSTEMS ENGINEERING · BACKEND PLATFORMS · DEVELOPER TOOLS · OPEN SOURCE**

[EXPLORE PROJECT DEEP DIVES](#project-deep-dives) &nbsp; · &nbsp; [OPEN SOURCE](#open-source) &nbsp; · &nbsp; [CONTACT](mailto:22je1052@iitism.ac.in)

[Matching Engine](https://github.com/vankudothuadhinaik/low-latency-matching-engine) &nbsp; · &nbsp; [Uptime Sentinel](https://github.com/vankudothuadhinaik/uptime-sentinel) &nbsp; · &nbsp; [UPI Offline Mesh](https://github.com/vankudothuadhinaik/UPI_Without_Internet) &nbsp; · &nbsp; [DataPulse](https://github.com/vankudothuadhinaik/DataPulse-Analytics)

</div>

---

## ENGINEERING PRINCIPLES

<table>
<tr>
<td width="50%" valign="top">

### 01 · Invariants before implementation

Define state transitions, ownership rules, bounds, and idempotency guarantees first. Keep the matching core deterministic and make APIs reject invalid states at their boundaries.

</td>
<td width="50%" valign="top">

### 02 · Failure paths are part of the design

Test retries, timeouts, stale leases, partial failure, duplicate requests, recovery, and cleanup—not only successful requests. Fail closed when safe behavior cannot be established.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 03 · Evidence over confident guesses

Prefer source-linked evidence, reproducible tests, versioned data, migration checks, and explicit abstention over claims that cannot be verified. A passing metric must always state its scope.

</td>
<td width="50%" valign="top">

### 04 · Bound trust and resource use

Treat repository content and external inputs as untrusted. Validate paths and payloads, protect credentials, constrain response size and execution time, and keep security boundaries explicit.

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### 05 · Measure behavior, not headlines

Benchmark real workloads, record environment and compiler settings, inspect distributions and run-to-run variance, and distinguish a local demonstration from production guarantees.

</td>
</tr>
</table>

<div align="center">

**DESIGN → TEST → OBSERVE → IMPROVE**

</div>

---

## PROJECT DEEP DIVES

<sub>SYSTEMS · DEVELOPER TOOLS · JOB PROCESSING · RELIABILITY · PAYMENTS · ANALYTICS</sub>

### 01 — LOW-LATENCY MATCHING ENGINE

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-matching-engine.svg" width="100%" alt="Matching engine dashboard illustration showing the bid/ask book, price-time matching, and event pipeline"/>

A C++20 limit-order-book prototype with price-time priority, full and partial fills, indexed cancellation, order-ID lookup, and a bounded single-producer/single-consumer event path. The matching core is deliberately single-threaded; concurrency is isolated at the event boundary.

**STACK** &nbsp; C++20 · CMake · SPSC queue · Sanitizers · Benchmarks

**VERIFICATION** &nbsp; The repository's CI includes Release tests, a Debug AddressSanitizer/UndefinedBehaviorSanitizer run, cancellation-heavy workloads, and multi-workload benchmark artifacts. Throughput and latency depend on the measured environment; the README documents the workload and interpretation limits.

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/low-latency-matching-engine) · [CI &amp; artifacts ↗](https://github.com/vankudothuadhinaik/low-latency-matching-engine/actions) · [BENCHMARK METHODOLOGY ↗](https://github.com/vankudothuadhinaik/low-latency-matching-engine/blob/main/docs/BENCHMARKING.md)

---

### 02 — REPOPILOT

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-repopilot.svg" width="100%" alt="RepoPilot dashboard showing repository indexing, code search, source-line evidence, and grounded answers"/>

RepoPilot indexes local codebases and combines incremental indexing, Python symbol extraction, conservative cross-language import/include edges, SQLite FTS5 retrieval, line-addressable evidence, an API, optional MCP tools, and a React dashboard.

**STACK** &nbsp; Python · SQLite/FTS5 · FastAPI · MCP · React · TypeScript

**VERIFICATION** &nbsp; CI exercises Python 3.11/3.12, the offline single- and multi-repository evaluation suites, repository performance benchmarks, Windows file-safety tests, frontend browser tests, Docker/authentication smoke tests, CodeQL, and the optional MCP import. The curated evaluation cases still need independent second-person review; structural citation checks do not prove semantic entailment. Live-provider evaluation is optional and separate from ordinary CI.

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/RepoPilot) · [CI &amp; EVALUATION ARTIFACTS ↗](https://github.com/vankudothuadhinaik/RepoPilot/actions) · [EVALUATION LIMITS ↗](https://github.com/vankudothuadhinaik/RepoPilot/blob/main/docs/evaluation.md)

---

### 03 — FLUXQUEUE

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-fluxqueue.svg" width="100%" alt="FluxQueue pipeline showing API submission, durable PostgreSQL state, leased workers, retries, and dead-letter outcomes"/>

A durable job-processing platform built around validated job submission, tenant-scoped API keys, idempotency, PostgreSQL persistence, leases and heartbeats, stale-token fencing, bounded retries, terminal dead-letter state, and payload-free worker logs.

**STACK** &nbsp; Python · FastAPI · SQLAlchemy · PostgreSQL · Alembic · Docker

**VERIFICATION** &nbsp; Main CI and the documented manual smoke workflow cover database migrations, worker execution, lease/concurrency behavior, API authentication, and container startup. The free-tier hosted endpoint may sleep and has no production availability guarantee. Treat the demo as a portfolio demonstration, not an uptime commitment.

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/FluxQueue) · [CI RUNS ↗](https://github.com/vankudothuadhinaik/FluxQueue/actions) · [API DEMO ↗](https://fluxqueue-api.onrender.com/docs)

---

### 04 — UPTIME SENTINEL

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/uptime-sentinel/main/docs/images/architecture.svg" width="100%" alt="Uptime Sentinel monitoring architecture with API, worker, PostgreSQL, and controlled egress"/>

A FastAPI service for scheduled HTTP/HTTPS checks, latency and failure history, incident open/update/recovery, a read-only public status page, and a PostgreSQL-backed worker using shared leases and fencing.

**STACK** &nbsp; Python · FastAPI · PostgreSQL · SQLAlchemy · Docker Compose

**VERIFICATION** &nbsp; The latest recorded CI passes lint, format, typing, tests, PostgreSQL concurrency, dependency audit, migration round-trips, local proxy security fixtures, and a registration-to-worker Compose E2E flow. The external controlled-proxy integration remains an opt-in verification gate and is not claimed as passed. Paid hosting and production readiness are out of scope.

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/uptime-sentinel) · [CI RUNS ↗](https://github.com/vankudothuadhinaik/uptime-sentinel/actions) · [VERIFICATION REPORT ↗](https://github.com/vankudothuadhinaik/uptime-sentinel/blob/main/VERIFICATION_REPORT.md) · [RELEASE CHECKLIST ↗](https://github.com/vankudothuadhinaik/uptime-sentinel/blob/main/RELEASE_CHECKLIST.md)

---

### 05 — UPI OFFLINE MESH

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-upi-mesh.svg" width="100%" alt="UPI Offline Mesh prototype showing encrypted QR payloads, verification, and simulated reconciliation"/>

An offline-payment prototype exploring encrypted QR payloads, AES-GCM authenticated encryption, RSA-PSS signatures, duplicate/replay protection, and idempotent settlement once a message reaches the simulated gateway.

**STACK** &nbsp; Java 17 · Spring Boot · Cryptography · PostgreSQL · Flyway

**SCOPE &amp; VERIFICATION** &nbsp; The repository implements a backend settlement gateway, QR payment simulation, and server-side store-and-forward/mesh simulation. Native Bluetooth LE/Wi-Fi Direct transport, a native Android client, and real payment rails are not implemented. Java CI includes persistence and production-profile tests; these validate a prototype, not production payment security.

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/UPI_Without_Internet) · [CI RUNS ↗](https://github.com/vankudothuadhinaik/UPI_Without_Internet/actions) · [DEMO VIDEO ↗](https://youtu.be/_jcLwtK2IOU)

---

### 06 — DATAPULSE ANALYTICS

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-datapulse.svg" width="100%" alt="DataPulse Analytics ingestion and aggregation dashboard"/>

A portfolio-scale event analytics demo: validated event ingestion, SQLAlchemy persistence, metrics/top-event aggregation, PostgreSQL migrations, and a React + TypeScript dashboard.

**STACK** &nbsp; Python · FastAPI · Pydantic · SQLAlchemy · PostgreSQL · React · TypeScript

**VERIFICATION** &nbsp; CI runs backend endpoint and payload-validation tests, applies the initial Alembic schema to PostgreSQL, checks migration/model parity, and verifies that production startup does not silently create the schema. Full user authorization, ingestion rate limiting, and broader frontend/API workflows remain future work.

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/DataPulse-Analytics) · [CI RUNS ↗](https://github.com/vankudothuadhinaik/DataPulse-Analytics/actions)

<details>
<summary><strong>MORE BUILDS — ETL · TIME SERIES · FRONTEND</strong></summary>

### 07 — HEALTHSTREAM ETL

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-healthstream.svg" width="100%" alt="HealthStream ETL pipeline for validating, normalizing, deduplicating, and reporting synthetic encounter data"/>

A standard-library Python ETL pipeline for synthetic healthcare encounter events: input validation, normalization, duplicate handling, deterministic aggregation, and quality reports with row-level rejection reasons.

**VERIFICATION** &nbsp; CI checks the unit suite and sample end-to-end pipeline. Regression tests cover Decimal rounding, malformed CSV, duplicate headers, surplus fields, invalid dates, and clear input-row diagnostics. All data is fabricated; this is not a clinical or billing system.

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/HealthStream-ETL) · [CI RUNS ↗](https://github.com/vankudothuadhinaik/HealthStream-ETL/actions)

### 08 — AQI PREDICTION

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-aqi.svg" width="100%" alt="AQI forecasting evaluation chart showing chronological test window and persistence baseline"/>

A time-series forecasting exploration for Indian-city AQI, now with a reproducible chronological persistence baseline and input validation. The historical ARIMA/SARIMAX/Prophet metric table remains unverified because its original split and evaluation protocol were not fully documented.

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/Predicting-the-AQI-of-Indian-Cities-Using-Machine-Learning) · [BASELINE CI ↗](https://github.com/vankudothuadhinaik/Predicting-the-AQI-of-Indian-Cities-Using-Machine-Learning/actions)

### 09 — TODO LIST MANAGEMENT APPLICATION

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-todo-list.svg" width="100%" alt="Todo List Manager interface showing task entry, filters, completion states, and browser-local persistence"/>

A responsive React task manager with accessible controls, active/completed filters, input validation, empty states, and browser-local persistence. It is intentionally a frontend learning project, without a backend or cross-device sync.

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/TodoList-Management-Application) · [CI RUNS ↗](https://github.com/vankudothuadhinaik/TodoList-Management-Application/actions)

[SEE ALL PUBLIC REPOSITORIES ↗](https://github.com/vankudothuadhinaik?tab=repositories)

</details>

---

## 3D CONTRIBUTION CITY

<div align="center">

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/profile-3d-contrib/profile-night-rainbow.svg?v=2" width="100%" alt="Three-dimensional GitHub contribution city, refreshed daily by GitHub Actions"/>

<sub>A separate 3D activity visualization, refreshed by GitHub Actions. GitHub’s native contribution graph below the README remains the authoritative yearly total.</sub>

</div>

---

## OPEN SOURCE

**CPython #160707 — MERGED**  
Free-threaded garbage-collector traversal fix and regression coverage. · [Review the contribution ↗](https://github.com/python/cpython/pull/160707)

**CPython #160703 — CLOSED · NOT MERGED**  
Monitoring callback error propagation from `for` loops, with a regression test. Tier-2 runtime coverage was not demonstrated in the available build; the proposal was closed without merge. · [View contribution ↗](https://github.com/python/cpython/pull/160703)

**chunklet-py #107 — MERGED**  
Windows multiprocessing pickling fix and regression tests. · [Review the contribution ↗](https://github.com/speedyk-005/chunklet-py/pull/107)

**jvm-mcp #238 — OPEN**  
Spring bean discovery failures are reported as errors instead of misleading empty results, with safer diagnostics and regression coverage. · [View pull request ↗](https://github.com/oscarbol09/jvm-mcp/pull/238)

**jvm-mcp #239 — OPEN · DESCRIPTION INCOMPLETE**  
Detect Java versions from target JVM executable paths. The pull request is open, but its current description still contains template placeholders; treat it as work in progress until the description, checks, and maintainer review are complete. · [View pull request ↗](https://github.com/oscarbol09/jvm-mcp/pull/239)

**jvm-mcp #240 — OPEN**  
Preserve original JMX connection failure causes and close partially initialized connectors safely, including cleanup-failure tests. Timeout support remains explicitly out of scope. · [View pull request ↗](https://github.com/oscarbol09/jvm-mcp/pull/240)

**jvm-mcp #241 — OPEN**  
Make virtual-thread inspection opt-in, bound temporary thread-dump size, and test cleanup and Java 21 behavior. · [View pull request ↗](https://github.com/oscarbol09/jvm-mcp/pull/241)

**jvm-mcp #242 — OPEN**  
Reduce false-positive framework detection and resolve relative JAR paths against the target JVM working directory on Linux when available. Windows/macOS resolution remains limited. · [View pull request ↗](https://github.com/oscarbol09/jvm-mcp/pull/242)

**ATTRIBUTION NOTE**  
jvm-mcp #230 belongs to another contributor (Chandu0501) and is merged upstream; it is not listed as your contribution. This profile lists your own PRs #238–#242 and distinguishes open proposals from merged work.

**CPython #160714 — OPEN**  
`kqueue` interruption-handling proposal and regression test. · [View open proposal ↗](https://github.com/python/cpython/pull/160714)

<sub>Merged contributions and open proposals are intentionally distinguished.</sub>

## GITHUB ACTIVITY

<div align="center">

<a href="https://github.com/vankudothuadhinaik?tab=repositories"><strong>EXPLORE ALL REPOSITORIES ↗</strong></a> &nbsp; · &nbsp; <a href="https://github.com/vankudothuadhinaik?tab=overview">PROFILE OVERVIEW ↗</a>
<a href="https://github.com/vankudothuadhinaik?tab=repositories"><img width="49%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=vankudothuadhinaik&layout=compact&hide_border=true&bg_color=101923&title_color=EF8557&text_color=F6F0E6&langs_count=6&hide=Jupyter%20Notebook" alt="GitHub language distribution panel"/></a>

<a href="https://github.com/vankudothuadhinaik?tab=repositories"><img width="98%" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=vankudothuadhinaik&theme=github_dark" alt="GitHub profile contribution summary"/></a>

<sub>Live panels use external services and may occasionally be delayed or unavailable. The project illustrations above are design visuals, not live application metrics.</sub>

</div>

## TOOLKIT

<div align="center">

<img src="https://skillicons.dev/icons?i=cpp,java,python,spring,fastapi,react,ts,postgres,git,github,cmake,linux&perline=6" alt="C++, Java, Python, Spring, FastAPI, React, TypeScript, PostgreSQL, Git, GitHub, CMake and Linux technology icons"/>

</div>

---

<div align="center">

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/animated-connect.svg?v=3" width="100%" alt="Animated connect footer with GitHub and email links"/>

### BUILD WITH INTENT. VERIFY THE EDGE CASES.

**Backend engineering · Systems programming · Developer tools · Open source**

[EMAIL ME ↗](mailto:22je1052@iitism.ac.in) &nbsp; · &nbsp; [GITHUB ↗](https://github.com/vankudothuadhinaik)

</div>
