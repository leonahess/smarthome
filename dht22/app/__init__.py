from influxdb import InfluxDBClient
import config

client = InfluxDBClient(host=config.influx_ip, port=config.influx_port, database=config.influx_database)

print("< connected to influx!")
print("> checking if database 'smarthome' exists ...")

database_list = client.get_list_database()
smarthome_exists = False

for s in range(0, len(database_list)):
    if database_list[s]['name'] == 'smarthome':
        smarthome_exists = True

        print("< database 'smarthome' exists")

if not smarthome_exists:

    print("< database 'smarthome' does not exist!")
    print("> creating database 'smarthome' ...")

    client.create_database('smarthome')

    print("< created database 'smarthome'!")
