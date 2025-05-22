
---

# 🌐 IoT Sensor Monitoring System

A simple, production-grade API built with **FastAPI**, **InfluxDB**, **Docker**, and **Docker Compose** for simulating and storing time-series sensor data. Perfect for learning how to build scalable backends for IoT and telemetry use cases.

---

## 🚀 Features

- 📥 **/ingest** endpoint to receive simulated sensor data (e.g., temperature, humidity)
- 📊 **/metrics** endpoint to retrieve historical metrics by device and time range
- 🗃️ Time-series data stored in **InfluxDB**, optimized for queries
- 📊 Real-time data visualization and dashboards with **Grafana**
- 🐳 Dockerized and published to Docker Hub using GitHub Actions
- 🔁 CI/CD workflow for automatic Docker image build and push
- 📦 One-command setup using **Docker Compose**

---

## 📦 Tech Stack

| Tech           | Description                        |
|----------------|------------------------------------|
| FastAPI        | High-performance async API backend |
| InfluxDB       | Time-series database               |
| Grafana        | Visualization and dashboard tool   |
| Docker         | Containerization                   |
| Docker Compose | Multi-container orchestration      |
| GitHub Actions | CI/CD automation for Docker builds |

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

* `device_id`: e.g., `sensor_001`
* `start`: ISO timestamp (e.g., `2025-05-20T00:00:00Z`)
* `end`: ISO timestamp (e.g., `2025-05-20T23:59:59Z`)

Example:

```http
GET /metrics?device_id=sensor_001&start=2025-05-20T00:00:00Z&end=2025-05-20T23:59:59Z
```

---

## 📈 Grafana Visualization

* Grafana is preconfigured as part of the Docker Compose stack and accessible at:

  ```
  http://localhost:3000
  ```

  ```

* **InfluxDB** is added as a data source in Grafana using:

  * URL: `http://influxdb:8086`
  * Organization: your InfluxDB org (e.g., `iotorg`)
  * Bucket: `iotbucket`
  * Token: The admin token set in the `.env` or Docker Compose file (e.g., `my-token`)

* Pre-built dashboards visualize your IoT sensor data with panels for:

  * Temperature trends over time
  * Humidity changes
  * Pressure variations (if applicable)

* Use the following Flux query in Grafana panels to fetch sensor data:

  ```flux
  from(bucket: "iotbucket")
    |> range(start: -50m)
    |> filter(fn: (r) => r._measurement == "iot_data")
    |> filter(fn: (r) => r.device_id == "sensor_001")
  ```

* Customize and add more dashboards to monitor multiple sensors or metrics in real-time.

---

## 🔄 CI/CD with GitHub Actions

This project includes a GitHub Actions workflow to automatically build and push Docker images to Docker Hub when you push to the `main` branch.

* **Workflow Triggers:**

  * Push to `main` branch
  * Pull request targeting `main` branch

### Secrets Required

Add the following secrets to your GitHub repository under:

```
Settings > Secrets and variables > Actions
```

| Secret Name       | Description                    |
| ----------------- | ------------------------------ |
| `DOCKER_USERNAME` | Your Docker Hub username       |
| `DOCKER_PASSWORD` | Your Docker Hub password/token |

### GitHub Actions Workflow Summary

* Checks out source code
* Sets up Docker Buildx
* Logs in to Docker Hub
* Builds and pushes Docker image
* Tags image as `latest`


---

## 🚀 Getting Started

1. Clone the repo
2. Create `.env` with InfluxDB credentials and tokens
3. Run `docker-compose up --build`
4. Start the sensor simulation script to send data to the API
5. Access Grafana dashboard at `http://localhost:3000` to monitor live data
6. Push code to GitHub `main` branch to trigger Docker Hub build

---

## 📝 Notes

* Ensure InfluxDB tokens and bucket names in your FastAPI app and Grafana match exactly.
* Grafana dashboards can be exported/imported as JSON for reuse or sharing.
* Use the `/metrics` endpoint for RESTful access to historical data if visualization isn't needed.
* The GitHub Actions workflow handles Docker image delivery to Docker Hub, making deployment seamless.

---

