import subprocess
from app import client
import config
import datetime
import time


class RaspiTemp:

    def __init__(self):
        while True:
            try:
                self.write(self.read())
            except Exception as e:
                print("Current Stats Exception: {}".format(e))

            time.sleep(10)

    def read(self):
        jsons = []
        result = subprocess.run("cat /sys/class/thermal/thermal_zone0/temp", shell=True)
        temp_cpu_raw = result.stdout
        temp_cpu = float("{}.{}".format(temp_cpu_raw / 1000, (temp_cpu_raw/1000) % (temp_cpu_raw/100)))

        freq0_cpu = float(subprocess.run("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq", shell=True).stdout)
        freq1_cpu = float(subprocess.run("cat /sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq", shell=True).stdout)
        freq2_cpu = float(subprocess.run("cat /sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq", shell=True).stdout)
        freq3_cpu = float(subprocess.run("cat /sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq", shell=True).stdout)

        print(temp_cpu_raw)
        print(temp_cpu)
        print(freq0_cpu)

        jsons.append({
            "measurement": "cpu",
            "tags": {
                "host": config.hostname
            },
            "fields": {
                "temp": temp_cpu
            },
            "time": datetime.datetime.now()
        })

        jsons.append({
            "measurement": "cpu",
            "tags": {
                "host": config.hostname,
                "cpu": "cpu0"
            },
            "fields": {
                "freq": freq0_cpu
            },
            "time": datetime.datetime.now()
        })

        jsons.append({
            "measurement": "cpu",
            "tags": {
                "host": config.hostname,
                "cpu": "cpu1"
            },
            "fields": {
                "freq": freq1_cpu
            },
            "time": datetime.datetime.now()
        })

        jsons.append({
            "measurement": "cpu",
            "tags": {
                "host": config.hostname,
                "cpu": "cpu2"
            },
            "fields": {
                "freq": freq2_cpu
            },
            "time": datetime.datetime.now()
        })

        jsons.append({
            "measurement": "cpu",
            "tags": {
                "host": config.hostname,
                "cpu": "cpu3"
            },
            "fields": {
                "freq": freq3_cpu
            },
            "time": datetime.datetime.now()
        })

        return jsons

    def write(self, jsons):

        try:
            client.write_points(jsons, protocol="json")
            print("wrote to db")
        except Exception as e:
            print("Write exception: {}".format(e))



