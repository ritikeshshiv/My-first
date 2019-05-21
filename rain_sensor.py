#!/usr/bin/env python
def rain():
    from time import sleep
    import os
    import RPi.GPIO as GPIO


    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(23, GPIO.IN)
    state = GPIO.input(23)

    if (state == 0):
        print ("Rain Water detected!")
        return 1
    else:
        print ("Rain Water not detected")
        return 0
rainy=rain()

