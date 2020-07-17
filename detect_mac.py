#!/usr/bin/env python

import nmap
from blinkstick import blinkstick
from time import sleep
from webcolors import name_to_rgb 
            
            
class BlinkStrip:
    def __init__(self):
        # Declare variables, not war.
        self.color = ['blue', 'orange']
        self.led_start = 0
        self.led_end = 8
        self.bsticks = []
        self.get_blinksticks()

    def get_blinksticks(self):
        for bstick in blinkstick.find_all():
            self.bsticks.append(bstick)


    def colors_handler(self, discovered_phones):
        print(discovered_phones)
        if len(discovered_phones) == 1:
            led_start = 0
            led_end = 8
            if '44:91:60:C5:20:D1' in discovered_phones:
                color = 'blue'
                self.display_colors(led_start, led_end, color)
            elif '42:3D:C9:CE:23:C0' in discovered_phones:
                color = 'red'
                self.display_colors(led_start, led_end, color)
        elif len(discovered_phones) == 2:
            if '44:91:60:C5:20:D1' in discovered_phones:
                color = 'blue'
                led_start = 0
                led_end = 3
                self.display_colors(led_start, led_end, color)
            if '42:3D:C9:CE:23:C0' in discovered_phones:
                color = 'red'
                led_start = 4
                led_end = 8
                self.display_colors(led_start, led_end, color)


    def display_colors(self, led_start, led_end, color):
        (r, g, b) = name_to_rgb(color)
        for led in range(led_start, led_end):
            for bstick in self.bsticks:
                try:                    
                    bstick.set_color(0, led, r, g, b)
                except Exception as e:
                    print('ERROR - {}'.format(e))
                    
    def clear(self):
        for bstick in self.bsticks:
            for i in range(self.led_start, self.led_end):
                bstick.set_color(0, i, 0, 0, 0)
                  
#     def __del__(self):
#         for bstick in self.bsticks:
#             for i in range(self.led_start, self.led_end):
#                 bstick.set_color(0, i, 0, 0, 0)
 
#BlinkStrip().loop_over_colors()

class DetectMobileDevices:
    def __init__(self):    
        nm = nmap.PortScanner() 
        network_subnet = '10.3.3.0/24'
        self.hosts = nm.scan(hosts=network_subnet, arguments='-sP') 

    def scan(self):
        discovered_phones = []
        b_phone = '44:91:60:C5:20:D1'
        c_phone = '42:3D:C9:CE:23:C0'
        
        for k,v in self.hosts['scan'].items(): 
            print(str(v))
            try:
                ip_address = str(v['addresses']['ipv4'])
                mac_address = str(v['addresses']['mac'])
                print(ip_address)
                print(mac_address)
                if mac_address  == b_phone:
                    print('Found phone!')
                    discovered_phones.append(b_phone)
                if mac_address == c_phone:
                    print('Found phone!')
                    discovered_phones.append(c_phone)                    
            except: 
                print(str(v['addresses']['ipv4']))
        BlinkStrip_obj = BlinkStrip()
        BlinkStrip_obj.clear()
        sleep(1)
        BlinkStrip_obj.colors_handler(discovered_phones)
DetectMobileDevices().scan()        