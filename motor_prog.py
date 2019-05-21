import RPi.GPIO as io ,time
from Soil_sensor import *
from rain_sensor import *


def motor():

    io.setwarnings(False)
    io.setmode(io.BOARD)
    io.setup(15,io.OUT)
    io.setup(16,io.OUT)
    mois = soil()
    rainy = rain()
    while(mois == 1 and rainy ==1): 
        io.output(15,0)
        time.sleep(1)
        io.output(16,0)
        time.sleep(1)
        print("Motor is OFF")
        return 0

    while(mois == 0 and rainy ==0):
        io.output(15,1)    
        time.sleep(1)
        io.output(16,0)
        time.sleep(1)
        print("Motor is ON")
        return 1
    io.output(15,0)
    time.sleep(1)
    io.output(16,0)
    time.sleep(1)
    return 0
    
##
##moto = motor()
##print(moto)
