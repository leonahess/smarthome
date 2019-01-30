from flask import render_template
from app import app
from app import influx
from app import sensors


@app.route('/')
def index():
    user = {'username': 'Leon'}

    temp_result = []
    hum_result = []

    for sensor in sensors:

        if sensor['temp']:
            measurement = sensor['name']
            query = influx.query("SELECT temperature FROM {} ORDER by time DESC LIMIT 1".format(measurement))
            raw = query.get_points()
            for res in raw:
                temp_result.append(
                    {
                        "temperature": res['temperature'],
                        "time": res['time'],
                        "name": sensor['nickname']
                    }
                )

        if sensor['hum']:
            query2 = influx.query("SELECT humidity FROM {} ORDER by time DESC LIMIT 1".format(measurement))
            raw2 = query2.get_points()
            for res2 in raw2:
                hum_result.append(
                    {
                        "humidity": res2['humidity'],
                        "time": res2['time'],
                        "name": sensor['nickname']
                    }
                )

    return render_template('index.html', temp_result=temp_result, hum_result=hum_result)
