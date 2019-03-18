from flask import Flask
from influxdb import InfluxDBClient

app = Flask(__name__)
influx = InfluxDBClient(host="192.168.66.133", port=8086, database='smarthome')

sensors = [
    {
        "temp": True,
        "hum": False,
        "id": "01131657bc73",
        "name": "front_window_outside",
        "nickname": "Draußen vorne"
    },
    {
        "temp": True,
        "hum": False,
        "id": "011830cd8dff",
        "name": "front_window_inside",
        "nickname": "Fensterbrett vorne"
    },
    {
        "temp": True,
        "hum": False,
        "id": "0113170ac3ed",
        "name": "front_radiator",
        "nickname": "Heizung vorne"
    },
    {
        "temp": True,
        "hum": True,
        "name": "window_front",
        "nickname": "Fensterbrett vorne"
    },
    {
        "temp": True,
        "hum": False,
        "id": "021830b173ff",
        "name": "back_window_inside",
        "nickname": "Fensterbrett hinten"
    },
    {
        "temp": True,
        "hum": False,
        "id": "011316f4161f",
        "name": "back_radiator",
        "nickname": "Heizung hinten"
    },
    {
        "temp": True,
        "hum": False,
        "id": "011316e9c41b",
        "name": "back_window_outside",
        "nickname": "Draußen hinten"
    },
    {
        "temp": True,
        "hum": True,
        "name": "window_back",
        "nickname": "Fensterbrett hinten"
    }
]

from app import routes
