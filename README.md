Simple raspberry pi pico DC motor robot with camera.

![Alt text](/pictures/robot.jpg "")

# Intro

This is a simple wifi/http/websocket based robot.
Web page serves a simple joystick that controls power of wheels and with that direction. (move joystick further, more power, left to turn left, right likewise)
Page works well on mobile, can be improved by using game controller API to have an actual playstation/xbox controller connected to the webpage for more fun.

# How to set up software once built

Set up micropython on pico (use the firmware for 'Raspberry Pi Pico W (with urequests and upip preinstalled)')
URL https://www.raspberrypi.com/documentation/microcontrollers/micropython.html

Update 'src/config.py' with your SSID and password.
Copy all files from src to pico. (you can use thonny for this)

Run webserver.py code with Thonny. (or rename to main.py and let pico run on each reboot)
It will print the IP address it obtains once it starts up. You can also obtain the IP address from your router and ideally assign a DNS and static IP.

If you copy files and rename webserver.py to main.py you might have issues reconnecting thonny, to fix that you will need flash_nuke.uf2 from utils and reflash micropython / copy files again

# Parts used:

a. Raspberry pi pico
- https://www.kiwi-electronics.com/nl/raspberry-pi-pico-w-10938?search=raspberry%20pi%20pico


b. DRV8833 
- https://www.adafruit.com/product/3297 or https://www.amazon.nl/gp/product/B08GM2XLMD/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1

c. Motors and wheels
- https://www.amazon.nl/gp/product/B0BHSLNJYN/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1

d. JST connectors or regular cables as per preference

https://www.amazon.nl/-/en/dp/B08JVC4LVG/ref=sr_1_17?crid=2LI3SQEAV8F06&keywords=jst+connector&qu=eyJxc2MiOiI0LjY5IiwicXNhIjoiNC40NCIsInFzcCI6IjQuMjcifQ%3D%3D&sprefix=jst+connector%2Caps%2C92&sr=8-17
https://www.amazon.nl/-/en/dp/B07KYHBVR7/ref=sr_1_15?crid=2GCQ7CNPDNBI4&keywords=jumper+wire+raspberry&sprefix=jumper+wire+raspberry%2Caps%2C71&sr=8-15

e. External battery

Any will do as long as it can give ~2A.

f. Fun parts

Wire for power bridge - https://www.amazon.nl/gp/product/B0043DXIA4/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1
Magnetic Charging Cable - microusb (for power, to not have to plug in/out microusb all the time)
standoffs - https://www.amazon.nl/gp/product/B08VD1ZCFJ/ref=ppx_yo_dt_b_asin_title_o06_s01?ie=UTF8&psc=1
Wood parts from general hardware store or just use a plastic box or anything around the house.

# Pico connections

VUSB is connected to a 100 ohm resistor towards ground. (to keep external battery engaged you need to consume at least 50mah)
VUSB is the large metallic wire in pictures

GPIO 12/13 -> input1/2 on first DRV8833
GPIO 14/15 -> input3/4 on first DRV8833
GPIO 16/17 -> input1/2 on second DRV8833
GPIO 18/19 -> input3/4 on second DRV8833

Ground to each DRV8833 ground (helps that there's ground between gpio 13/14 and 17/18)
Power from DRV8833 to the VBUS wire.
