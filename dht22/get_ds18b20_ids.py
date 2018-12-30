from w1thermsensor import W1ThermSensor

for sensor in W1ThermSensor.get_available_sensors():
    print(sensor.id)
