
def ultrasonic():
    
    import RPi.GPIO as a
    import time

    a.setwarnings(False)
    a.setmode(a.BOARD)
    a.setup(7,a.OUT)
    a.setup(11,a.IN)

    trig,echo=7,11

    a.output(trig,1)
    time.sleep(0.00001)
    a.output(trig,0)
    while(a.input(echo)==0):
        pass
    t1=time.time()
    while(a.input(echo)==1):
        pass
    t2=time.time()
    T=t2-t1
    s=17150*T
    ss= round(s,2)
    print('the object is available at',ss, 'cm')
    return ss


#dis=ultrasonic()
#print(dis)
