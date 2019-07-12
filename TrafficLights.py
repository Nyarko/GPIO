from gpiozero import LED
from time import sleep

red = LED(17)
yellow = LED(27)
green = LED(22)

red.blink(1, 1)
yellow.blink(2, 2)
green.blink(3, 3)

while True:
    red.on()
    sleep(1)
    yellow.on()
    sleep(1)
    green.on()
    sleep(1)
    red.off()
    sleep(1)
    yellow.off()
    sleep(1)
    green.off()