# 🚀 Real-Time eCommerce Data Engineering Pipeline

An end-to-end real-time Data Engineering project that simulates order processing for an eCommerce platform using Apache Kafka, Apache Airflow, PySpark, Delta Lake, and Databricks Community Edition. The project follows the Medallion Architecture (Bronze → Silver → Gold) to ingest, validate, transform, and analyze streaming order data.

## 📖 Overview

Modern eCommerce platforms generate thousands of customer orders every second. Processing this data reliably requires a scalable pipeline capable of ingesting streaming events, validating data quality, removing duplicates, performing incremental processing, and producing business-ready analytics.

This project demonstrates how such a pipeline can be built using modern Data Engineering tools and best practices.

The pipeline generates synthetic order events, streams them through Apache Kafka, orchestrates ingestion with Apache Airflow, processes the data in Databricks using PySpark and Delta Lake, and organizes the data using the Medallion Architecture.

The final Gold layer provides aggregated business metrics such as total revenue, order count, average order value, and pipeline execution metrics.

## ⭐ Project Highlights

- Event-driven architecture using Apache Kafka
- Workflow orchestration with Apache Airflow
- Medallion Architecture (Bronze → Silver → Gold)
- Data validation and quality checks
- Incremental processing using Delta MERGE
- Window-function based deduplication
- Pipeline execution metrics
- Gold layer business KPIs
- Dockerized local development environment
- Databricks Community Edition implementation

## 🎯 Business Problem

An eCommerce company receives customer orders continuously throughout the day.

The company needs a scalable system capable of:

- Receiving real-time order events
- Decoupling producers and consumers
- Validating incoming data
- Removing duplicate events
- Maintaining the latest version of each order
- Measuring pipeline quality
- Producing business-ready analytical datasets

Traditional batch pipelines are not suitable for handling continuously arriving events. This project demonstrates a streaming-first architecture using Apache Kafka and Delta Lake.

## 💡 Solution

The implemented solution follows a modern event-driven architecture.

1. Orders are generated using a Python-based producer.
2. Apache Kafka acts as the event streaming platform.
3. Apache Airflow orchestrates the producer and consumer tasks.
4. The consumer stores incoming events as landing JSON files.
5. Databricks ingests the landing data into the Bronze layer.
6. Silver layer performs validation, deduplication, and transformation.
7. Delta MERGE enables incremental processing.
8. Gold layer generates business KPIs for reporting and analytics.

## Section 5 — Technology Stack

| Category         | Technologies                 |
| ---------------- | ---------------------------- |
| Programming      | Python                       |
| Streaming        | Apache Kafka                 |
| Workflow         | Apache Airflow               |
| Processing       | Apache Spark (PySpark)       |
| Storage          | Delta Lake                   |
| Platform         | Databricks Community Edition |
| Containerization | Docker & Docker Compose      |
| Data Format      | JSON / JSONL                 |
| Version Control  | Git & GitHub                 |


## Section 6 — Folder Structure

real-time-ecommerce-data-platform/
│
├── airflow/
│
├── producer/
│
├── consumer/
│
├── databricks/
│   ├── 01_bronze_ingestion
│   ├── 02_silver_processing
│   ├── 03_merge
│   ├── 04_pipeline_metrics
│   └── 05_gold_summary
│
├── landing/
│
├── docs/
│
├── docker-compose.yml
│
├── requirements.txt
│
└── README.md

---

## Key Engineering Decisions

| Decision                     | Why                                                          |
| ---------------------------- | ------------------------------------------------------------ |
| Kafka                        | Decouple producer and consumer for scalable event processing |
| Airflow                      | Orchestrate ingestion tasks and workflow dependencies        |
| Delta MERGE                  | Enable incremental updates and avoid duplicate records       |
| Window Functions             | Retain the latest version of each order                      |
| Medallion Architecture       | Separate raw, validated, and business-ready datasets         |
| Databricks Community Edition | Free environment suitable for learning and prototyping       |


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
