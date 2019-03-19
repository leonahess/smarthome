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
            query = influx.query(
                """SELECT temperature FROM temperature WHERE "name" = '{}' ORDER by time DESC LIMIT 1""".format(
                    measurement))
            raw = query.get_points()
            for res in raw:
                time = dateutil.parser.parse(res['time'])
                temp_result.append(
                    {
                        "temperature": round(res['temperature'], 2),
                        "time": "{}:{}.{}".format(time.hour + 1, time.minute, time.second),
                        "name": sensor['nickname']
                    }
                )

        if sensor['hum']:
            query2 = influx.query(
                """SELECT humidity FROM humidity WHERE "name" = '{}' ORDER by time DESC LIMIT 1""".format(measurement))
            raw2 = query2.get_points()
            for res2 in raw2:
                time = dateutil.parser.parse(res2['time'])
                hum_result.append(
                    {
                        "humidity": round(res2['humidity'], 2),
                        "time": "{}:{}.{}".format(time.hour + 1, time.minute, time.second),
                        "name": sensor['nickname']
                    }
                )

    return render_template('sensors.html', temp_result=temp_result, hum_result=hum_result)


@app.route('/graphs')
def graphs():
    front_outer = []
    back_outer = []
    front_board = []
    back_board = []
    front_radiator = []
    back_radiator = []

    front_outer_query = influx.query(
        """SELECT mean("temperature") FROM "temperature" WHERE ("name" = 'front_window_outside') AND (time > now() - 1d) 
        GROUP BY time(10m)fill(0)""")
    back_outer_query = influx.query(
        """SELECT mean("temperature") FROM "temperature" WHERE ("name" = 'back_window_outside') AND (time > now() - 1d) 
        GROUP BY time(10m)fill(0)""")
    front_board_query = influx.query(
        """SELECT mean("temperature") FROM "temperature" WHERE ("name" = 'front_window_inside') AND (time > now() - 1d) 
        GROUP BY time(10m)fill(0)""")
    back_board_query = influx.query(
        """SELECT mean("temperature") FROM "temperature" WHERE ("name" = 'back_window_inside') AND (time > now() - 1d) 
        GROUP BY time(10m)fill(0)""")
    back_radiator_query = influx.query(
        """SELECT mean("temperature") FROM "temperature" WHERE ("name" = 'back_radiator') AND (time > now() - 1d) 
        GROUP BY time(10m)fill(0)""")
    front_radiator_query = influx.query(
        """SELECT mean("temperature") FROM "temperature" WHERE ("name" = 'front_radiator') AND (time > now() - 1d) 
        GROUP BY time(10m)fill(0)""")

    for res in front_outer_query.get_points():
        time = dateutil.parser.parse(res['time'])
        if res['mean'] is not None:
            front_outer.append(
                {
                    "temperature": round(res['mean'], 2),
                    "time": res['time'],
                    "name": "front_window_outside"
                }
            )
    for res in back_outer_query.get_points():
        time = dateutil.parser.parse(res['time'])
        if res['mean'] is not None:
            back_outer.append(
                {
                    "temperature": round(res['mean'], 2),
                    "time": res['time'],
                    "name": "front_window_outside"
                }
            )
    for res in front_board_query.get_points():
        time = dateutil.parser.parse(res['time'])
        if res['mean'] is not None:
            front_board.append(
                {
                    "temperature": round(res['mean'], 2),
                    "time": res['time'],
                    "name": "front_window_outside"
                }
            )
    for res in back_board_query.get_points():
        time = dateutil.parser.parse(res['time'])
        if res['mean'] is not None:
            back_board.append(
                {
                    "temperature": round(res['mean'], 2),
                    "time": res['time'],
                    "name": "front_window_outside"
                }
            )
    for res in front_radiator_query.get_points():
        time = dateutil.parser.parse(res['time'])
        if res['mean'] is not None:
            front_radiator.append(
                {
                    "temperature": round(res['mean'], 2),
                    "time": res['time'],
                    "name": "front_window_outside"
                }
            )
    for res in back_radiator_query.get_points():
        time = dateutil.parser.parse(res['time'])
        if res['mean'] is not None:
            back_radiator.append(
                {
                    "temperature": round(res['mean'], 2),
                    "time": res['time'],
                    "name": "front_window_outside"
                }
            )

    return render_template('graphs.html', front_outer=front_outer, back_outer=back_outer, front_board=front_board,
                           back_board=back_board, front_radiator=front_radiator, back_radiator=back_radiator)
