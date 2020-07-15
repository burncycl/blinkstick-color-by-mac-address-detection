from blinkstick import blinkstick
from time import sleep
from webcolors import name_to_rgb 


rainbow = ['red',
           'orange',
           'yellow',
           'green',
           'cyan',
           'blue',
           'indigo',
           'purple',
           ]


class BlinkStrip:
    def __init__(self):
        # Declare variables, not war.
        self.led_start = 0
        self.led_end = 8
        self.bsticks = []
        self.get_blinksticks()

    def get_blinksticks(self):
        for bstick in blinkstick.find_all():
            self.bsticks.append(bstick)

    def loop_over_colors(self):
        while True:
            for color in rainbow:
                (r, g, b) = name_to_rgb(color)
                for led in range(self.led_start, self.led_end):
                    for bstick in self.bsticks:
                        error_count = 0
                        while True:
                            try:                    
                                bstick.set_color(0, led, r, g, b)
                                sleep(0.005)
                            except Exception as e:                                
                                print('ERROR - {}'.format(e))
                                error_count += 1
                                if error_count == 4:
                                    print('here')
                                    error_count = 0
                                    self.get_blinksticks()
                                continue
                            break
                  
    def __del__(self):
        for bstick in self.bsticks:
            for i in range(self.led_start, self.led_end):
                bstick.set_color(0, i, 0, 0, 0)


BlinkStrip().loop_over_colors()
