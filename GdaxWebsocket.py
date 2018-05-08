# GDAX Websocket module to retrieve pricing feeds
# Note that opening the websocket uses a seperate thread
# TODO currently gdax is installed with git repo and ducttape, move to PyPi once new version is released
# https://github.com/danpaquin/gdax-python/pull/260
import gdax, time
from datetime import datetime

# Threading fixes
import json
class Feed(gdax.WebsocketClient):
    def __init__(self, products, channels=['ticker']):
        super().__init__()
        self.products = products
        self.channels = channels
        

    def on_open(self):
        self.url = 'wss://ws-feed.gdax.com/'
        self.last_update = datetime.now()
        self.last_message = {}
        for product in self.products:
            self.last_message[product] = None
    
#    def close(self):
#        # Override to prevent prevent Seg fault, TODO upgrade gdax module version
#        if not self.stop:
#            if self.type == 'heartbeat':
#                self.ws.send(json.dumps({'type':'heartbeat','on':False}))
#            self.on_close()
#            self.stop = True
#            self.thread.join()
#            try:
#                if self.ws:
#                    self.ws.close()
#            except WebSocketConnectionClosedException as e:
#                pass

    def on_close(self):
        #self.thread.join()
        #self.stop = True
        #self.ws.close()
        print('closed web socket')

    def on_message(self, msg):
        self.last_message[msg.get('product_id')] = msg
        # TODO store multiple messages, not just the last one
        print(msg)

    def get_recent_data(self, msg):
        self.last_update = datetime.now()

        return self.last_message



# Unit tests
if __name__ == '__main__':
    
    test_feed = Feed(products = ['LTC-USD', 'BTC-USD', 'ETH-USD'])
    test_feed.start()
    time.sleep(0.25)
    test_feed.close()
