FROM python:alpine
RUN apk add tzdata

ADD . .

WORKDIR .

RUN pip3 install -r requirements.txt

CMD ["python3", "smarthome_raspi.py"]