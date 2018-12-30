## Run as Docker Container

````
docker build -t conatiner_name .
docker run --net=host --restart always -d container_name
````

## Autorun the Script on system startup with systemd

I supply a default unit file. For it to work you have to edit the ``WorkingDirectory=`` path and the ``ExecStart=`` path
to your installation location in ``HS110Flux.service``.

Copy the unit file ``HS110Flux.service`` to the correct directory:

````sudo cp /your/path/HS110Flux/HS110Flux.service /lib/systemd/system/````

Then set the right permissions on that file:

````sudo chmod 644 /lib/systemd/system/HS110Flux.service````

Then enable the service:
````
sudo systemctl daemon-reload
sudo systemctl enable HS110Flux.service
````

Then reboot:

````sudo reboot````

The script should now autostart on system startup.

If you want to check the status of the script:

``sudo systemctl status HS110Flux.service``