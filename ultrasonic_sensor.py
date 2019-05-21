import RPi.GPIO as a
import time
import requests
import sys
import Adafruit_DHT
import time


pin=27
trig=7
echo=11
channel=37
rain=23

sensor=Adafruit_DHT.DHT11
a.setmode(a.BOARD)
a.setmode(a.BOARD)
a.setup(channel,a.IN)
a.setup(trig,a.OUT)
a.setup(echo,a.IN)


def ultrasonic():
    print("fsajhjads")
    a.output(trig,True)
    time.sleep(0.00001)
    a.output(trig,False)

    while a.input(echo)==0:
        print("dchhgd")
        pass
    pulse_start=time.time()

    while a.input(echo)==1:
        print("gd")
        pass
    pulse_end=time.time()

    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    return distance
    #print("Distance",distance,"cm")


def rain():
    if (state == 0):
        print ("Water detected!")
        return 1
    else:
        print ("Water not detected")
        return 0


def dht():
    while True:
        hum, temp=Adafruit_DHT.read_retry(11,pin)
        print('Temp:{0:0.1f}*C Humidity: {1:0.1f}%'.format(temp,hum))
        return hum,temp



def soil():
    def callback(channel):
        if a.input(channel):
            print("no water")
        else:
            print("water")
    a.add_event_detect(channel,a.BOTH,bouncetime=300)
    a.add_event_callback(channel,callback)
    while True:
        time.sleep(1)


        
mois=soil()        
hum,temp=dht()
dis=ultrasonic()
drop=rain()
'''
dis=ultrasonic()
temp,hum,mois,dis=66,24,52,dis

print(dis)
print(hum)
print(temp)
print(mois)

requests.get('https://api.thingspeak.com/update?api_key=MS2T0N4Q72WUOMXS&field1={}&field2={}&field3={}&field4={}'.format(temp,hum,mois,dis))
print("doneee!!")






