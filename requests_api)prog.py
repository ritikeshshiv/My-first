import requests
while(1):
    temp=int(input("Enter temp"))
    hum=int(input("Enter hum"))
    moi=int(input("Enter moisture"))
    dis=int(input("Enter distance"))
    s=requests.get('https://api.thingspeak.com/update?api_key=V27GAISGUE097QFA&field1={}&field2={}&field3={}&field4={}'.format(temprature,hum,moisture,dis))
    print("values updated successfully..!!!")
