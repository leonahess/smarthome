from flask import Flask
from influxdb import InfluxDBClient

app = Flask(__name__)
influx = InfluxDBClient(host="192.168.66.56", port=8086, database='smarthome')

sensors = [
    {
      "id": "01131657bc73",
      "name": "front_window_outside"
    },
    {
      "id": "011830cd8dff",
      "name": "front_window_inside"
    },
    {
      "id": "0113170ac3ed",
      "name": "front_third"
    }
]

from app import routes
