
import sys
from Adafruit_IO import MQTTClient
from Adafruit_IO import Client, Feed

ADAFRUIT_IO_KEY = '9de3934474334c6a895bd9ce1994148c'
ADAFRUIT_IO_USERNAME = 'anjith101'
FEED_ID = 'menu'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#READ FROM FEED
def connected(client):
    
    print('Connected to E-dinate Listening for {0}'.format(FEED_ID))

    client.subscribe(FEED_ID)

def disconnected(client):
    
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
   
    print('Feed {0} received new order: {1}'.format(feed_id, payload))

    B = ('{1}'.format(feed_id, payload))
    print (B)

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.connect()
client.loop_blocking()