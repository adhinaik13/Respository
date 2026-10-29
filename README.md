<div align="center">

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/profile-command-center.svg" width="100%" alt="Vankudothu Adhi Naik engineering portfolio cover in warm ivory, editorial blue, coral and chartreuse"/>

**INTEGRATED M.TECH · MATHEMATICS & COMPUTING · IIT (ISM) DHANBAD**

*I build systems that behave predictably — and test the edges where they don't.*

[EXPLORE PROJECTS](#selected-work) &nbsp; · &nbsp; [OPEN SOURCE](#open-source) &nbsp; · &nbsp; [CONTACT](mailto:22je1052@iitism.ac.in)

</div>

---

## THE ENGINEERING DNA

<div align="center">

**01 · SYSTEMS & PERFORMANCE**  
C++20 · Data structures · Order books · Concurrency

*Deterministic matching, event flow, and edge cases that expose hidden assumptions.*

**02 · BACKEND & DATA**  
Java · Spring Boot · Python · FastAPI · SQL

*Clear API contracts, validation, idempotency, useful tests, predictable failure handling.*

**03 · PRODUCT ENGINEERING**  
React · TypeScript · REST APIs

*Turning backend capability into a clear interface and practical user workflows.*

**04 · OPEN SOURCE**  
CPython · Python tooling · Regression tests

*Contributing fixes and tests that capture the bug—not just the happy path.*

</div>

## SELECTED WORK

<sub>TEN PROJECTS · SYSTEMS, PAYMENTS, ANALYTICS, DATA QUALITY, ML, STORAGE &amp; DEVELOPER TOOLS</sub>

### 01 — LOW-LATENCY MATCHING ENGINE
<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-matching-engine.svg" width="100%" alt="Custom matching engine systems dashboard showing bid book, price-time matching core and event path"/>

A C++20 limit-order-book prototype with price-time priority, full and partial fills, indexed order cancellation, order lookup, and a bounded single-producer/single-consumer event path. The latest implementation maintains queue-position iterators for efficient cancellation and includes a 1,000-order cancellation/FIFO stress test.

**STACK** &nbsp; `C++20` &nbsp; `CMake` &nbsp; `Testing` &nbsp; `Benchmarking`

**VERIFICATION** &nbsp; Release assertions remain enabled in tests; CI includes AddressSanitizer and UndefinedBehaviorSanitizer, cancellation-heavy workload checks, and five-workload benchmark evidence with runner/compiler metadata. Results are CI-run-specific, not universal hardware claims. [Inspect CI runs ↗](https://github.com/vankudothuadhinaik/low-latency-matching-engine/actions) · [Benchmark methodology ↗](https://github.com/vankudothuadhinaik/low-latency-matching-engine/blob/main/docs/BENCHMARKING.md)

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/low-latency-matching-engine)

---

### 02 — UPTIME SENTINEL

A FastAPI uptime-monitoring service for HTTP/HTTPS endpoints, with latency and failure tracking, incident lifecycle management, a read-only public status page, PostgreSQL-backed worker leases, and configurable cleanup of expired check history.

**STACK** &nbsp; `Python 3.12` &nbsp; `FastAPI` &nbsp; `PostgreSQL` &nbsp; `SQLAlchemy` &nbsp; `Docker Compose` &nbsp; `GitHub Actions`

**PROJECT STATUS** &nbsp; Free GitHub portfolio project · local Compose demo · no paid hosting required.

**VERIFICATION** &nbsp; [latest main CI run #233](https://github.com/vankudothuadhinaik/uptime-sentinel/actions/runs/40849831440) passed after documentation updates. The merged PR #11 was validated in [run #229](https://github.com/vankudothuadhinaik/uptime-sentinel/actions/runs/40849371364): `checks`, `compose-smoke`, and the newly required `proxy-local-integration` job passed (29 controlled local proxy security tests). A local Docker Compose E2E run on 2026-10-29 verified readiness, registration/login, monitor creation, worker processing, persisted HTTP 200 check results, and public status. GitHub Secret Scanning showed 0 open and 0 closed alerts in the repository UI screenshot on 2026-10-29; a separate Advanced Security screenshot confirmed Push Protection was On. The separate external controlled-proxy integration remains opt-in and skipped until dedicated fixture URLs/secrets are configured; it is not claimed as passed. [Verification report](https://github.com/vankudothuadhinaik/uptime-sentinel/blob/main/VERIFICATION_REPORT.md) · [Release checklist](https://github.com/vankudothuadhinaik/uptime-sentinel/blob/main/RELEASE_CHECKLIST.md). No production deployment is claimed.

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/uptime-sentinel/main/docs/images/architecture.svg" width="100%" alt="Uptime Sentinel architecture diagram showing API, worker, PostgreSQL and controlled egress boundary"/>

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/uptime-sentinel) · [LATEST CI RUNS ↗](https://github.com/vankudothuadhinaik/uptime-sentinel/actions) · [PROJECT README ↗](https://github.com/vankudothuadhinaik/uptime-sentinel/blob/main/README.md) · [RELEASE CHECKLIST ↗](https://github.com/vankudothuadhinaik/uptime-sentinel/blob/main/RELEASE_CHECKLIST.md) · [SECURITY TEST PLAN ↗](https://github.com/vankudothuadhinaik/uptime-sentinel/blob/main/EGRESS_PROXY_TESTING.md)

---

### 03 — UPI OFFLINE MESH
<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-upi-mesh.svg" width="100%" alt="Custom UPI Offline Mesh dashboard showing encrypted payload, signature verification, safe queueing and simulated reconciliation"/>

An offline-payment prototype exploring encrypted QR payloads, RSA-PSS signatures, replay protection, idempotency, and simulated store-and-forward settlement.

**STACK** &nbsp; `Java 17` &nbsp; `Spring Boot` &nbsp; `AES-GCM` &nbsp; `RSA-PSS`

**VERIFICATION** &nbsp; CI validates the Java build and Docker image; a separate PostgreSQL + Redis production-profile test job passes, including Flyway startup and the current test suite. The latest work also fixes provisional idempotency-claim cleanup and aligns the production schema with the JPA entities. These checks validate the prototype's test configuration—not real payment rails or production security readiness. [Inspect CI runs ↗](https://github.com/vankudothuadhinaik/UPI_Without_Internet/actions) · [Persistence/retry PR ↗](https://github.com/vankudothuadhinaik/UPI_Without_Internet/pull/8)

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/UPI_Without_Internet)

---

### 04 — DATAPULSE ANALYTICS
<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-datapulse.svg" width="100%" alt="Custom DataPulse Analytics dashboard showing event volume illustration, FastAPI ingestion, validation and dashboard layers"/>

A full-stack event-analytics prototype combining API ingestion and aggregation, SQLAlchemy models, and a React + TypeScript dashboard. The chart in this illustration is sample artwork, not live product telemetry.

**STACK** &nbsp; `FastAPI` &nbsp; `SQLAlchemy` &nbsp; `React` &nbsp; `TypeScript`

**VERIFICATION** &nbsp; Backend endpoint tests pass; CI also applies the initial Alembic schema to PostgreSQL 16, checks ORM/migration parity, and verifies production startup does not run implicit schema creation. Rate limiting, full user authorization, and broader PostgreSQL API integration coverage remain incomplete. [Inspect CI runs ↗](https://github.com/vankudothuadhinaik/DataPulse-Analytics/actions) · [Migration PR ↗](https://github.com/vankudothuadhinaik/DataPulse-Analytics/pull/8)

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/DataPulse-Analytics)

### 05 — HEALTHSTREAM ETL

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-healthstream.svg" width="100%" alt="HealthStream ETL dashboard illustration showing ingestion, validation, normalization, deduplication and data-quality reporting"/>

A synthetic healthcare-event pipeline focused on data quality: validation, normalization, deduplication, and quality reporting. The illustration describes the workflow; it does not display patient data or live pipeline telemetry.

**FOCUS** &nbsp; `ETL` &nbsp; `Data validation` &nbsp; `Normalization` &nbsp; `Deduplication`

**VERIFICATION** &nbsp; CI passes unit tests and the sample pipeline; regression tests cover Decimal rounding, deterministic output, malformed CSV quoting, duplicate headers, surplus row fields, and source-row diagnostics. Source CSV is read incrementally, while accepted rows and rejection details are still retained in memory. [Inspect CI runs ↗](https://github.com/vankudothuadhinaik/HealthStream-ETL/actions) · [CSV validation PR ↗](https://github.com/vankudothuadhinaik/HealthStream-ETL/pull/8)

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/HealthStream-ETL)

---

### 06 — AQI PREDICTION

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-aqi.svg" width="100%" alt="AQI prediction dashboard illustration with time-series trend, persistence baseline and station-wise evaluation workflow"/>

An air-quality prediction project exploring time-series evaluation with a chronological persistence baseline and per-station comparisons. The chart is illustrative, not a live air-quality feed.

**FOCUS** &nbsp; `Python` &nbsp; `Time series` &nbsp; `Baseline evaluation` &nbsp; `Air quality`

**VERIFICATION** &nbsp; CI validates notebook/data structure and publishes commit-specific persistence-baseline metrics; regression tests cover malformed CSV quoting, duplicate headers, surplus fields, invalid dates, and non-finite AQI values. Historical ARIMA/SARIMAX/Prophet scores remain unverified. [Inspect CI runs ↗](https://github.com/vankudothuadhinaik/Predicting-the-AQI-of-Indian-Cities-Using-Machine-Learning/actions) · [CSV validation PR ↗](https://github.com/vankudothuadhinaik/Predicting-the-AQI-of-Indian-Cities-Using-Machine-Learning/pull/7)

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/Predicting-the-AQI-of-Indian-Cities-Using-Machine-Learning)

---

<details>
<summary><strong>MORE BUILDS — DEVELOPER TOOLS · STORAGE · JOB QUEUES · FRONTEND</strong></summary>

### 07 — REP PILOT

Evidence-grounded repository intelligence with local indexing, Python symbol discovery, static import edges, SQLite/FTS search, cited source snippets, optional OpenAI-compatible answers, and MCP tools. The synthetic 50-query benchmark is a reproducibility fixture, not a real-world accuracy claim.

**VERIFICATION** &nbsp; Main CI passes lint, core mypy, tests, compilation, retrieval evaluation, frontend production build, Docker build, and optional MCP import. The API's shared bearer token is not full identity, role-based authorization, or tenant isolation. [Source ↗](https://github.com/vankudothuadhinaik/RepoPilot) · [CI runs ↗](https://github.com/vankudothuadhinaik/RepoPilot/actions)

### 08 — STOREFORGE

An educational object-storage system with content-addressed chunks, SHA-256 integrity checks, SQLite/PostgreSQL metadata options, a three-node replicated demo, replica fallback, and object metadata operations.

**VERIFICATION** &nbsp; Latest main CI passes Ruff, format, mypy, tests, container build, and a three-node integration check for binary upload/download, replica failover, API restart, and PostgreSQL metadata. This local Compose demo does not prove independent hardware failure tolerance; user authentication and automated garbage collection remain unimplemented. [Source ↗](https://github.com/vankudothuadhinaik/StoreForge) · [CI runs ↗](https://github.com/vankudothuadhinaik/StoreForge/actions)

### 09 — FLUXQUEUE

A durable job-processing foundation using FastAPI, SQLAlchemy, PostgreSQL, Alembic, idempotency keys, worker leases, lease fencing, retries, and a dead-letter state.

**VERIFICATION** &nbsp; CI exercises schema migrations and PostgreSQL lease fencing, with API/worker tests and container smoke checks. Execution is at-least-once; authentication and tenant authorization remain outstanding. CodeQL scans source, but SARIF upload permission is still being addressed, so the analysis job is advisory rather than proof of a published clean report. [Source ↗](https://github.com/vankudothuadhinaik/FluxQueue) · [CI runs ↗](https://github.com/vankudothuadhinaik/FluxQueue/actions)

### 10 — TODO LIST MANAGEMENT APPLICATION

A React task workflow with accessible actions and localStorage persistence. [Source ↗](https://github.com/vankudothuadhinaik/TodoList-Management-Application)

[SEE ALL REPOSITORIES ↗](https://github.com/vankudothuadhinaik?tab=repositories)

</details>


---

## OPEN SOURCE

**CPython #160707 — MERGED**  
Free-threaded garbage-collector traversal fix and regression coverage. · [Review the contribution ↗](https://github.com/python/cpython/pull/160707)

**CPython #160703 — CLOSED · NOT MERGED**  
Monitoring callback error propagation from `for` loops, with a regression test. Tier-2 runtime coverage was not demonstrated in the available build; the proposal was closed without merge. · [View contribution ↗](https://github.com/python/cpython/pull/160703)

**chunklet-py #107 — MERGED**  
Windows multiprocessing pickling fix and regression tests. · [Review the contribution ↗](https://github.com/speedyk-005/chunklet-py/pull/107)

**jvm-mcp #238 — OPEN · CHECKS PASSING**  
Spring bean discovery error reporting: distinguish failed Actuator/JMX discovery from a genuinely empty application context, preserve safe diagnostics, and add regression tests. Required GitHub Actions checks are passing; awaiting maintainer review. · [View pull request ↗](https://github.com/oscarbol09/jvm-mcp/pull/238)

**jvm-mcp #239 — OPEN · CHECKS PASSING**  
Detect Java versions from JVM executable paths. GitHub Actions checks pass and the branch has no reported conflicts; PR description and maintainer review remain pending. · [View pull request ↗](https://github.com/oscarbol09/jvm-mcp/pull/239)

**jvm-mcp #240 — OPEN · CHECKS PASSING**  
Preserve root causes when JMX connections fail and close partially initialized connectors safely, with regression tests for cleanup behavior. · [View pull request ↗](https://github.com/oscarbol09/jvm-mcp/pull/240)

**jvm-mcp #241 — OPEN · CHECKS PASSING**  
Make virtual-thread summary inspection opt-in to avoid unnecessary thread-dump work; add CLI/MCP controls, size limits, cleanup, and Java 21 coverage. · [View pull request ↗](https://github.com/oscarbol09/jvm-mcp/pull/241)

**jvm-mcp #242 — OPEN · CHECKS PASSING**  
Correct framework detection and improve relative JAR-path resolution using the target JVM's working directory when available. · [View pull request ↗](https://github.com/oscarbol09/jvm-mcp/pull/242)

**CPython #160714 — OPEN**  
`kqueue` interruption-handling proposal and regression test. · [View open proposal ↗](https://github.com/python/cpython/pull/160714)

<sub>Merged contributions and open proposals are intentionally distinguished.</sub>

## LIVE GITHUB COMMAND CENTER

<div align="center">

<a href="https://github.com/vankudothuadhinaik"><img width="49%" src="https://github-readme-stats.vercel.app/api?username=vankudothuadhinaik&show_icons=true&hide_border=true&rank_icon=github&bg_color=101923&title_color=EF8557&icon_color=D4F06A&text_color=F6F0E6" alt="GitHub profile statistics panel"/></a>
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

### BUILD WITH INTENT. VERIFY THE EDGE CASES.

**Backend engineering · Systems programming · Developer tools · Open source**

[EMAIL ME ↗](mailto:22je1052@iitism.ac.in) &nbsp; · &nbsp; [GITHUB ↗](https://github.com/vankudothuadhinaik)

</div>
