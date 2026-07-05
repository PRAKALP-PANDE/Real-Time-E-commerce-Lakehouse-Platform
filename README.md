## Project Progress

- [x] Bronze Ingestion
- [x] Silver Validation
- [x] Window-based Deduplication
- [x] Incremental Processing with Delta MERGE
- [ ] Data Quality Metrics
- [ ] Gold Layer
- [ ] Streaming Pipeline
- [ ] Airflow Orchestration

---

## Architecture

                ┌─────────────┐
                │ Order Events│
                └──────┬──────┘
                       │
                ┌──────▼──────┐
                │   Kafka     │
                └──────┬──────┘
                       │
          ┌────────────▼────────────┐
          │ Spark Structured Stream │
          └────────────┬────────────┘
                       │
          ┌────────────▼────────────┐
          │ Delta Lake Bronze Layer │
          └────────────┬────────────┘
                       │
          ┌────────────▼────────────┐
          │ Delta Lake Silver Layer │
          └────────────┬────────────┘
                       │
          ┌────────────▼────────────┐
          │ Delta Lake Gold Layer   │
          └────────────┬────────────┘
                       │
             ┌─────────▼─────────┐
             │ Analytics Tables  │
             └─────────┬─────────┘
                       │
                ┌──────▼──────┐
                │ Dashboard   │
                └─────────────┘
