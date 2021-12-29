import paho.mqtt.client as mqtt
import datetime


def on_connect(client, userdata, flags, rc):
    print("Connect rc : " + str(rc))


def on_message(client, userdata, msg):
    userdata["counter"] = int(msg.payload)
    userdata["last_time"] = datetime.datetime.now()


time_arg_d = {"counter": 0, "last_time": 0}
client = mqtt.Client(userdata=time_arg_d)
client.on_connect = on_connect
client.message_callback_add("/counter/in", on_message)
client.connect("127.0.0.1", 1883, 60)
client.subscribe("/counter/in")

run = True
while run:
    client.loop()
    if time_arg_d["counter"] != 0:
        current_time = datetime.datetime.now()
        delta = current_time - time_arg_d["last_time"]
        ms = delta.total_seconds()
        if ms >= time_arg_d["counter"]:
            client.publish("/counter/out", "Alarm!")
            time_arg_d["counter"] = 0
