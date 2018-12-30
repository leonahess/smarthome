from influxdb import InfluxDBClient


class Influx:

    def __init__(self):
        self.client = InfluxDBClient(host="localhost", port=8086, database='smarthome')

        print("< connected to influx!")
        print("> checking if database 'smarthome' exists ...")

        database_list = self.client.get_list_database()
        smarthome_exists = False

        for s in range(0, len(database_list)):
            if database_list[s]['name'] == 'smarthome':
                smarthome_exists = True

                print("< database 'smarthome' exists")

        if not smarthome_exists:
            print("< database 'smarthome' does not exist!")
            print("> creating database 'smarthome' ...")

            self.client.create_database('smarthome')

            print("< created database 'smarthome'!")
