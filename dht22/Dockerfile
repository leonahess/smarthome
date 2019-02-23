FROM python:alpine
RUN apk add build-base

ADD . .

WORKDIR .

RUN pip3 install -r requirements.txt
RUN apt-get install python3-numpy

CMD [ "python3", "smarthome_dht22.py" ]