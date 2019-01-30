from flask import Flask
from influxdb import InfluxDBClient

app = Flask(__name__)
influx = InfluxDBClient(host="192.168.66.56", port=8086, database='smarthome')

sensors = [
    {
        "temp": True,
        "hum": False,
        "id": "01131657bc73",
        "name": "front_window_outside",
        "nickname": "Draußen"
    },
    {
        "temp": True,
        "hum": False,
        "id": "011830cd8dff",
        "name": "front_window_inside",
        "nickname": "vorderes Fensterbrett"
    },
    {
        "temp": True,
        "hum": False,
        "id": "0113170ac3ed",
        "name": "front_third",
        "nickname": "vordere Jalousie"
    },
    {
        "temp": True,
        "hum": True,
        "name": "window_front",
        "nickname": "vorderes Fensterbrett"
    }
]

from app import routes
