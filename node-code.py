import sys
import urllib2
import Adafruit_DHT
from time import sleep
while True:
 #   try:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
        if humidity is not None and temperature is not None:
                print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, $
        else:
                print('Failed to get reading. Try again!')
                sys.exit(1)

#    except:
#        print 'exiting'
#        break

        baseURL = 'https://api.thingspeak.com/update?api_key=NIJ4S43M2TRE69UN'

        f = urllib2.urlopen(baseURL +"&field1=%s&field2=%s" % (humidity,tempera$
        print f.read()
        sleep(300)
