Why Kafka?
Decouples producer and consumer.
Supports scalability.
Allows asynchronous processing.

---

Why Delta MERGE?
Avoid duplicate records.

Support incremental loading.

Maintain latest order state.

---


Why Window Function?
Latest event wins.

Supports event-based processing.

---


Why Manual Databricks Execution?
Databricks Community Edition limitations.

Future enhancement:
Databricks Jobs API.

---

I evaluated multiple integration options. Because Databricks Community Edition doesn't support the same orchestration capabilities as a full workspace, I documented a manual handoff in Version 1.0 and designed the project so it can later be upgraded to Databricks Jobs without changing the downstream pipeline.


---


