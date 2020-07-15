#!/usr/bin/env python

import nmap

nm = nmap.PortScanner() 
network_subnet = '10.9.9.0/24'

hosts = nm.scan(hosts=network_subnet, arguments='-sP') 

for k,v in hosts['scan'].items(): 
    if str(v['status']['state']) == 'up':
        print(str(v))
        try:    
            print(str(v['addresses']['ipv4']) + ' => ' + str(v['addresses']['mac']))
        except: 
            print(str(v['addresses']['ipv4']))
