import wifi
import time

from ws_connection import ClientClosedError
from ws_server import WebSocketServer, WebSocketClient

from machine import Pin, PWM

right_forward = [ PWM(Pin(12, Pin.OUT)), PWM(Pin(14, Pin.OUT)) ]
right_back = [ PWM(Pin(13, Pin.OUT)), PWM(Pin(15, Pin.OUT)) ]

left_forward = [ PWM(Pin(16, Pin.OUT)), PWM(Pin(18, Pin.OUT)) ]
left_back = [ PWM(Pin(17, Pin.OUT)), PWM(Pin(19, Pin.OUT)) ]

for i in left_forward:
    i.freq(500)
    i.duty_u16(0)

for i in left_back:
    i.freq(500)
    i.duty_u16(0)

for i in right_forward:
    i.freq(500)
    i.duty_u16(0)

for i in right_back:
    i.freq(500)
    i.duty_u16(0)

    
deadline = time.ticks_add(time.ticks_ms(), 300)

class TestClient(WebSocketClient):
    def __init__(self, conn):
        super().__init__(conn)

    def process(self):
        try:
            msg = self.connection.read()
            if not msg:
                return
            msg = msg.decode("utf-8")
            msg = msg.split("\n")[-2]
            msg = msg.split(" ")
            
            deadline = time.ticks_add(time.ticks_ms(), 300)
            
            for i in left_forward:
                i.duty_u16(int(msg[0]))
            for i in left_back:
                i.duty_u16(int(msg[1]))
            for i in right_forward:
                i.duty_u16(int(msg[2]))
            for i in right_back:
                i.duty_u16(int(msg[3]))
        except ClientClosedError:
            print("Connection close error")
            self.connection.close()
        except e:
            print("exception:" + str(e) + "\n")
                


class TestServer(WebSocketServer):
    def __init__(self):
        super().__init__("index.html", 100)

    def _make_client(self, conn):
        return TestClient(conn)

wifi.run()

server = TestServer()
server.start()
try:
    while True:
        server.process_all()
        if time.ticks_diff(deadline, time.ticks_ms()) < 0:
            for i in left_forward:
                i.duty_u16(0)
            for i in left_back:
                i.duty_u16(0)
            for i in right_forward:
                i.duty_u16(0)
            for i in right_back:
                i.duty_u16(0)
                
            deadline = time.ticks_add(time.ticks_ms(), 100000)
            
except KeyboardInterrupt:
    pass
server.stop()
