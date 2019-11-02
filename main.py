import requests
import http.client as hp
import urllib
import time
import random

import time
 

sleep = 15
key = '9R2KET2RLKDC7RCX'

def update_val(heartbeat,temp):
    # params = urllib.parse.urlencode({'field1': heartbeat, 'key':key }) 
    # headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    # conn = hp.HTTPConnection("api.thingspeak.com:80")
    # try:
    #     conn.request("POST", "/update", params, headers)
    #     response = conn.getresponse()
    #     print (heartbeat,temp)
    #     print (response.status, response.reason)
    #     data = response.read()
    #     conn.close()
    # except:
    #     print( "connection failed")
    url = "https://api.thingspeak.com/update"
    params={'api_key':key, 'field1':heartbeat}
    r = requests.get(url, params)
    data = r.json()
    print(data)
    

if __name__ == "__main__":
    import serial
    ser = serial.Serial('/dev/ttyACM0',115200) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
    while True:
        line = ser.readline()
        line = line.decode('ascii').strip()
        print(line.split(','))
        # update_val(line[1],line[3])
        time.sleep(1)
        
