import datetime
import time
from src.performance import Performance


class DS18B20:

    def __init__(self, sensor, name, influx):
        self.perf = Performance()

        self.sensor = sensor
        self.influx = influx
        self.name = name
        while True:
            self.perf.cycle_start()
            self.get_temperature()
            self.perf.cycle_end()

            self.perf.calc_cycle_time()

            self.write_to_database()

            time.sleep(3)

    def get_temperature(self):
        try:
            self.temp = self.sensor.get_temperature()
        except Exception as e:
            print("Exception occured while reading the sensor {}, "
                  "it might got physically disconnected! Try to reconnect it.".format(self.name))
            print(e)

        self.id = self.sensor.id

        #print("ID: {}, temp: {}".format(self.id, self.temp))

    def assemble_json(self):
        json = [{
            "measurement": self.name,
            "tags": {
                "id": self.id
            },
            "fields":
                {
                    "temperature": self.temp,
                    "cycle_time": self.perf.cycle_time
                },
            "time": datetime.datetime.now(),
            "time_precision": "s"
          }]
        #print(datetime.datetime.now())

        return json

    def write_to_database(self):
        json = self.assemble_json()

        try:
            self.influx.client.write_points(json, protocol="json")
        except Exception as e:
            print(e)
