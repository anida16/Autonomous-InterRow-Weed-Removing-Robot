import Jetson.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN)


while True:
    x = GPIO.input(15)

    if x is 0:
        print("Button is pressed")
        os.system("./over_heat_protection.sh")
    
    if x is 1:
        print("Button is released")
        
    
    #if x is 1:
    #   print("Button Pressed")

    #if x is 0:
    #    print("Button is Released")

GPIO.cleanup()