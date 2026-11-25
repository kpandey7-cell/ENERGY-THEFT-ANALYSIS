import time
import paho.mqtt.client as mqtt

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    protocol=mqtt.MQTTv311,
)

print("Connecting...")
client.connect("localhost", 1883, 60)

client.loop_start()

time.sleep(2)

print("Connected:", client.is_connected())

payload = '{"test":"python"}'

result = client.publish(
    "energy/meters/TEST/reading",
    payload,
    qos=1,
)

print("Publish return code:", result.rc)

result.wait_for_publish()

print("Published:", result.is_published())

time.sleep(3)

client.loop_stop()
client.disconnect()

print("Finished.")