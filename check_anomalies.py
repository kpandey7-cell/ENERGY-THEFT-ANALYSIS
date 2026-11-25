from influxdb_client import InfluxDBClient

client = InfluxDBClient(
    url="http://localhost:8087",
    token="energy-dev-token",
    org="energy-analytics",
)

query = '''
from(bucket: "energy")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "anomaly_events")
'''

tables = client.query_api().query(query)

print("ANOMALY TABLES:", len(tables))
print("ANOMALY RECORDS:", sum(len(table.records) for table in tables))

client.close()
