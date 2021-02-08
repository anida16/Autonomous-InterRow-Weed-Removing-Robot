from __future__ import print_function
import xbox
import smbus
import time
import math
import Jetson.GPIO as GPIO
import subprocess
import digitalio
import board

bus = smbus.SMBus(1)
address = 0x08

output_pin = digitalio.DigitalInOut(board.D18)  # BOARD pin 12, BCM pin 18
output_pin.direction = digitalio.Direction.OUTPUT

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

def press_button(boolean, ifTrue, ifFalse):
    if boolean:
        output_pin.value = ifTrue
    else:
        output_pin.value = ifFalse

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

def angleFromCoords(x,y):
    angle = 0.0
    if x==0.0 and y==0.0:
        angle = -1
    elif x>=0.0 and y>=0.0:
        # first quadrant
        angle = math.degrees(math.atan(y/x)) if x!=0.0 else 90.0
    elif x<0.0 and y>=0.0:
        # second quadrant
        angle = math.degrees(math.atan(y/x))
        angle += 180.0
    elif x<0.0 and y<0.0:
        # third quadrant
        angle = math.degrees(math.atan(y/x))
        angle += 180.0
    elif x>=0.0 and y<0.0:
        # third quadrant
        angle = math.degrees(math.atan(y/x)) if x!=0.0 else -90.0
        angle += 360.0
    return angle
 

# Instantiate the controller
joy = xbox.Joystick()

# Show various axis and button states until Back button is pressed
print("Xbox controller sample: Press Back button to exit")
while not joy.Back():
    # Show connection status
    #show("Connected:")
    #showIf(joy.connected(), "Y", "N")
    # Left analog stick
    press_button(joy.Y(), False, True)
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
    
    x, y = joy.leftStick()
    angle = angleFromCoords(x,y)
    #print(angle)

    #showIf(angle==-1, 0x3D)
    showIf(angle==0, 0x3D)
    showIf(0<angle<=3, 0x3E)
    showIf(3<angle<=6, 0x3F)
    showIf(6<angle<=9, 0x40)
    showIf(9<angle<=12, 0x41)
    showIf(12<angle<=15, 0x42)
    showIf(15<angle<=18, 0x43)
    showIf(18<angle<=21, 0x44)
    showIf(21<angle<=24, 0x45)
    showIf(24<angle<=27, 0x46)
    showIf(27<angle<=30, 0x47)
    showIf(30<angle<=33, 0x48)
    showIf(33<angle<=36, 0x49)
    showIf(36<angle<=39, 0x4A)
    showIf(39<angle<=42, 0x4B)
    showIf(42<angle<=45, 0x4C)
    showIf(45<angle<=48, 0x4D)
    showIf(48<angle<=51, 0x4E)
    showIf(51<angle<=54, 0x4F)
    showIf(54<angle<=57, 0x50)
    showIf(57<angle<=60, 0x51)
    showIf(60<angle<=63, 0x52)
    showIf(63<angle<=66, 0x53)
    showIf(66<angle<=69, 0x54)
    showIf(69<angle<=72, 0x55)
    showIf(72<angle<=75, 0x56)
    showIf(75<angle<=78, 0X57)
    showIf(78<angle<=81, 0x58)
    showIf(81<angle<=84, 0x59)
    showIf(84<angle<=87, 0x5A)
    showIf(87<angle<=90, 0x5B)

    showIf(90<angle<=93, 0x5C)
    showIf(93<angle<=96, 0x5D)
    showIf(96<angle<=99, 0x5E)
    showIf(99<angle<=102, 0x5F)
    showIf(102<angle<=105, 0x60)
    showIf(105<angle<=108, 0x61)
    showIf(108<angle<=111, 0x62)
    showIf(111<angle<=114, 0x63)
    showIf(114<angle<=117, 0x64)
    showIf(117<angle<=120, 0x65)
    showIf(120<angle<=123, 0x66)
    showIf(123<angle<=126, 0x67)
    showIf(126<angle<=129, 0x68)
    showIf(129<angle<=132, 0x69)
    showIf(132<angle<=135, 0x6A)
    showIf(135<angle<=138, 0x6B)
    showIf(138<angle<=141, 0x6C)
    showIf(141<angle<=144, 0x6D)
    showIf(144<angle<=147, 0x6E)
    showIf(147<angle<=150, 0x6F)
    showIf(150<angle<=153, 0x70)
    showIf(153<angle<=156, 0x71)
    showIf(156<angle<=159, 0x72)
    showIf(159<angle<=162, 0x73)
    showIf(162<angle<=165, 0x74)
    showIf(165<angle<=168, 0x75)
    showIf(168<angle<=171, 0x76)
    showIf(171<angle<=174, 0x77)
    showIf(174<angle<=177, 0x78)
    showIf(177<angle<=180, 0x79)

    showIf(180<angle<=183, 0x7A)
    showIf(183<angle<=186, 0x7B)
    showIf(186<angle<=189, 0x7C)
    showIf(189<angle<=192, 0x7D)
    showIf(192<angle<=195, 0x7E)
    showIf(195<angle<=198, 0x7F)
    showIf(198<angle<=201, 0x80)
    showIf(201<angle<=204, 0x81)
    showIf(204<angle<=207, 0x82)
    showIf(207<angle<=210, 0x83)
    showIf(210<angle<=213, 0x84)
    showIf(213<angle<=216, 0x85)
    showIf(216<angle<=219, 0x86)
    showIf(219<angle<=222, 0x87)
    showIf(222<angle<=225, 0x88)
    showIf(225<angle<=228, 0x89)
    showIf(228<angle<=231, 0x8A)
    showIf(231<angle<=234, 0x8B)
    showIf(234<angle<=237, 0x8C)
    showIf(237<angle<=240, 0x8D)
    showIf(240<angle<=243, 0x8E)
    showIf(243<angle<=246, 0x8F)
    showIf(246<angle<=249, 0x90)
    showIf(249<angle<=252, 0x91)
    showIf(252<angle<=255, 0x92)
    showIf(255<angle<=258, 0x93)
    showIf(258<angle<=261, 0x94)
    showIf(261<angle<=264, 0x95)
    showIf(264<angle<=267, 0x96)
    showIf(267<angle<=270, 0x97)

    showIf(270<angle<=273, 0x98)
    showIf(273<angle<=276, 0x99)
    showIf(276<angle<=279, 0x9A)
    showIf(279<angle<=282, 0x9B)
    showIf(282<angle<=285, 0X9C)
    showIf(285<angle<=288, 0x9D)
    showIf(288<angle<=291, 0x9E)
    showIf(291<angle<=294, 0x9F)
    showIf(294<angle<=297, 0xA0)
    showIf(297<angle<=300, 0xA1)
    showIf(300<angle<=303, 0xA2)
    showIf(303<angle<=306, 0xA3)
    showIf(306<angle<=309, 0xA4)
    showIf(309<angle<=312, 0xA5)
    showIf(312<angle<=315, 0xA6)
    showIf(315<angle<=318, 0xA7)
    showIf(318<angle<=321, 0xA8)
    showIf(321<angle<=324, 0xA9)
    showIf(324<angle<=327, 0xAA)
    showIf(327<angle<=330, 0xAB)
    showIf(330<angle<=333, 0xAC)
    showIf(333<angle<=336, 0xAD)
    showIf(336<angle<=339, 0xAE)
    showIf(339<angle<=342, 0xAF)
    showIf(342<angle<=345, 0xB0)
    showIf(345<angle<=348, 0xB1)
    showIf(348<angle<=351, 0xB2)
    showIf(351<angle<=354, 0xB3)
    showIf(354<angle<=357, 0xB4)
    showIf(357<angle<=360, 0xB5)

    # Move cursor back to start of line
    show(chr(13))
# Close out when done
joy.close()