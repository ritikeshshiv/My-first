def soil():

    import RPi.GPIO as gpio
    import time
    #channel=37
    gpio.setmode(gpio.BOARD)
    gpio.setup(37,gpio.IN)

    if gpio.input(37):
        print("no water")
        return 0
    else:
        print("water")
        return 1
##    gpio.add_event_detect(channel,gpio.BOTH,bouncetime=300)
##    gpio.add_event_callback(channel,callback)

##mois = soil()    
##print(mois)
