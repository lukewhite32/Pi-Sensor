
from time import sleep
import json

sense = SenseHat()

while 1:
    data = {"temp" : sense.get_temperature()}
    string = json.dumps(data)

    sensorFile = open("html/data/sensor.json", 'w+')
    sensorFile.write(string)
    sensorFile.close()

    sleep(1)