FROM python:alpine
RUN apk add build-base

ADD . .

WORKDIR .

RUN pip3 install -r requirements.txt

CMD [ "python3", "smarthome_dht22.py" ]