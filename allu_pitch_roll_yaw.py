from sense_hat import SenseHat


sense = SenseHat()
sense.clear()

o = sense.get_orientation()
pitch = round(o["pitch"],1)
roll = round(o["roll"],1)
yaw = round(o["yaw"],1)
sense.show_message("pitch %s roll %s yaw %s" % (pitch, roll, yaw))
print("pitch %s roll %s yaw %s" % (pitch, roll, yaw))
