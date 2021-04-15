import time
import board
import digitalio
     
print("press the button!")
     
#led = digitalio.DigitalInOut(board.D18)
#led.direction = digitalio.Direction.OUTPUT
     
button = digitalio.DigitalInOut(board.D18)
button.direction = digitalio.Direction.INPUT
# use an external pullup since we don't have internal PU's
#button.pull = digitalio.Pull.UP
     
while True:
    print(button.value)
        #led.value = not button.value # light when button is pressed!
    if button.value is False:
        print("button pressed")

    if button.value is True:
        print("button released")

    #GPIO.cleanup()