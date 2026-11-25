# Architecture Document

## Overview
The Energy Theft and Abnormal Consumption Analytics platform is an end-to-end IoT system designed to ingest, process, and analyze smart meter data to detect anomalous consumption patterns. 

## Components

### 1. Virtual Smart-Meter Simulator
- **Purpose**: Generates realistic electricity consumption data representing normal, commercial, industrial, and abnormal behaviors (e.g., spikes, drops, theft).
- **Implementation**: Python script/service that runs multiple independent meter simulations and publishes data to the MQTT broker.

### 2. MQTT Broker
- **Purpose**: Acts as the central message bus for all incoming IoT data.
- **Implementation**: Eclipse Mosquitto or EMQX (Dockerized). Handles publisher/subscriber connections and message routing.

### 3. MQTT Ingestion Service
- **Purpose**: Consumes data from the MQTT broker, validates JSON payloads, and persists readings to the database.
- **Implementation**: Python-based worker service subscribing to meter topics. Includes retry mechanisms and graceful shutdown. Optimized for bulk writes to handle high-frequency data.

### 4. InfluxDB Time-Series Database
- **Purpose**: Highly performant, persistent storage optimized for high-frequency meter time-series data and anomaly records.
- **Implementation**: Dockerized InfluxDB OSS 2.x (do not migrate to InfluxDB 3.x). Data is organized into Organization and Buckets, using Measurements, Tags (e.g., `meter_id`, `meter_type`), and Fields (e.g., `energy_kwh`, `power_kw`) to efficiently query historical data and conduct anomaly analysis.

### 5. Anomaly Detection Engine
- **Purpose**: Identifies abnormal consumption patterns.
- **Implementation**: Initially utilizes statistical methods (Rolling Mean, Rolling Standard Deviation, Z-Score) applied to Flux query results. Architected as a modular Python service, allowing easy plug-and-play of advanced Machine Learning models (Isolation Forest, LOF) in the future. Writes anomaly events back to InfluxDB OSS 2.x.

### 6. REST API
- **Purpose**: Exposes backend data for clients and dashboards.
- **Implementation**: Python web framework (e.g., FastAPI or Flask) providing endpoints for meters, readings, anomalies, and statistics, abstracting InfluxDB queries using Flux and the Python InfluxDB client.

### 7. Grafana
- **Purpose**: Data visualization and dashboarding.
- **Implementation**: Native integration with InfluxDB using the Grafana InfluxDB data source with Flux to execute complex time-series queries. Displays real-time power usage, active meters, and historical anomaly overlays.

### 8. Docker
- **Purpose**: Containerization of all services (Simulator, Broker, Ingestion, API, Anomaly Detection, InfluxDB, Grafana) via Docker Compose for easy deployment and isolation.

### 9. Logging
- **Strategy**: Structured JSON logging across all Python services for consistent tracking of events, errors, and system state.

### 10. Error Handling
- **Strategy**: Implement robust connection retries for MQTT and InfluxDB, dead-letter queues for malformed payloads, and clear, descriptive error logs.

### 11. Configuration
- **Strategy**: 12-factor app methodology using environment variables (`.env` files) to manage secrets, InfluxDB API tokens, URIs, and broker addresses. No hardcoded credentials.

### 12. Testing
- **Strategy**: Automated testing suite encompassing unit tests, integration tests, and component-specific tests (MQTT, InfluxDB, API).
