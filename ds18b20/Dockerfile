FROM python:alpine

ADD . .

WORKDIR .

RUN pip3 install w1thermsensor
RUN pip3 install influxdb

CMD [ "python3", "smarthome_ds18b20.py" ]