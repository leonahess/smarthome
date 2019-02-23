FROM python:alpine

ADD . .

WORKDIR .

RUN pip3 install -r requirements.txt
RUN apk add py3-numpy

CMD [ "python3", "smarthome_dht22.py" ]