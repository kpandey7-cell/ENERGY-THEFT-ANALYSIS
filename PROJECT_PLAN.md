# Project Plan

This document outlines the phased development strategy for the Energy Theft and Abnormal Consumption Analytics platform. 

The goal is to build the project incrementally, ensuring each component is fully functional, integrated, and testable before progressing to the next.

## Phase 1: Architecture and Repository Setup
- Finalize planning documents adapting to InfluxDB architecture.
- Set up the Git repository and directory structure (e.g., `simulator/`, `backend/`, `database/`).
- Initialize Python environment and configure linter/formatter tools.

## Phase 2: MQTT and Smart-Meter Simulator
- Set up a local MQTT broker (e.g., Mosquitto).
- Develop the smart-meter simulation logic to generate realistic multi-variable profiles (power, energy, voltage, current, power factor).
- Implement publishing to MQTT with appropriate topic structures.
- Write tests for simulator configurations and MQTT connectivity.

## Phase 3: InfluxDB Data Layer
- Set up a local InfluxDB OSS 2.x instance via Docker (do not migrate to 3.x).
- Configure organizations, buckets, and InfluxDB API tokens.
- Develop Python InfluxDB client utilities/repositories for writing and querying points using Flux.
- Write unit tests for InfluxDB operations.

## Phase 4: MQTT Ingestion Service
- Develop a background worker to subscribe to MQTT topics.
- Implement JSON payload parsing, validation, and error handling.
- Write telemetry records into the InfluxDB bucket in optimized batches.
- Test end-to-end data flow from simulator to time-series database.

## Phase 5: Anomaly Detection
- Implement statistical models (Rolling Mean, Std Dev, Z-Score).
- Create a service that regularly executes Flux queries against InfluxDB to analyze recent data.
- Persist detected anomalies back into the `anomaly_events` measurement in InfluxDB.
- Ensure the architecture is modular for future ML additions.

## Phase 6: REST API
- Build API endpoints for fetching meters, readings, anomalies, and aggregate statistics by wrapping InfluxDB queries.
- Implement input validation and standard JSON responses.
- Write API integration tests.

## Phase 7: Grafana Dashboards
- Deploy Grafana via Docker.
- Configure the Grafana InfluxDB data source using Flux as the primary data source.
- Build dashboards for Total Consumption, Power/Voltage trends, and Anomaly Analysis overlays.

## Phase 8: Integration Testing
- Create automated end-to-end tests covering the entire data lifecycle.
- Test failure scenarios (e.g., missing fields, disconnects).

## Phase 9: Dockerization and Deployment
- Write Dockerfiles for custom services (Simulator, Ingestion, API, Anomaly Detection).
- Create a comprehensive `docker-compose.yml` to spin up the entire stack.
- Handle environment variables properly for secrets and configurations.

## Phase 10: Documentation and Final Validation
- Update `README.md` with instructions on how to run the project.
- Validate that all major components communicate seamlessly.
- Final review against project specifications.
