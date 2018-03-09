  var five = require ('johnny-five');
 var board = new five.Board();

var PubNub = require('pubnub')




    board.on("ready", function(){
   var led_green = new five.Led(13);
   var led_red = new five.Led(3);
 pubnub = new PubNub({
		
		publishKey : 'pub-c-2d8f55f6-daa7-467b-923b-6a1e6570c9fc',
        subscribeKey : 'sub-c-1575c412-2116-11e8-a7d0-2e884fd949d2',
               
                    });


               
                    pubnub.addListener(
                    {
                        
                         message: function(message) 
                         {
                            
                            if(message.message=='GREEN'){
                             	publish("GREEN LED IS ON");

                                led_red.off();
                                led_green.on();

                                console.log("GREEN LED IS ON!", message);

                            }else if(message.message=='RED'){
                                publish("RED LED IS ON");  

                                led_green.off();
                                led_red.on();

                                console.log("RED LED IS ON!", message);

                            }else if(message.message == 'BOTH'){
                                publish("BOTH LEDS ARE ON");

                                led_green.on();
                                led_red.on();

                                console.log("BOTH LEDS ARE ON");

                            }else if(message.message == 'OFF'){
                                publish("BOTH LEDS ARE OFF");
                                
                                led_green.off();
                                led_red.off();

                                console.log("BOTH LEDS ARE OFF");
                            }

                              }   
                         
                         
                    });    
                 
    console.log("Subscribing");
    pubnub.subscribe({
        channels: ['ch1'] 
       

    });

   
   
function publish(x){
             

                     var publishConfig = 
                     {
                        channel : "ch2",
                        message : x
                     }
                     pubnub.publish(publishConfig, function(status, response) 
                     {
                     console.log(status, response);

                     });

                 
                        };
   
});