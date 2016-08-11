import sys
import urllib2
import Adafruit_DHT
from time import sleep
import datetime

while 1:
 #   try:       
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
        if humidity is not None and temperature is not None:
                print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
                date='{:%Y-%m-%d+%H:%M:%S}'.format(datetime.datetime.now())
        else:
                print('Failed to get reading. Try again!')
                sys.exit(1)


        baseURL = 'http://necbig.comli.com/send_node_data/node.php?nodeID=1'

        f = urllib2.urlopen(baseURL +"&hum=%s&temp=%s&dtime=" % (humidity,temperature)+"'{:%Y-%m-%d+%H:%M:%S}'".format(datetime.datetime.now()))
        print f.read()
        sleep(30)
#    except:
#       print 'exiting'
#       break   
