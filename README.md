
---

# 🌐 IoT Sensor Monitoring System

A simple, production-grade API built with **FastAPI**, **InfluxDB**, **Docker**, and **Docker Compose** for simulating and storing time-series sensor data. Perfect for learning how to build scalable backends for IoT and telemetry use cases.

---

## 🚀 Features

- 📥 **/ingest** endpoint to receive simulated sensor data (e.g., temperature, humidity)
- 📊 **/metrics** endpoint to retrieve historical metrics by device and time range
- 🗃️ Time-series data stored in **InfluxDB**, optimized for queries
- 📦 Dockerized with one-command setup using **Docker Compose**

---

## 📦 Tech Stack

| Tech         | Description                        |
|--------------|------------------------------------|
| FastAPI      | High-performance async API backend |
| InfluxDB     | Time-series database               |
| Docker       | Containerization                   |
| Docker Compose | Multi-container orchestration    |

---

## 🛠️ Endpoints

### ✅ POST `/ingest`
Ingest simulated sensor data.

```json
{
  "device_id": "sensor_001",
  "temperature": 26.5,
  "humidity": 60.0,
  "timestamp": "2025-05-20T10:30:00Z"
}
````

### 🔍 GET `/metrics`

Query sensor metrics.

**Query Params:**

* `device_id`: `sensor_001`
* `start`: ISO timestamp
* `end`: ISO timestamp

Example:

```http
GET /metrics?device_id=sensor_001&start=2025-05-20T00:00:00Z&end=2025-05-20T23:59:59Z
```

---





