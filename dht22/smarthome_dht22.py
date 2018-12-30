from app.dht22 import DHT22
from threading import Thread
import config


def main():
    dht22()


def dht22():
    threads = []

    for entry in config.dht22:
        threads.append(Thread(name=entry["name"], target=DHT22, args=(entry["pin"], entry["name"])))

    print("> starting dht22 threads ...")

    for thread in threads:
        thread.start()
        print("< {}".format(thread))


if __name__ == "__main__":
        main()
