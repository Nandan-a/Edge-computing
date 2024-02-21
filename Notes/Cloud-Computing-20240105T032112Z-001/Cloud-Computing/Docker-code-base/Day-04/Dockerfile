FROM python:3.12-rc-buster

LABEL "developer"="diot-sept-2022"

WORKDIR /app/mqttapp

ADD . /app/mqttapp/

RUN pip install -r requirements.txt 

CMD ["python", "mqtt_subscriber.py"]



