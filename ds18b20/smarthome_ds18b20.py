from app.ds18b20 import DS18B20
import config
import json
from threading import Thread
from w1thermsensor import W1ThermSensor


def main():
    print("> initializing PiFluxTemp ...")
    print("> loading config file ...")

    print("< loaded config file!")
    print("> establishing connection to influx ...")

    print("< PiFluxTemp finished initializing!")
    print("> starting main threads ...")

    # Pools all the threads together for easier thread management
    Thread(name="ds18b20 main", target=ds18b20, args=()).start()


def ds18b20():
    threads = []

    for sensor in W1ThermSensor.get_available_sensors():
        for entry in config.sensors:
            if entry["id"] == sensor.id:
                threads.append(Thread(name=entry["name"], target=DS18B20, args=(sensor, entry["name"])))

    print("starting ds18b20 threads ...")

    for thread in threads:
        thread.start()
        print("< {}".format(thread))


if __name__ == "__main__":
        main()
