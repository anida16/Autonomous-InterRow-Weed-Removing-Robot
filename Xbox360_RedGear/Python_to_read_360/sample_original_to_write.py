from __future__ import print_function
import xbox
import smbus
import time
import math

bus = smbus.SMBus(1)
address = 0x08


# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)
    #writeData(n)

# Print one or more values without a line feed
def show(*args):
    for arg in args:
        print(arg, end="")
        #writeData(arg)
        #print()

# Print true or false value based on a boolean, without linefeed
def showIf(boolean, ifTrue, ifFalse=" "):
    if boolean:
        show(ifTrue)
        #print(ifTrue)
        writeData(ifTrue)
    else:
        show(ifFalse)

def writeData(value):
    #time.sleep(3)
    #byteValue = StringToBytes(value)  
    #bus.write_i2c_block_data(address,0x08,byteValue) #first byte is 0=command byte.. just is.
    bus.write_byte(address, value)
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
while not joy.Back():
    # Show connection status
    #show("Connected:")
    #showIf(joy.connected(), "Y", "N")
    # Left analog stick
    show("  Left X/Y:", fmtFloat(joy.leftX()), "/", fmtFloat(joy.leftY()))
    # Right trigger
    #show("  RightTrg:", fmtFloat(joy.rightTrigger()))
    # A/B/X/Y buttons
    show("  Buttons:")
    showIf(joy.A(), 0x1)
    showIf(joy.B(), 0x2)
    showIf(joy.X(), 0x3)
    showIf(joy.Y(), 0x4)
    # Dpad U/D/L/R
    #show("  Dpad:")
    showIf(joy.dpadUp(),    0x5)
    showIf(joy.dpadDown(),  0x6)
    showIf(joy.dpadLeft(),  0x7)
    showIf(joy.dpadRight(), 0x8)

    showIf(joy.leftBumper(),  0x9)
    showIf(joy.rightBumper(), 0xA)

    showIf((0<joy.rightTrigger()<=0.02), 0xB)
    showIf((0.02<joy.rightTrigger()<=0.04), 0xC)
    showIf((0.04<joy.rightTrigger()<=0.06), 0xD)
    showIf((0.06<joy.rightTrigger()<=0.08), 0xE)
    showIf((0.08<joy.rightTrigger()<=0.1), 0xF)
    showIf((0.1<joy.rightTrigger()<=0.12), 0x10)
    showIf((0.12<joy.rightTrigger()<=0.14), 0x11)
    showIf((0.14<joy.rightTrigger()<=0.16), 0x12)
    showIf((0.16<joy.rightTrigger()<=0.18), 0x13)
    showIf((0.18<joy.rightTrigger()<=0.2), 0x14)

    showIf((0.2<joy.rightTrigger()<=0.22), 0x15)
    showIf((0.22<joy.rightTrigger()<=0.24), 0x16)
    showIf((0.24<joy.rightTrigger()<=0.26), 0x17)
    showIf((0.26<joy.rightTrigger()<=0.28), 0x18)
    showIf((0.28<joy.rightTrigger()<=0.3), 0x19)
    showIf((0.3<joy.rightTrigger()<=0.32), 0x1A)
    showIf((0.32<joy.rightTrigger()<=0.34), 0x1B)
    showIf((0.34<joy.rightTrigger()<=0.36), 0x1C)
    showIf((0.36<joy.rightTrigger()<=0.38), 0x1D)
    showIf((0.38<joy.rightTrigger()<=0.4), 0x1E)

    showIf((0.4<joy.rightTrigger()<=0.42), 0x1F)
    showIf((0.42<joy.rightTrigger()<=0.44), 0x20)
    showIf((0.44<joy.rightTrigger()<=0.46), 0x21)
    showIf((0.46<joy.rightTrigger()<=0.48), 0x22)
    showIf((0.48<joy.rightTrigger()<=0.5), 0x23)
    showIf((0.5<joy.rightTrigger()<=0.52), 0x24)
    showIf((0.52<joy.rightTrigger()<=0.54), 0x25)
    showIf((0.54<joy.rightTrigger()<=0.56), 0x26)
    showIf((0.56<joy.rightTrigger()<=0.58), 0x27)
    showIf((0.58<joy.rightTrigger()<=0.6), 0x28)

    showIf((0.6<joy.rightTrigger()<=0.62), 0x29)
    showIf((0.62<joy.rightTrigger()<=0.64), 0x2A)
    showIf((0.64<joy.rightTrigger()<=0.66), 0x2B)
    showIf((0.66<joy.rightTrigger()<=0.68), 0x2C)
    showIf((0.68<joy.rightTrigger()<=0.7), 0x2D)
    showIf((0.7<joy.rightTrigger()<=0.72), 0x2E)
    showIf((0.72<joy.rightTrigger()<=0.74), 0X2F)
    showIf((0.74<joy.rightTrigger()<=0.76), 0x30)
    showIf((0.76<joy.rightTrigger()<=0.78), 0x31)
    showIf((0.78<joy.rightTrigger()<=0.8), 0x32)

    showIf((0.8<joy.rightTrigger()<=0.82), 0x33)
    showIf((0.82<joy.rightTrigger()<=0.84), 0x34)
    showIf((0.84<joy.rightTrigger()<=0.86), 0x35)
    showIf((0.86<joy.rightTrigger()<=0.88), 0x36)
    showIf((0.88<joy.rightTrigger()<=0.9), 0x37)
    showIf((0.9<joy.rightTrigger()<=0.92), 0x38)
    showIf((0.92<joy.rightTrigger()<=0.94), 0X39)
    showIf((0.94<joy.rightTrigger()<=0.96), 0x3A)
    showIf((0.96<joy.rightTrigger()<=0.98), 0x3B)
    showIf((0.98<joy.rightTrigger()<=1), 0x3C)
    

    
    # Move cursor back to start of line
    show(chr(13))
# Close out when done
joy.close()