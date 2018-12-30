from pyHS100 import Discover
from app.influx import Influx
from threading import Thread
from app.hs110 import HS110


def main():

    influx = Influx()

    threads = []

    for dev in Discover.discover():
        threads.append(Thread(name=dev, target=HS110, args=(dev, influx)))

    for thread in threads:
        thread.start()
        print("< {}".format(thread))


if __name__ == "__main__":
    main()
