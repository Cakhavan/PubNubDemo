import requests
import json 
import time
import serial


#subscriber format
sub = 'http://pubsub.pubnub.com/subscribe/sub-c-7fe8c6c0-3eba-11e8-afae-2a65d00afee8/ch1/callback/0'

command = 0 

#PySerial Set up
Arduino_Serial = serial.Serial('/dev/cu.usbmodem1411',9600) 


#Command Communication
def func(command):

  if command == 'ON':

     Arduino_Serial.write('1'.encode())
     print("LED ON")

  elif command == 'OFF':

     Arduino_Serial.write('0'.encode())
     print("LED OFF")

 

if __name__ == '__main__':

  while True:

    #Subscribe request (initial)
    subscribe = requests.get(sub)

    #Subscribe request into variable
    read = requests.get('http://pubsub.pubnub.com/subscribe/sub-c-7fe8c6c0-3eba-11e8-afae-2a65d00afee8/ch1/0/' + str(subscribe.content[1]))

    #Jsonify data into an object
    jData = json.loads(read.content)

    #print(jData)
    size = len(jData[0])
    command = jData[0][size-1]

    func(command)

    time.sleep(3)



   
