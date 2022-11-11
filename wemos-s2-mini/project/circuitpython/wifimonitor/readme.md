# WiFi Monitor

* detect up to 28 devices via network ping
* upload result to thingspeak.com

## setup thinkspeak

* create account and channel
* add field 1..7 for devices
* add field 8 for accesspoint

example:
* field1: Bob = 1 SmartphoneA, 2 SmartphoneB
* field2: Mom = 1 SmartphoneC
* field3: Dad = 1 SmartphoneD
* field4: PC = 1 Mom, 2 Dad, 3 Bob
* field5: TV = 1 Netflix, 2 Amazon Prime
* field8: WiFi = 1 Base, 2 SndFloor

The device id must 1,2,4 or 8 and the result added, 
e.g. Field1 = 3, if 1 + 2 exists 
