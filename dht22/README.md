# PiFluxTemp

## Requirements

#### Required Python modules

````
influxdb
w1thermsensor
Adafruit_DHT
numpy
````

to install them run ``sudo pip3 install -r requirements.txt``

the ``numpy`` module might throw erros when installed via pip3. To fix this uninstall the defect version with
``sudo pip3 uninstall numpy``. Then install numpy via apt-get with ``sudo apt-get install python3-numpy``.

If you don't have pip installed install it with ``sudo apt-get install python3-pip``

#### InfluxDB

You need a Server running [InfluxDB](https://portal.influxdata.com/downloads).
This can be on your Raspberry Pi, though I recommend a Machine
with at least a couple Gigs of RAM.

## Getting started

Connect all your DS18B20s to the GPIO port ``4`` and one dht22 to a GPIO port of your choosing respectively.
Also don't forget to enable the 1wire bus.

#### Edit the config.json

For the dht22 sensors add the gpio pin which you connected it to and
add a name of your choosing.

For the DS18B20 sensors add their unique id in the "id" field and add 
name of your choosing.

If you don't know the unique IDs of your DS18B20s you can run ``python3 get_ds18b20_ids.py``
which will print them out for you.

``"influx_server_ip": "<ip>"`` sets the IP of your InfluxDB Server or localhost if you run it on your RPi


``"ds18b20_precision": <9-12>`` sets the precision for the ds18b20 sensors between 9 and 12

````
Mode	 |   Resolution	|   Conversion time
-------------------------------------------
9 bits	 |   0.5°C	|   93.75 ms
10 bits	 |   0.25°C	|   187.5 ms
11 bits	 |   0.125°C    |   375 ms
12 bits	 |   0.0625°C   |   750 ms
````

Example config:
````
{
  "dht22":
  [
    {
      "pin": 17,
      "name": "dht1"
    },
    {
      "pin": 16,
      "name": "dht2"
    }
  ],
  "ds18b20":
  [
    {
      "id": "011316e9c41b",
      "name": "ds1"
    },
    {
      "id": "01183108d9ff",
      "name": "ds2"
    },
    {
      "id": "021830b173ff",
      "name": "ds3"
    }
  ],
  "influx_server_ip": "localhost",
  "ds18b20_precision": "12"
}
````

#### Autorun the Script on system startup

I supply a default unit file. For it to work you have to clone this repo into home directory of the user pi (``/home/pi/``).
If you want to store the script in another location you just have to change the path to the ``pifluxtemp.service``.

Copy the unit file ``pifluxtemp.service`` to the correct directory:

````sudo cp /home/pi/PifluxTemp/pifluxtemp.service /lib/systemd/system/````

Then set the right permissions on that file:

````sudo chmod 644 /lib/systemd/system/pifluxtemp.service````

Then enable the service:
````
sudo systemctl daemon-reload
sudo systemctl enable pifluxtemp.service
````

Then reboot:

````sudo reboot````

The script should now autostart on system startup.

If you want to check the status of the script:

``sudo systemctl status pifluxtemp.service``
