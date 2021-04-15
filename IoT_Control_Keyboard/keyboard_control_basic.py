from __future__ import print_function
from pynput.keyboard import Key, Listener, Controller
import smbus
import time
import math

bus = smbus.SMBus(1)
address = 0x08

def writeData(value):
    #time.sleep(3)
    #byteValue = StringToBytes(value)  
    #bus.write_i2c_block_data(address,0x08,byteValue) #first byte is 0=command byte.. just is.
    bus.write_byte(address, value)
    return -1

def on_release(key):
    print("Key released")
    #writeData(0xB6)

keyboard = Controller()
def show(key): 

    
    if key.char is ('w'): 
        print("Dpad Up") 
        writeData(0x5)
    
    elif key.char is ('a'): 
        print("Dpad left") 
        writeData(0x7)

    elif key.char is ('s'): 
        print("Dpad Down") 
        writeData(0x6)

    elif key.char is ('d'): 
        print("Dpad right") 
        writeData(0x8)

    else:
        print("dsds")
        writeData(0xB6)

    if key == Key.delete:  
        return False

    #if 
     #   print("Nothing Pressed")
      #  writeData(0xB6)
  
# Collect all event until released 
while(True):
       
    with Listener(on_press = show, on_release = on_release) as listener: 
        listener.join() 
       
