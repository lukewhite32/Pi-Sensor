from time import sleep
import json

sense = SenseHat()
sense.set_imu_config(True, True, True)

while 1:
    joyButtons = [False, False, False, False, False]
    joyDirections = ["up", "down", "left", "right", "middle"]

    for event in sense.stick.get_events():
        if event.action == "pressed":
            joyButtons[joyDirections.index(event.direction)] = True
        elif event.action == "released":
            joyButtons[joyDirections.index(event.direction)] = False

    sense.set_imu_config(True, False, False)
    compass = sense.get_compass()

    sense.set_imu_config(False, True, False)
    gyroPitch = sense.get_orientation_degrees()[0]
    gyroRoll = sense.get_orientation_degrees()[1]
    gyroYaw = sense.get_orientation_degrees()[2]

    sense.set_imu_config(False, False, True)
    accelPitch = sense.get_accelerometer()[0]
    accelRoll = sense.get_accelerometer()[1]
    accelYaw = sense.get_accelerometer()[2]

    data = {
        "temp" : sense.get_temperature(), 
        "pressure" : sense.get_pressure(),
        "humidity" : sense.get_humidity(),
        "gyroPitch" : gyroPitch,
        "gyroRoll" : gyroRoll,
        "gyroYaw" : gyroYaw,
        "compass" : compass,
        "accelPitch" : accelPitch,
        "accelRoll" : accelRoll,
        "accelYaw" : accelYaw,
        "up" : joyButtons[0],
        "down" : joyButtons[1],
        "left" : joyButtons[2],
        "right" : joyButtons[3],
        "middle" : joyButtons[4]
        }
    string = json.dumps(data)

    sensorFile = open("html/data/sensor.json", 'w+')
    sensorFile.write(string)
    sensorFile.close()

    sleep(1)