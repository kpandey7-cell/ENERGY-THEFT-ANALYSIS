from influxdb_client import InfluxDBClient

client = InfluxDBClient(
    url="http://localhost:8087",
    token="energy-dev-token",
    org="energy-analytics"
)

query = '''
from(bucket: "energy")
    |> range(start: -30m)
    |> filter(fn: (r) => r._measurement == "electricity_consumption")
    |> filter(fn: (r) => r._field == "power_kw")
    |> group(columns: ["meter_id"])
    |> count()
'''

tables = client.query_api().query(query)

print("\nREADINGS PER METER\n")

for table in tables:
    for record in table.records:
        print(
            f"Meter: {record.values.get('meter_id')} | "
            f"Readings: {record.get_value()}"
        )

client.close()