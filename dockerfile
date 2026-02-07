FROM apache/airflow:2.8.1-python3.11

USER root

# Copy requirements
COPY requirements.txt /requirements.txt

# Switch back to airflow user BEFORE installing packages
USER airflow

RUN pip install --no-cache-dir -r /requirements.txt
