# HS110 submodule

## Requirements
#### Required Python modules

````
influxdb
pyHS100
````

To install them run ``sudo pip3 install -r requirements.txt``

If you don't have pip installed install it with ``sudo apt-get install python3-pip``

## Getting started

setup all you ``HS110``'s with the Kasa App. Then run:

````
python3 smarthome_hs110.py
````

#### Autorun the Script on system startup

##### Docker

````
docker build -t conatiner_name .
docker run --net=host --restart always -d --name=hs110 container_name
````

##### systemd

I supply a default unit file. For it to work you have to edit the ``WorkingDirectory=`` path and the ``ExecStart=`` path
to your installation location in ``smarthome_hs110.service``.

Copy the unit file ``smarthome_hs110.service`` to the correct directory:

````
sudo cp smarthome_hs110.service /lib/systemd/system/
````

Then set the right permissions on that file:

````
sudo chmod 644 /lib/systemd/system/smarthome_hs110.service
````

Then enable the service:
````
sudo systemctl daemon-reload
sudo systemctl enable smarthome_hs110.service
````

The script should now autostart on system startup.
It should also try to restart if it crashes.

you can start the script without rebooting with:

````
sudo systemctl start smarthome_ds18b20.service
````
If you want to check the status of the script:

````
sudo systemctl status smarthome_hs110.service
````
