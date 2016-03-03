__author__ = 'Mark Liang'
__email__ = 'mliang@mozilla.com'
__copyright__ = 'Copyright 2016 Mozilla Taiwan. All Rights Reserved'

import RPi.GPIO as GPIO
import time

from firebase import firebase

firebase_url = 'https://rpi-workshop.firebaseio.com/'

myFirebaseRef = firebase.FirebaseApplication(firebase_url, None)
result = myFirebaseRef.put('/', "K0", "off")
print "Start:"

GPIO.setmode(GPIO.BCM)

# K0 = 16
# K1 = 20
# K2 = 21
# K3 = 6
# K4 = 13
# K5 = 19
# K6 = 26
# K7 = 5

inputs = [16, 20, 21, 6, 13, 19, 26, 5]
for x in range(0, 8):
    GPIO.setup(inputs[x], GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    for x in range(0, 8):
        input_state = GPIO.input(inputs[x])
        if input_state == False:
            current = myFirebaseRef.get('/', 'K'+str(x))
            if current == "on":
                myFirebaseRef.put('/', 'K'+str(x), 'off')
            else:
                myFirebaseRef.put('/', 'K'+str(x), 'on')
            print "K"+str(x)+" Pressed"
            time.sleep(0.01)