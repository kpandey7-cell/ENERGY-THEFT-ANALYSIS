# Testing Strategy

To ensure reliability and data integrity, the project implements a multi-level testing strategy using `pytest`.

## 1. Unit Tests
- **Scope**: Individual functions, classes, and algorithms.
- **Focus Areas**:
  - JSON payload validation logic.
  - Data transformation into InfluxDB Line Protocol or Dictionary structures.
  - Anomaly detection algorithms (e.g., verifying Z-score calculations with static mock arrays).
  - API endpoint route handlers using mock dependencies.

## 2. Integration Tests
- **Scope**: Interaction between multiple internal components or with external services.
- **Focus Areas**:
  - API tests using a mock Python InfluxDB client or a Dockerized test bucket.
  - Database repository tests verifying actual InfluxDB OSS 2.x batch writes and Flux queries.
  - Simulator generating a payload and verifying the MQTT client invokes the publish method correctly.

## 3. MQTT Tests
- **Scope**: Messaging layer reliability.
- **Focus Areas**:
  - End-to-end publish/subscribe flow using a local or test broker instance.
  - Verifying the ingestion service properly handles disconnects.
  - Verifying the ingestion service discards malformed payloads.

## 4. End-to-End (E2E) Tests
- **Scope**: The entire system running together.
- **Focus Areas**:
  - Spinning up Simulator, Broker, Ingestion Service, InfluxDB, and API via Docker Compose.
  - Validating that simulated readings flow all the way to InfluxDB, are readable via the API `/readings` endpoint, and that simulated anomalies trigger entries in the `anomaly_events` measurement.

## 5. Automation
- Tests will be configured to run automatically using a local script (e.g., `make test`) and can be integrated into a CI/CD pipeline (e.g., GitHub Actions).
