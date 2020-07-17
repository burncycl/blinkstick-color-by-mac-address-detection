from ping3 import ping
from blinkstick import blinkstick
from time import sleep
from webcolors import name_to_rgb 


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

    def discovery(self):
        while True:
            discovered_phones = []
            ips = ['10.3.3.11','10.3.3.12']
            for ip in ips:
                response = ping(ip)
                if response is not None:
                    discovered_phones.append(ip)
            self.colors_handler(discovered_phones)


    def colors_handler(self, discovered_phones):
        print(discovered_phones) # Debugging
        if len(discovered_phones) == 1:
            led_start = 0
            led_end = 8
            if '10.3.3.11' in discovered_phones:
                color = 'blue'
                self.display_colors(led_start, led_end, color)
            elif '10.3.3.12' in discovered_phones:
                color = 'orange'
                self.display_colors(led_start, led_end, color)
        elif len(discovered_phones) == 2:
            if '10.3.3.11' in discovered_phones:
                color = 'blue'
                led_start = 0
                led_end = 4
                self.display_colors(led_start, led_end, color)
            if '10.3.3.12' in discovered_phones:
                color = 'orange'
                led_start = 4
                led_end = 8
                self.display_colors(led_start, led_end, color)


    def display_colors(self, led_start, led_end, color):
        (r, g, b) = name_to_rgb(color)
        for led in range(led_start, led_end):
            for bstick in self.bsticks:
                try:                    
                    bstick.pulse(0, led, r, g, b)
                except Exception as e:
                    print('ERROR - {}'.format(e))
                    
    def clear(self):
        for bstick in self.bsticks:
            for i in range(self.led_start, self.led_end):
                bstick.set_color(0, i, 0, 0, 0)
                
                
BlinkStrip_obj = BlinkStrip()
BlinkStrip_obj.clear()
BlinkStrip_obj.discovery()
