from flask import render_template
from app import app
from app import influx
from app import sensors


@app.route('/')
def index():
    user = {'username': 'Leon'}

    result = []
    result2 = []

    for sensor in sensors:
        measurement = sensor['name']
        query = influx.query("SELECT temperature FROM {} ORDER by time DESC LIMIT 1".format(measurement))
        raw = query.get_points()

        for res in raw:
            result2.append(res)
            result.append(
                {
                    "temperature": res['temperature'],
                    "time": res['time'],
                    "name": sensor['name']
                }
            )

    return render_template('index.html', query=result)
