# REST API Specification

The API exposes internal data for front-end applications, dashboards (Grafana), and potential external integrations. All endpoints return JSON and use standard HTTP status codes.

The backend acts as an abstraction layer over InfluxDB OSS 2.x, translating REST requests into complex Flux queries using the Python InfluxDB client.

## Base URL
`/api/v1`

## Endpoints

### 1. Meters
- **`GET /meters`**
  - **Description**: Returns a list of unique meters discovered from the time-series tags.
  - **Query Params**: `type`, `zone`
  - **Response**: Array of meter metadata objects (derived from InfluxDB tags).

### 2. Consumption
- **`GET /meters/{meter_id}/readings`**
  - **Description**: Returns historical consumption data (`power_kw`, `energy_kwh`, `voltage`, etc.) for a meter.
  - **Query Params**: `start_time`, `end_time`, `downsample_interval` (e.g., '1h', '5m')
  - **Response**: Time-series array of reading objects.

### 3. Anomalies
- **`GET /anomalies`**
  - **Description**: Returns a global list of recent anomaly events across all meters.
  - **Query Params**: `start_time`, `end_time`, `limit`, `min_score`, `zone`
  - **Response**: Array of anomaly event objects with scores and timestamps.

- **`GET /meters/{meter_id}/anomalies`**
  - **Description**: Returns anomaly history for a specific meter.
  - **Query Params**: `start_time`, `end_time`, `limit`
  - **Response**: Array of anomaly event objects.

### 4. Statistics
- **`GET /stats/overview`**
  - **Description**: High-level aggregated statistics powered by aggregate Flux queries.
  - **Response**:
    ```json
    {
      "active_meters_24h": 150,
      "total_energy_kwh_24h": 4500.5,
      "peak_power_kw_24h": 320.1,
      "total_anomalies_24h": 12
    }
    ```
