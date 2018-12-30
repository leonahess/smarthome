from src.influx import Influx
from src.ds18B20 import DS18B20
from src.dht22 import DHT22

import json
from threading import Thread
from w1thermsensor import W1ThermSensor


def main():
    print("> initializing PiFluxTemp ...")
    print("> loading config file ...")

    # Loads the config file and converts it to and python object with the json decoder
    json_data = open("config.json").read()
    config = json.loads(json_data)

    print("< loaded config file!")
    print("> establishing connection to influx ...")

    # Creates and Influx Object, which connects to the database so that the threads can write to the database
    influx = Influx(config)

    print("< PiFluxTemp finished initializing!")
    print("> starting main threads ...")

    # Pools all the threads together for easier thread management
    threads = []
    threads.append(Thread(name="ds18b20 main", target=ds18b20, args=(influx, config, )))
    threads.append(Thread(name="dht22 main", target=dht22, args=(influx, config, )))

    for entry in threads:
        entry.start()
        print("< {}".format(entry))


def ds18b20(influx, config):
    threads = []

    for sensor in W1ThermSensor.get_available_sensors():
        for entry in config["ds18b20"]:
            if entry["id"] == sensor.id:
                threads.append(Thread(name=entry["name"], target=DS18B20, args=(sensor, entry["name"], influx)))

    print("starting ds18b20 threads ...")

    for thread in threads:
        thread.start()
        print("< {}".format(thread))


def dht22(influx, config):
    threads = []

    for entry in config["dht22"]:
        threads.append(Thread(name=entry["name"], target=DHT22, args=(entry["pin"], entry["name"], influx)))

    print("> starting dht22 threads ...")

    for thread in threads:
        thread.start()
        print("< {}".format(thread))


if __name__ == "__main__":
        main()
