import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
pwm=GPIO.PWM(7,50)
pwm.start(5)

choice = 3
while choice != 0:
    choice = int(raw_input("1: on\n2: off\n0: stop\n:"))
    print (choice)
    if choice == 1:
        pwm.ChangeDutyCycle(5)
        print ("######## ON ########")
    if choice == 2:
        pwm.ChangeDutyCycle(10)
        print ("######## OFF ########")
