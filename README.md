# 🚀 Real-Time eCommerce Data Platform

> An end-to-end Real-Time Data Engineering project that simulates an eCommerce order processing platform using Apache Kafka, Apache Airflow, PySpark, Delta Lake, and Databricks. The project follows the Medallion Architecture (Bronze → Silver → Gold) to ingest, validate, transform, and analyze streaming order data.

---

## 📌 Project Overview

Modern eCommerce platforms generate thousands of customer orders every second. Processing this continuously arriving data requires a scalable, reliable, and fault-tolerant data pipeline.

This project demonstrates how a modern Lakehouse-based Data Engineering platform can be built using industry-standard tools.

The pipeline:

- Generates real-time order events
- Streams events through Apache Kafka
- Orchestrates ingestion using Apache Airflow
- Stores landing data as JSON
- Processes data using PySpark and Delta Lake
- Implements Medallion Architecture
- Performs data validation and deduplication
- Supports incremental loading using Delta MERGE
- Produces business-ready Gold layer analytics

---

# 🎯 Business Problem

An eCommerce company continuously receives customer orders throughout the day.

The business requires a scalable platform capable of:

- Processing streaming order events
- Decoupling producers and consumers
- Validating incoming data
- Removing duplicate events
- Supporting incremental processing
- Tracking pipeline execution metrics
- Producing business-ready analytical datasets

Traditional batch ETL pipelines are not suitable for continuously arriving events.

This project demonstrates an event-driven Lakehouse architecture that solves these challenges.

---

# 🏗️ Solution Architecture

The implemented solution follows an event-driven architecture.

```
                    Airflow
                        │
                        ▼
        Generate Orders (Producer)
                        │
                        ▼
                 Apache Kafka
                        │
                        ▼
        Consume Orders (Consumer)
                        │
                        ▼
             Landing JSON Files
                        │
         (Databricks Community Edition)
                        ▼
                Bronze Layer
                        │
                        ▼
                Silver Layer
                        │
          Validation & Deduplication
                        │
                Delta MERGE
                        │
                        ▼
                 Pipeline Metrics
                        │
                        ▼
                  Gold Layer
```

---

# 🥉 Medallion Architecture

## Bronze Layer

Purpose:

- Store raw incoming data
- Preserve original records
- Support auditing
- Enable replay

Operations:

- Read landing JSON files
- Load into Delta Table

---

## Silver Layer

Purpose:

- Clean data
- Validate records
- Remove duplicates
- Prepare analytics-ready dataset

Implemented Features:

- Data validation
- Window Function
- Latest record selection
- Processed timestamp
- Delta MERGE

---

## Gold Layer

Purpose:

Provide business-ready KPIs.

Generated Metrics:

- Total Orders
- Total Revenue
- Average Order Value
- Maximum Order Value
- Minimum Order Value

---

# ⚙️ Technology Stack

| Category | Technology |
|------------|------------|
| Language | Python |
| Streaming | Apache Kafka |
| Workflow Orchestration | Apache Airflow |
| Data Processing | Apache Spark (PySpark) |
| Storage | Delta Lake |
| Platform | Databricks Community Edition |
| Containerization | Docker & Docker Compose |
| Data Format | JSON / JSONL |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
real-time-ecommerce-data-platform/

│
├── airflow/
│   ├── dags/
│   └── docker-compose.yml
│
├── producer/
│   └── generate_orders.py
│
├── consumer/
│   └── consumer.py
│
├── databricks/
│   ├── 01_bronze_ingestion
│   ├── 02_silver_processing
│   ├── 03_merge
│   ├── 04_pipeline_metrics
│   └── 05_gold_summary
│
├── landing/
│   └── orders.json
│
├── docs/
│
├── docker-compose.yml
│
├── requirements.txt
│
└── README.md
```

---

# 🔄 End-to-End Data Flow

```
Order Generator
      │
      ▼
Apache Kafka
      │
      ▼
Consumer
      │
      ▼
Landing JSON
      │
      ▼
Bronze
      │
      ▼
Silver
      │
      ▼
Delta MERGE
      │
      ▼
Gold
```

---

# ✅ Features

- Real-time order generation
- Apache Kafka streaming
- Apache Airflow orchestration
- Dockerized local environment
- Landing layer implementation
- Medallion Architecture
- Bronze → Silver → Gold pipeline
- Data validation
- Window Function based deduplication
- Incremental loading using Delta MERGE
- Pipeline execution metrics
- Business KPI generation
- Modular project structure

---

# 📊 Pipeline Metrics

The pipeline tracks execution statistics including:

- Bronze record count
- Silver record count
- Rejected records
- Pipeline execution timestamp

Example:

| Bronze | Silver | Rejected |
|---------|---------|-----------|
| 5 | 3 | 2 |

---

# 📈 Gold Layer Output

Example Business KPIs

| Metric | Value |
|----------|---------|
| Total Orders | 3 |
| Total Revenue | 2250 |
| Average Order Value | 750 |
| Maximum Order Value | 900 |
| Minimum Order Value | 600 |

---

# 🛠️ Engineering Decisions

| Decision | Reason |
|------------|--------|
| Apache Kafka | Decouples producers and consumers for scalable event processing |
| Apache Airflow | Orchestrates producer and consumer workflow |
| Medallion Architecture | Separates raw, validated and business-ready datasets |
| Delta MERGE | Supports incremental loading without full refresh |
| Window Functions | Keeps latest version of duplicate orders |
| Pipeline Metrics | Enables monitoring and operational visibility |
| Docker | Provides reproducible local development environment |
| Databricks Community Edition | Free Spark environment suitable for learning and prototyping |

---

# ⚠️ Challenges Encountered

During development several real-world engineering challenges were encountered.

- Spark installation issues on Windows
- Docker networking between Kafka and Airflow
- Kafka advertised listener configuration
- Airflow dependency management
- Databricks Community Edition limitations
- Incremental merge implementation
- Data validation strategy
- Duplicate event handling

These challenges were resolved through iterative debugging and architectural improvements.

---

# 🚀 Future Improvements

Future enhancements include:

- Databricks Job API integration
- Cloud deployment (AWS / Azure / GCP)
- CI/CD pipeline
- Schema Registry
- Kafka Connect
- Data Quality framework
- Monitoring dashboard
- Kubernetes deployment

---

# ▶️ How to Run

### 1. Start Kafka

```bash
docker compose up -d
```

### 2. Start Airflow

```bash
cd airflow

docker compose up -d
```

### 3. Trigger Airflow DAG

Run

```
first_pipeline
```

The DAG will:

- Generate orders
- Publish events to Kafka
- Consume events
- Store landing JSON

### 4. Execute Databricks notebooks

Run notebooks in the following order:

1. Bronze Ingestion
2. Silver Processing
3. Delta MERGE
4. Pipeline Metrics
5. Gold Layer

---

# 📸 Screenshots


- Airflow DAG: ![Airflow](docs/screenshots/instance.png)
- Successful Airflow Run
- Kafka Producer: ![Airflow](docs/screenshots/producer.png)
- Kafka Consumer: ![Airflow](docs/screenshots/consumer.png)
- Bronze Table
- Silver Table
- Gold Table
- Pipeline Metrics
- Architecture Diagram: ![Architecture](docs/architecture.png)

---

# 🎓 Key Learnings

This project helped me gain hands-on experience with:

- Event-driven architectures
- Apache Kafka
- Apache Airflow
- Docker
- PySpark
- Delta Lake
- Medallion Architecture
- Incremental processing
- Window Functions
- Data validation
- Pipeline monitoring
- End-to-end Data Engineering workflows

---

# 👨‍💻 Author

**Prakalp Pande**

- GitHub: https://github.com/PRAKALP-PANDE
- LinkedIn: *(Add your LinkedIn URL here)*

---

## ⭐ If you found this project helpful, consider giving it a star!