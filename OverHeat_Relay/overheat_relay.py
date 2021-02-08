import Jetson.GPIO as GPIO
import time
import subprocess
#import board
import sys
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/')
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/Jetson/GPIO')

# Pin Definitions
output_pin = 18  # BOARD pin 12, BCM pin 18

def main():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BCM)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    try:
        while True:
            # Toggle the output every second
            #print("Outputting {} to pin {}".format(curr_value, output_pin))
            #GPIO.output(output_pin, curr_value)
            #curr_value ^= GPIO.HIGH

            cmd2 = "cat /sys/class/thermal/thermal_zone0/temp |  awk \'{printf \"%.1f \", $(NF-0) / 1000}\'" # pylint: disable=line-too-long
            Temp2 = subprocess.check_output(cmd2, shell=True).decode("utf-8")
            print(Temp2)

            if float(Temp2) > 50:
                #y += font.getsize("OVERHEATING")[1]
                #draw.text((x+5, y+20), "OVERHEATING", font=font2, fill="#0000FF")  
                GPIO.output(output_pin, curr_value)
                #curr_value ^= GPIO.HIGH
                curr_value = GPIO.LOW
            
            else:
                time.sleep(5)
                GPIO.output(output_pin, GPIO.HIGH)

            time.sleep(.1)
    
    
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()