import RPi.GPIO as io
import time
import os
from led import *
from rain_sensor import  *
from DHT_sensor import *
from Soil_sensor import *
from motor_prog import * 
import requests



while(1):
    print("Lets begin")


    print("sensing ultrasonic")
    dis=ultrasonic()
    print("sensing DHT11")
    temp,hum = dht()
    rainy=rain()
    mois=soil()
    moto=motor()
    print("So your values are..\nDistance:{}\nTemperature:{}\nHumidity:{}\nRainStatus:{}\nMoisture:{}\nMotor:{}".format(dis,temp,hum,rainy,mois,moto))



requests.get('https://api.thingspeak.com/update?api_key=MS2T0N4Q72WUOMXS&field1={}&field2={}&field3={}&field4={}'.format(temp,hum,mois,dis))
print("doneee!!")

time.sleep(5)





