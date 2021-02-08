import smbus
import time
# Nvidia Jetson Nano i2c Bus 0
bus = smbus.SMBus(1)
time.sleep(3)
# This is the address we setup in the Arduino Program
address = 0x08

def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number

def writeData(value):
    byteValue = StringToBytes(value)    
    bus.write_i2c_block_data(address,0x00,byteValue) #first byte is 0=command byte.. just is.
    return -1

def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal

while True:
    print("sending")
    writeData("test")   
    time.sleep(5)

    print('OPEN')
    writeData("OPEN-00-00")
    time.sleep(7)

    print('WIN')
    writeData("WIN-12-200")
    time.sleep(7)