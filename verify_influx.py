from influxdb_client import InfluxDBClient

client = InfluxDBClient(
    url="http://localhost:8087",
    token="energy-dev-token",
    org="energy-analytics",
)

query = '''
from(bucket: "energy")
  |> range(
      start: 2026-10-04T10:23:00Z,
      stop: 2026-10-04T10:28:00Z
  )
  |> filter(fn: (r) => r._measurement == "electricity_consumption")
  |> filter(fn: (r) => r._field == "power_kw")
  |> filter(fn: (r) => r.meter_id == "REFIT_HOUSE_10")
  |> sort(columns: ["_time"])
'''

tables = client.query_api().query(query)

print("\nHOUSE 10 — NEW ANOMALY WINDOW\n")

for table in tables:
    for record in table.records:
        print(
            f"{record.get_time()} | "
            f"power={record.get_value():.4f} kW"
        )

client.close()