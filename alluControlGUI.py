## /usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(2, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    GPIO.wait_for_edge(2, GPIO.FALLING)
    i = 0
    while i < 3:
        GPIO.output(24, True)
        time.sleep(1)
        GPIO.output(24, False)
        time.sleep(1)
        i += 1
except KeyboardInterrupt:
    GPIO.cleanup()    

try:
    GPIO.wait_for_edge(3, GPIO.FALLING)
    a = 0
    while a < 3:
        GPIO.output(23, True)
        time.sleep(1)
        GPIO.output(23, False)
        time.sleep(1)
        a += 1
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
