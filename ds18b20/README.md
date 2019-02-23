# DS18B20 submodule

## Requirements

#### Required Python modules

````
influxdb
w1thermsensor
````

To install them run ``sudo pip3 install -r requirements.txt``

If you don't have pip installed install it with ``sudo apt-get install python3-pip``

## Getting started

Connect all your DS18B20s to the GPIO port ``4``.
Also don't forget to enable the 1wire bus:
````
sudo raspi-config
````

#### Edit the config.py

For the DS18B20 sensors add their unique id in the "id" field and add 
name of your choosing.

If you don't know the unique IDs of your DS18B20s you can run ``python3 get_ds18b20_ids.py``
which will print them out for you.

``influx_ip = "192.168.66.56"`` sets the IP of your InfluxDB Server or localhost if you run it on your RPi

``influx_port = "8086"`` sets the port of the InfluxDB Server, default is ``8086``.

``influx_database = "smarthome"`` sets the database name, default is ``smarthome``.

#### Set Precision of the sensors

The ds18b20 sensors can run on different precisions. In the ``scripts`` directory edit the ``set_precision.py``
and run it once to write to the memory of the sensor. (The Memory of the sensor can only be written about 50k times
so be careful with writing to its memory)

````
Mode	 |   Resolution	|   Conversion time
-------------------------------------------
9 bits	 |   0.5°C	|   93.75 ms
10 bits	 |   0.25°C	|   187.5 ms
11 bits	 |   0.125°C    |   375 ms
12 bits	 |   0.0625°C   |   750 ms
````

#### Run the script

````
python3 smarthome_ds18b20.py
````


#### Autorun the Script on system startup

##### Docker

````
docker build -t conatiner_name .
docker run --net=host --restart always -d --privileged -e "TZ=Europe/Berlin" container_name
````

##### systemd

I supply a default unit file. For it to work you have to clone this repo into home directory of the user pirate 
(``/home/pirate/``).
If you want to store the script in another location you just have to change the path to the 
``smarthome_ds18b20.service``.

Copy the unit file ``smarthome_ds18b20.service`` to the correct directory:

````sudo cp smarthome_ds18b20.service /lib/systemd/system/````

Then set the right permissions on that file:

````sudo chmod 644 /lib/systemd/system/smarthome_ds18b20.service````

Then enable the service:
````
sudo systemctl daemon-reload
sudo systemctl enable smarthome_ds18b20.service
````

The script should now autostart on system startup.
It should also try to restart if it crashes.

you can start the script without rebooting with:

````
sudo systemctl start smarthome_ds18b20.service
````

If you want to check the status of the script:

``sudo systemctl status smarthome_ds18b20.service``
