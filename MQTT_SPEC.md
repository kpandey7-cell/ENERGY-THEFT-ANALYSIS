# MQTT Specification

## Broker Details
- **Protocol**: MQTT v3.1.1 or v5.0
- **Security**: Optional TLS for production, plain TCP (port 1883) for local development.
- **QoS Level**: QoS 1 (At least once) recommended for telemetry readings to prevent data loss.

## Topic Structure

All meter readings are published to a hierarchical topic structure organized by meter ID.

**Topic Template**: 
`meters/{meter_id}/telemetry`

- `{meter_id}`: The UUID of the meter.

## Payload Schema

The payload must be a valid JSON object. It has been designed to easily map directly to InfluxDB Tags and Fields.

### Example Payload
```json
{
  "meter_id": "123e4567-e89b-12d3-a456-426614174000",
  "timestamp": "2026-09-30T10:00:00Z",
  "tags": {
    "meter_type": "industrial",
    "zone": "north-substation"
  },
  "fields": {
    "power_kw": 45.2,
    "energy_kwh": 1205.5,
    "voltage": 230.1,
    "current": 196.4,
    "power_factor": 0.95
  }
}
```

### Properties
- `meter_id` (string): Must match the `{meter_id}` in the topic and be a valid UUID. Will be stored as an InfluxDB tag.
- `timestamp` (string): ISO 8601 formatted datetime in UTC representing when the reading was taken.
- `tags` (object): Metadata properties for grouping and filtering.
  - `meter_type` (string): e.g., 'residential', 'commercial', 'industrial'.
  - `zone` (string): Geographical or logical location.
- `fields` (object): The actual metrics being measured.
  - `power_kw` (float): Instantaneous real power.
  - `energy_kwh` (float): Cumulative or interval energy.
  - `voltage` (float): Measured supply voltage.
  - `current` (float): Amperage draw.
  - `power_factor` (float): Efficiency metric.

## Error Handling & Resiliency
- Publishers (Simulator) must implement automatic reconnection logic if the broker connection is lost.
- Consumers (Ingestion Service) must acknowledge messages only after successfully batch-writing them to InfluxDB.
- Invalid JSON or missing required fields should be logged as warnings, and the message should be discarded or routed to a dead-letter topic.
