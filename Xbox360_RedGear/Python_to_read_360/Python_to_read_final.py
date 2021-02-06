from __future__ import print_function
import xbox
import smbus
import time
import math
# Nvidia Jetson Nano i2c Bus 0
bus = smbus.SMBus(1)


# This is the address we setup in the Arduino Program
address = 0x08


# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

# Print one or more values without a line feed
def show(*args):
    for arg in args:
        print(arg, end="")
        #writeData(arg)
    

# Print true or false value based on a boolean, without linefeed
def showIf(boolean, ifTrue, ifFalse=" "):
    if boolean:
        show(ifTrue)
    else:
        show(ifFalse)

def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number

def writeData(value):
    #time.sleep(3)
    byteValue = StringToBytes(value)  
    bus.write_i2c_block_data(address,0x08,byteValue) #first byte is 0=command byte.. just is.
    return -1

def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal


# Instantiate the controller
joy = xbox.Joystick()

# Show various axis and button states until Back button is pressed
print("Xbox controller sample: Press Back button to exit")
#time.sleep(1)
while not joy.Back():
    # Show connection status
    #show("Connected:")
    #showIf(joy.connected(), "Y", "N")
    # Left analog stick
    #show("  Left X/Y:", fmtFloat(joy.leftX()), "/", fmtFloat(joy.leftY()))
    # Right analog stick
    #show("  Right X/Y:", fmtFloat(joy.rightX()), "/", fmtFloat(joy.rightY()))
    # Right Stick
    #show("  RightStick:", fmtFloat(joy.rightThumbstick()))
    # Left Stick
    #show("  LeffStick:", fmtFloat(joy.leftThumbstick()))
    # Right trigger
    #show("  RightTrg:", fmtFloat(joy.rightTrigger()))
    # Left trigger
    #show("  LeftTrg:", fmtFloat(joy.leftTrigger()))
    # Right button
    #show("  RightBut:", fmtFloat(joy.rightBumper()))
    # Left button
    #show("  LeftBut:", fmtFloat(joy.leftBumper()))
    # A/B/X/Y buttons
    #show("  Buttons:")
    #showIf(joy.A(), "A")
    #showIf(joy.B(), "B")
    #showIf(joy.X(), "X")
    #showIf(joy.Y(), "Y")
    # Dpad U/D/L/R
    #show("  Dpad:")
    #showIf(joy.dpadUp(),    "U")
    #showIf(joy.dpadDown(),  "D")
    #showIf(joy.dpadLeft(),  "L")
    #showIf(joy.dpadRight(), "R")
    # Move cursor back to start of line
    #show(chr(13)
    if joy.dpadDown() is 1:
        print("Dpad Down Pressed")
        writeData("dpadDown")
    elif joy.dpadUp() is 1:
        print("Dpad Up Pressed")
        writeData("dpadUp")
    elif joy.dpadLeft() is 1:
        print("Dpad Left Pressed")
        writeData("dpadLeft")
    elif joy.dpadRight() is 1:
        print("Dpad Right Pressed")
        writeData("dpadRight")
    elif joy.A() is 1:
        print("A Pressed")
        writeData("A")
    elif joy.B() is 1:
        print("B Pressed")
        writeData("B")
    elif joy.X() is 1:
        print("X Pressed")
        writeData("X")
    elif joy.Y() is 1:
        print("Y Pressed")
        writeData("Y")

    #elif math.ceil(joy.leftY()) is not 0 and math.ceil(joy.rightTrigger()) is not 0:
    #    if joy.leftY() < 0:
    #        print("Reverse Direction is ",joy.leftY(),"  Speed is",joy.rightTrigger())
    #        writeData("Reverse Direction is ",joy.leftY(),"  Speed is",joy.rightTrigger())
    #    #print(math.ceil(joy.leftY()))
    #    if joy.leftY() > 0:
    #        print("Forward Direction is ",joy.leftY(),"  Speed is",joy.rightTrigger())
    #        writeData("Forward Direction is ",joy.leftY(),"  Speed is",joy.rightTrigger())
    else:
        print("Brake")
        writeData("Brake")


# Close out when done
joy.close()
