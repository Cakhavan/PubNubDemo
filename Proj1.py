import requests
import json 


command = 0 


if __name__ == '__main__':

  while True:

    #user input
    command = input("what is you command \n")
    type(command)


    #publish request
    publish = requests.get('http://pubsub.pubnub.com/publish/pub-c-379c2e9b-8ffd-43b8-b2d6-ee3c2f0fbf31/sub-c-7fe8c6c0-3eba-11e8-afae-2a65d00afee8/0/ch1/0/%22' + str(command) + '%22')
    

   

    #V V V SETTING UP A SUBSCRIBER V V V 
    #############################################################################################################################################################################################

    #subscriber format
    sub = 'http://pubsub.pubnub.com/subscribe/sub-c-7fe8c6c0-3eba-11e8-afae-2a65d00afee8/ch1/callback/0'


    #subscribe request (initial)
    subscribe = requests.get(sub)


    #subscribe request
    read = requests.get('http://pubsub.pubnub.com/subscribe/sub-c-7fe8c6c0-3eba-11e8-afae-2a65d00afee8/ch1/0/' + str(subscribe.content[1]))

    #jsonify into object
    jData = json.loads(read.content)

    #print(jData)