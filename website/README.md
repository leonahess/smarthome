## Run as Docker Container

````
docker build -t conatiner_name .
docker run --net=host --restart always container_name
````

## Autorun the Script on system startup with systemd

I supply a default unit file. For it to work you have to edit the ``WorkingDirectory=`` path and the ``ExecStart=`` path
to your installation location in ``smartfluxdash.service``.

Copy the unit file ``smartfluxdash.service`` to the correct directory:

````sudo cp /your/path/SmartFluxDash/smartfluxdash.service /lib/systemd/system/````

Then set the right permissions on that file:

````sudo chmod 644 /lib/systemd/system/smartfluxdash.service````

Then enable the service:
````
sudo systemctl daemon-reload
sudo systemctl enable smartfluxdash.service
````

Then reboot:

````sudo reboot````

The script should now autostart on system startup.

If you want to check the status of the script:

``sudo systemctl status smartfluxdash.service``