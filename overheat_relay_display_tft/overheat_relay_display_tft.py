import Jetson.GPIO as GPIO
import subprocess
import digitalio
import board
import time
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789        # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357        # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735        # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351      # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331      # pylint: disable=unused-import
import os

# Pin Definitions
output_pin = digitalio.DigitalInOut(board.D18)  # BOARD pin 12, BCM pin 18
output_pin.direction = digitalio.Direction.OUTPUT
button_state = digitalio.DigitalInOut(board.D16)
button_manual = digitalio.DigitalInOut(board.D13)
auto_button = digitalio.DigitalInOut(board.D6)
semi_auto_button = digitalio.DigitalInOut(board.D12)
iot_button = digitalio.DigitalInOut(board.D19)


# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# pylint: disable=line-too-long
# Create the display:
#disp = st7789.ST7789(spi, rotation=90                             # 2.0" ST7789
#disp = st7789.ST7789(spi, height=240, y_offset=80, rotation=90    # 1.3", 1.54" ST7789
#disp = st7789.ST7789(spi, rotation=90, width=135, height=240, x_offset=53, y_offset=40, # 1.14" ST7789
#disp = hx8357.HX8357(spi, rotation=180,                           # 3.5" HX8357
disp = st7735.ST7735R(spi, rotation=90,                           # 1.8" ST7735R
#disp = st7735.ST7735R(spi, rotation=270, height=128, x_offset=2, y_offset=3,   # 1.44" ST7735R
#disp = st7735.ST7735R(spi, rotation=90, bgr=True,                 # 0.96" MiniTFT ST7735R
#disp = ssd1351.SSD1351(spi, rotation=180,                         # 1.5" SSD1351
#disp = ssd1351.SSD1351(spi, height=96, y_offset=32, rotation=180, # 1.27" SSD1351
#disp = ssd1331.SSD1331(spi, rotation=180,                         # 0.96" SSD1331
#disp = ili9341.ILI9341(spi, rotation=90,                           # 2.2", 2.4", 2.8", 3.2" ILI9341
                      cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=BAUDRATE)
# pylint: enable=line-too-long

if disp.rotation % 180 == 90:
    height = disp.width   # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width   # we swap height/width to rotate it to landscape!
    height = disp.height

image = Image.new('RGB', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)

# First define some constants to allow easy positioning of text.
padding = -2
x = 0

# Load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
font2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 20)

def main():
    # Pin Setup:
    # Board pin-numbering scheme
    #GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    #GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    #output_pin.value = True
    output_pin.value = True
    
    print("Starting demo now! Press CTRL+C to exit")
    #curr_value = GPIO.HIGH
    try:
        while True:

            # Draw a black filled box to clear the image.
            draw.rectangle((0, 0, width, height), outline=0, fill=0)

            # Shell scripts for system monitoring from here:
            # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
            cmd = "hostname -I | cut -d\' \' -f1"
            IP = "IP: "+subprocess.check_output(cmd, shell=True).decode("utf-8")
            cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
            CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
            cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
            MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
            cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%d GB  %s\", $3,$2,$5}'"
            Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
            cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk \'{printf \"CPU Temp: %.1f C\", $(NF-0) / 1000}\'" # pylint: disable=line-too-long
            Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")
            temp1 =  "cat /sys/class/thermal/thermal_zone0/temp |  awk \'{%.1f C\", $(NF-0) / 1000}\'"
            #Temp2 = subprocess.check_output(temp1, shell=True).decode("utf-8")

            # Toggle the output every second
            #print("Outputting {} to pin {}".format(curr_value, output_pin))
            #GPIO.output(output_pin, curr_value)
            #curr_value ^= GPIO.HIGH
            
            
            cmd2 = "cat /sys/class/thermal/thermal_zone0/temp |  awk \'{printf \"%.1f \", $(NF-0) / 1000}\'" # pylint: disable=line-too-long
            Temp2 = subprocess.check_output(cmd2, shell=True).decode("utf-8")
            print(Temp2)

            # Write four lines of text.
            y = padding
            draw.text((x, y), IP, font=font, fill="#FFFFFF")
            y += font.getsize(IP)[1]
            draw.text((x, y), CPU, font=font, fill="#FFFF00")
            y += font.getsize(CPU)[1]
            draw.text((x, y), MemUsage, font=font, fill="#00FF00")
            y += font.getsize(MemUsage)[1]
            draw.text((x, y), Disk, font=font, fill="#0000FF")
            y += font.getsize(Disk)[1]
            draw.text((x, y), Temp, font=font2, fill="#FF00FF")

            if button_manual.value is False:
                draw.text((0, 90), "Manual Mode", font=font2, fill="#0000FF") 
            
            if auto_button.value is False:
                draw.text((0, 90), "Auto Mode", font=font2, fill="#0000FF") 
            
            if semi_auto_button.value is False:
                draw.text((0, 90), "Semi-Auto Mode", font=font2, fill="#0000FF") 

            if iot_button.value is False:
                draw.text((0, 90), "IoT Mode", font=font2, fill="#0000FF") 
            
            #print(button_manual.value)

            if float(Temp2) > 50:
                #y += font.getsize("OVERHEATING")[1]
                #draw.text((x+5, y+20), "OVERHEATING", font=font2, fill="#0000FF")  
                #GPIO.output(output_pin, curr_value)
                #curr_value ^= GPIO.HIGH
                #curr_value = GPIO.LOW
                output_pin.value = False
                y += font.getsize("OVERHEATING")[1]
                draw.text((x+5, y+8), "OVERHEATING", font=font2, fill="#0000FF") 
                #time.sleep(15) 
                #print(button_state.value)
                if button_state.value is True:
                    print("exiting")
                    #GPIO.cleanup()  
                    exit()
                time.sleep(5)      
            
            else:
                
                #GPIO.output(output_pin, GPIO.HIGH)
                output_pin.value = True
                disp.image(image)
                #x = GPIO.input(15)
                #print(button_state.value)
                if button_state.value is True:
                    print("exiting")
                    #GPIO.cleanup()  
                    exit()
                #time.sleep(5) 

            disp.image(image)
            time.sleep(.1)
    
    
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()