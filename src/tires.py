from machine import Pin, PWM

class Tires():
    def __init__(self):
        self.right_forward = [ PWM(Pin(12, Pin.OUT)), PWM(Pin(14, Pin.OUT)) ]
        self.right_back = [ PWM(Pin(13, Pin.OUT)), PWM(Pin(15, Pin.OUT)) ]

        self.left_forward = [ PWM(Pin(16, Pin.OUT)), PWM(Pin(18, Pin.OUT)) ]
        self.left_back = [ PWM(Pin(17, Pin.OUT)), PWM(Pin(19, Pin.OUT)) ]

        for i in self.left_forward:
            i.freq(500)
            i.duty_u16(0)

        for i in self.left_back:
            i.freq(500)
            i.duty_u16(0)

        for i in self.right_forward:
            i.freq(500)
            i.duty_u16(0)

        for i in self.right_back:
            i.freq(500)
            i.duty_u16(0)


    def apply_power(self, left_forward, left_back, right_forward, right_back):
        for i in self.left_forward:
            i.duty_u16(left_forward)

        for i in self.left_back:
            i.duty_u16(left_back)

        for i in self.right_forward:
            i.duty_u16(right_forward)

        for i in self.right_back:
            i.duty_u16(right_back)
