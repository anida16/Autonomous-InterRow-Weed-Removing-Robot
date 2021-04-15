#!/usr/bin/env python

# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import Jetson.GPIO as GPIO
import time
import os

# Pin Definitions:
auto_button = 31
semi_auto_button = 32
manual_button = 33
iot_button = 35
critical_button = 36
shut_down_button = 37

# blink LED 2 quickly 5 times when button pressed
def manual(channel1):

    if GPIO.input(33) is 0:
        print("Manual Button Pressed")
        os.system("terminator -e \"./manual_control.sh\"")

    else:
        print("ignore")
    
    #GPIO.add_event_detect(manual_button, GPIO.RISING, callback=main, bouncetime=10)
    
def critical(channel2):

    if GPIO.input(36) is 0:
        print("Critical Button Pressed")
        os.system("terminator -e \"./over_heat_protection.sh\"")
        print("im here at critical button")

    else:
        print("ignore")

 
    #GPIO.add_event_detect(manual_button, GPIO.RISING, callback=main, bouncetime=10)


def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    #GPIO.setup([led_pin_1, led_pin_2], GPIO.OUT)  # LED pins set as output
    GPIO.setup([auto_button, semi_auto_button, manual_button, iot_button, critical_button, shut_down_button], GPIO.IN)  # button pin set as input

    # Initial state for LEDs:
    #GPIO.output(led_pin_1, GPIO.LOW)
    #GPIO.output(led_pin_2, GPIO.LOW)
    GPIO.add_event_detect(manual_button, GPIO.FALLING, callback=manual, bouncetime=1000)
    GPIO.add_event_detect(critical_button, GPIO.FALLING, callback=critical, bouncetime=1000)
    

    print("Starting demo now! Press CTRL+C to exit")
    try:
        #print("Bruh")
        while True:
            # blink LED 1 slowly
            '''
            GPIO.output(led_pin_1, GPIO.HIGH)
            print("LED 1 ON")
            time.sleep(2)
            GPIO.output(led_pin_1, GPIO.LOW)
            print("LED 1 OFF")
            time.sleep(2)
            '''
            print("Inside Main loop")
            time.sleep(2)
    finally:
        GPIO.cleanup()  # cleanup all GPIOs

if __name__ == '__main__':
    main()