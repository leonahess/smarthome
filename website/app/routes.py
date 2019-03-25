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


def parse(query_result):

    parse_result = []

    for res in query_result.get_points():
        time = dateutil.parser.parse(res['time'])
        if res['mean'] is not None:
            parse_result.append(
                {
                    "data": round(res['mean'], 2),
                    "time": "{}:{}".format(time.hour + 1, time.minute),
                }
            )

    return parse_result


def query(field, measurement, tag, divisor):

    query_result = influx.query("""SELECT mean("{}") / {} FROM "{}" WHERE ("name" = '{}') AND (time > now() - 1d) 
        GROUP BY time(10m)fill(0)""".format(field, divisor, measurement, tag))

    return parse(query_result)


@app.route('/graphs')
def graphs():
    front_outer = query("temperature", "temperature", "front_window_outside", 1)
    back_outer = query("temperature", "temperature", "back_window_outside", 1)
    front_board = query("temperature", "temperature", "front_window_inside", 1)
    back_board = query("temperature", "temperature", "back_window_inside", 1)
    desk = query("temperature", "temperature", "desk", 1)
    front_radiator = query("temperature", "temperature", "front_radiator", 1)
    back_radiator = query("temperature", "temperature", "back_radiator", 1)
    back_board_hum = query("humidity", "humidity", "window_front", 1)
    front_board_hum = query("humidity", "humidity", "window_back", 1)
    desk_hum = query("humidity", "humidity", "desk", 1)
    power_computer = query("milliwatt", "power", "Computer", 1000)
    power_server = query("milliwatt", "power", "Server", 1000)
    power_small = query("milliwatt", "power", "Kleinteile", 1000)

    return render_template('graphs.html', front_outer=front_outer, back_outer=back_outer, front_board=front_board,
                           back_board=back_board, front_radiator=front_radiator, back_radiator=back_radiator, desk=desk,
                           back_board_hum=back_board_hum, front_board_hum=front_board_hum, desk_hum=desk_hum,
                           power_computer=power_computer, power_server=power_server, power_small=power_small)
