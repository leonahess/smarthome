import datetime
import Adafruit_DHT
import time
import statistics
from app.performance import Performance
from app import client


class DHT22:

    def __init__(self, pin, name):
        self.perf = Performance()

        self.AM2302 = Adafruit_DHT.AM2302

        self.pin = pin
        self.name = name

        self.values = []
        self.filtered_temperature = []
        self.filtered_humidity = []

        while True:
            self.perf.cycle_start()
            self.get_temperature()
            self.perf.cycle_end()

            self.perf.calc_cycle_time()

            self.write_to_database()
            time.sleep(3)

    def get_temperature(self):

        try:
            self.humidity, self.temp = Adafruit_DHT.read_retry(self.AM2302, self.pin)
        except Exception as e:
            print(e)

        if self.humidity is not None and self.temp is not None:
            if 0 <= self.humidity < 100 and -30 < self.temp < 100:
            # print("dht read success, temp: {}, hum: {}".format(self.temp, self.humidity))
               self.write = True
            self.values.append({"temp": self.temp, "hum": self.humidity})
            # print(self.values)

            if len(self.values) > 10:
                self.values.pop(0)
                print("popped values")

            x = self.eliminate_noise([x["temp"] for x in self.values])
            y = self.eliminate_noise([x["hum"] for x in self.values])

            # print(y, x)

            self.filtered_temperature.append(statistics.mean(x))
            self.filtered_humidity.append(statistics.mean(y))
            print(self.filtered_humidity, self.filtered_temperature)

        else:
            print("dht read failed")
            self.write = False

    def eliminate_noise(self, values, std_factor=2):
        mean = statistics.mean(values)
        if len(values) > 1:
            standard_deviation = statistics.stdev(values)
        else:
            standard_deviation = 1

        if standard_deviation == 0:
            return values

        final_values = [element for element in values if element > mean - std_factor * standard_deviation]
        final_values = [element for element in final_values if element < mean + std_factor * standard_deviation]

        return final_values

    def assemble_json(self):

        utcnow = datetime.datetime.utcnow()

        json = [{
            "measurement": "temperature",
            "tags": {
                "name": self.name
            },
            "fields":
                {
                    "temperature": round(self.filtered_temperature.pop(), 3),
                    "cycle_time": self.perf.cycle_time
                },
            "time": utcnow,
            "time_precision": "s"
        },
        {
            "measurement": "humidity",
            "tags": {
                "name": self.name
            },
            "fields":
                {
                    "humidity": round(self.filtered_humidity.pop(), 3),
                    "cycle_time": self.perf.cycle_time
                },
            "time": utcnow,
            "time_precision": "s"
        }]

        return json

    def write_to_database(self):
        if self.write is True:
            json = self.assemble_json()

            try:
                client.write_points(json, protocol="json")
            except Exception as e:
                print(e)
