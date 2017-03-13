from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
sense.show_message("Temp: " + (str("%.1f" % temp)))
print("Temp: " + (str("%.1f" % temp)))

humidity = sense.get_humidity()
sense.show_message("Hum: " + (str(round(humidity,1))))
print("Hum: " + (str(round(humidity,1))))
