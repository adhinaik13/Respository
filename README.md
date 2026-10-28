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

<sub>SIX PROJECTS · SYSTEMS, PAYMENTS, ANALYTICS, DATA QUALITY, ML &amp; RELIABILITY</sub>

### 01 — LOW-LATENCY MATCHING ENGINE
<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-matching-engine.svg" width="100%" alt="Custom matching engine systems dashboard showing bid book, price-time matching core and event path"/>

A C++20 limit-order-book prototype with price-time priority, full and partial fills, cancellation, order lookup, and a bounded single-producer/single-consumer event path.

**STACK** &nbsp; `C++20` &nbsp; `CMake` &nbsp; `Testing` &nbsp; `Benchmarking`

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/low-latency-matching-engine)

---

### 02 — UPI OFFLINE MESH
<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-upi-mesh.svg" width="100%" alt="Custom UPI Offline Mesh dashboard showing encrypted payload, signature verification, safe queueing and simulated reconciliation"/>

An offline-payment prototype exploring encrypted QR payloads, RSA-PSS signatures, replay protection, idempotency, and simulated store-and-forward settlement.

**STACK** &nbsp; `Java 17` &nbsp; `Spring Boot` &nbsp; `AES-GCM` &nbsp; `RSA-PSS`

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/UPI_Without_Internet)

---

### 03 — DATAPULSE ANALYTICS
<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-datapulse.svg" width="100%" alt="Custom DataPulse Analytics dashboard showing event volume illustration, FastAPI ingestion, validation and dashboard layers"/>

A full-stack event-analytics prototype combining API ingestion and aggregation, SQLAlchemy models, and a React + TypeScript dashboard. The chart in this illustration is sample artwork, not live product telemetry.

**STACK** &nbsp; `FastAPI` &nbsp; `SQLAlchemy` &nbsp; `React` &nbsp; `TypeScript`

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/DataPulse-Analytics)

### 04 — HEALTHSTREAM ETL

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-healthstream.svg" width="100%" alt="HealthStream ETL dashboard illustration showing ingestion, validation, normalization, deduplication and data-quality reporting"/>

A synthetic healthcare-event pipeline focused on data quality: validation, normalization, deduplication, and quality reporting. The illustration describes the workflow; it does not display patient data or live pipeline telemetry.

**FOCUS** &nbsp; `ETL` &nbsp; `Data validation` &nbsp; `Normalization` &nbsp; `Deduplication`

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/HealthStream-ETL)

---

### 05 — AQI PREDICTION

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/vankudothuadhinaik/main/assets/dashboard-aqi.svg" width="100%" alt="AQI prediction dashboard illustration with time-series trend, persistence baseline and station-wise evaluation workflow"/>

An air-quality prediction project exploring time-series evaluation with a chronological persistence baseline and per-station comparisons. The chart is illustrative, not a live air-quality feed.

**FOCUS** &nbsp; `Python` &nbsp; `Time series` &nbsp; `Baseline evaluation` &nbsp; `Air quality`

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/Predicting-the-AQI-of-Indian-Cities-Using-Machine-Learning)

---

<details>
<summary><strong>MORE BUILDS — DATA · ML · FRONTEND</strong></summary>

- **[TodoList Management Application](https://github.com/vankudothuadhinaik/TodoList-Management-Application)** — React task workflow with accessible actions and localStorage persistence.

[SEE ALL REPOSITORIES ↗](https://github.com/vankudothuadhinaik?tab=repositories)

</details>

### 06 — UPTIME SENTINEL

A FastAPI uptime-monitoring service for HTTP/HTTPS endpoints, with latency and failure tracking, incident lifecycle management, a read-only public status page, PostgreSQL-backed worker leases, and configurable daily cleanup of expired check history.

**STACK** &nbsp; `Python 3.12` &nbsp; `FastAPI` &nbsp; `PostgreSQL` &nbsp; `SQLAlchemy` &nbsp; `Docker Compose` &nbsp; `GitHub Actions`

**VERIFICATION** &nbsp; CI run #88 passed the standard checks and Docker Compose smoke test, including Codecov upload. The real controlled egress-proxy security integration remains skipped pending private proxy fixtures/secrets; production deployment is not yet verified.

<img src="https://raw.githubusercontent.com/vankudothuadhinaik/uptime-sentinel/integration/sentry-doppler/docs/images/architecture.svg" width="100%" alt="Uptime Sentinel architecture diagram showing API, worker, PostgreSQL and controlled egress boundary"/>

[VIEW SOURCE ↗](https://github.com/vankudothuadhinaik/uptime-sentinel) · [LATEST VERIFIED CI RUN ↗](https://github.com/vankudothuadhinaik/uptime-sentinel/actions/runs/40681979743) · [OPEN PR #4 ↗](https://github.com/vankudothuadhinaik/uptime-sentinel/pull/4) · [PROJECT README ↗](https://github.com/vankudothuadhinaik/uptime-sentinel/blob/integration/sentry-doppler/README.md) · [SECURITY TEST PLAN ↗](https://github.com/vankudothuadhinaik/uptime-sentinel/blob/integration/sentry-doppler/EGRESS_PROXY_TESTING.md)

---

## OPEN SOURCE

**CPython #160707 — MERGED**  
Free-threaded garbage-collector traversal fix and regression coverage. · [Review the contribution ↗](https://github.com/python/cpython/pull/160707)

**CPython #160703 — CLOSED · NOT MERGED**  
Monitoring callback error propagation from `for` loops, with a regression test. Tier-2 runtime coverage was not demonstrated in the available build; the proposal was closed without merge. · [View contribution ↗](https://github.com/python/cpython/pull/160703)

**chunklet-py #107 — MERGED**  
Windows multiprocessing pickling fix and regression tests. · [Review the contribution ↗](https://github.com/speedyk-005/chunklet-py/pull/107)

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
