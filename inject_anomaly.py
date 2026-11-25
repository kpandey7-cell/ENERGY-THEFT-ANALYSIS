import json
from datetime import datetime, timezone

import paho.mqtt.client as mqtt


BROKER = "localhost"
PORT = 1884

meter_id = "REFIT_HOUSE_1"

payload = {
    "meter_id": meter_id,
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "power_kw": 10.0,
    "meter_type": "residential",
    "zone": "refit",
}

topic = f"energy/meters/{meter_id}/reading"

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="anomaly_test_injector",
)

print("Connecting to MQTT...")
client.connect(BROKER, PORT, 60)

client.loop_start()

message = json.dumps(payload)

result = client.publish(
    topic,
    message,
    qos=1,
)

result.wait_for_publish()

print("Published abnormal reading:")
print(message)

client.loop_stop()
client.disconnect()