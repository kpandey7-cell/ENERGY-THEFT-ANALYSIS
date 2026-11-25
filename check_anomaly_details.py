from influxdb_client import InfluxDBClient

client = InfluxDBClient(
    url="http://localhost:8087",
    token="energy-dev-token",
    org="energy-analytics",
)

query = '''
from(bucket: "energy")
  |> range(start: -6h)
  |> filter(fn: (r) => r._measurement == "anomaly_events")
  |> filter(fn: (r) => r._field == "anomaly_score")
  |> keep(columns: ["_time", "_value", "meter_id"])
  |> sort(columns: ["_time"])
'''

tables = client.query_api().query(query)

print()
print("TIME | METER | ANOMALY SCORE")
print("-" * 70)

for table in tables:
    for record in table.records:
        print(
            record.get_time(),
            "|",
            record.values.get("meter_id"),
            "|",
            record.get_value(),
        )

client.close()
