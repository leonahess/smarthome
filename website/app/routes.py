from flask import render_template
from app import app
from app import influx
from app import sensors
import dateutil.parser


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/sensors')
def table():
    temp_result = []
    hum_result = []

    for sensor in sensors:

        if sensor['temp']:
            measurement = sensor['name']
            query = influx.query("SELECT temperature FROM {} ORDER by time DESC LIMIT 1".format(measurement))
            raw = query.get_points()
            for res in raw:
                time = dateutil.parser.parse(res['time'])
                temp_result.append(
                    {
                        "temperature": round(res['temperature'], 2),
                        "time": "{}:{}.{}".format(time.hour, time.minute, time.second),
                        "name": sensor['nickname']
                   }
                )

        if sensor['hum']:
            query2 = influx.query("SELECT humidity FROM {} ORDER by time DESC LIMIT 1".format(measurement))
            raw2 = query2.get_points()
            for res2 in raw2:
                time = dateutil.parser.parse(res2['time'])
                hum_result.append(
                    {
                        "humidity": round(res2['humidity'], 2),
                        "time": "{}:{}.{}".format(time.hour, time.minute, time.second),
                        "name": sensor['nickname']
                    }
                )

    return render_template('sensors.html', temp_result=temp_result, hum_result=hum_result)