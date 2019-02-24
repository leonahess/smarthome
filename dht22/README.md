# DHT22 submodule

Currently untested

## Requirements

#### Required Python modules

````
influxdb
Adafruit_DHT
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

Connect one dht22 to a GPIO port of your choosing respectively.
Also don't forget to enable the 1wire bus.

#### Edit the config.json

For the dht22 sensors add the gpio pin which you connected it to and
add a name of your choosing.

``influx_ip = "192.168.66.56"`` sets the IP of your InfluxDB Server or localhost if you run it on your RPi

``influx_port = "8086"`` sets the port of the InfluxDB Server, default is ``8086``.

``influx_database = "smarthome"`` sets the database name, default is ``smarthome``.


#### Autorun the Script on system startup

##### Docker

````
docker build -t conatiner_name .
docker run --restart always -d --name=dht22 --privileged container_name
````

##### systemd

I supply a default unit file. For it to work you have to clone this repo into home directory of the user pirate 
(``/home/pirate/``).
If you want to store the script in another location you just have to change the path to the 
``smarthome_dht22.service``.

Copy the unit file ``smarthome_dht22.service`` to the correct directory:

````sudo cp smarthome_dht22.service /lib/systemd/system/````

Then set the right permissions on that file:

````sudo chmod 644 /lib/systemd/system/smarthome_dht22.service````

Then enable the service:
````
sudo systemctl daemon-reload
sudo systemctl enable smarthome_dht22.service
````

The script should now autostart on system startup.
It should also try to restart if it crashes.

you can start the script without rebooting with:

````
sudo systemctl start smarthome_dht22.service
````

If you want to check the status of the script:

``sudo systemctl status smarthome_dht22.service``