# OpenSky Flight Data Pipeline ✈️

An end-to-end **data engineering pipeline** that ingests live flight data from the **OpenSky Network API**, processes it using an **ETL workflow**, and stores it in **PostgreSQL**, orchestrated with **Apache Airflow** and deployed using **Docker**.

This project demonstrates real-world data engineering concepts including orchestration, ETL design, SQL schema creation, and containerized pipelines.

---

## 🚀 Project Overview

The pipeline performs the following steps:

1. **Extract** real-time flight data from the OpenSky API
2. **Transform** raw JSON data into structured, clean records
3. **Load** processed data into PostgreSQL tables
4. Orchestrate the workflow using **Airflow DAGs**

---

## 🧱 Architecture

OpenSky API
↓
Extract (Python)
↓
Transform (Python)
↓
Load (PostgreSQL)
↓
Airflow DAG (Scheduling & Orchestration)


---

## 🛠 Tech Stack

- **Python**
- **Apache Airflow**
- **PostgreSQL**
- **SQL**
- **Docker & Docker Compose**
- **Git & GitHub**

---

## 📁 Project Structure

OPENSKY_PIPELINE/
│
├── dags/
│ ├── opensky_pipeline_dags.py # Airflow DAG definition
│ │
│ └── src/
│ ├── extract.py # Extract data from OpenSky API
│ ├── transform.py # Data cleaning & transformation
│ ├── load.py # Load data into PostgreSQL
│ └── main.py # ETL entry point
│
├── sql/
│ └── create_tables.sql # Database schema creation
│
├── logs/ # Airflow logs
├── scripts/ # Helper / setup scripts
│
├── docker-compose.yml # Airflow & Postgres services
├── dockerfile # Custom Airflow image
├── requirements.txt # Python dependencies
├── .env # Environment variables (not committed)
└── README.md


---

## 📥 Extract

- Fetches live flight state vectors from the OpenSky Network API
- Parses JSON response
- Handles missing or null values

**Sample fields extracted:**
- ICAO24
- Callsign
- Origin country
- Latitude / Longitude
- Altitude
- Velocity
- Timestamp

---

## 🔄 Transform

- Cleans invalid or incomplete records
- Converts timestamps to readable formats
- Prepares structured data for database insertion

Transformation logic is implemented in `transform.py`.

---

## 📤 Load

- Creates tables using SQL scripts
- Inserts transformed data into PostgreSQL
- Ensures data consistency and schema alignment

Database schema is defined in:
sql/create_tables.sql


---

## ⏱ Orchestration with Airflow

- DAG defined in `opensky_pipeline_dags.py`
- Tasks:
  - Extract
  - Transform
  - Load
- Supports scheduled or manual execution

---

## ▶️ How to Run

### 1. Clone the repository

git clone https://github.com/Robin6551/opensky_pipeline.git
cd opensky_pipeline
2. Configure environment variables

Create a .env file:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=opensky

3. Start services
docker-compose up -d

4. Access Airflow UI
http://localhost:8080


Trigger the OpenSky DAG from the Airflow dashboard.

📊 Use Cases

Real-time flight monitoring

Aviation analytics

Learning Airflow-based ETL pipelines

Data engineering portfolio project

🎯 Key Learnings

Designing ETL pipelines

Working with real-time APIs

Airflow DAG orchestration

PostgreSQL schema design

Dockerized data workflows

🔮 Future Improvements

Incremental data loading

Data quality checks

Add monitoring & alerts

Cloud deployment (AWS / GCP)

Analytics dashboard integration

👤 Author

Robin
Aspiring Data Engineer
GitHub: https://github.com/Robin6551



