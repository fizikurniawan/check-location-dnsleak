#!/usr/bin/python3

import sys
import time
import requests
from bs4 import BeautifulSoup as bs
from colorama import Fore, Style


class CheckLocation():
    def __init__(self):
        self.show_author()
        self.progress_bar()
        self.connect_dnsleak() 

    def scrap_dns_leak(self, html):
        soup = bs(html, 'html.parser')
        all_p = soup.find_all('p')
        ip = ''
        location = ''

        for p in all_p:
            if 'from' in p.text:
                location = p.text
                location = location.replace('from', '')

            if 'Hello' in p.text:
                ip = p.text
                ip = ip.replace('Hello ', '')

        try:
            self.show_pretty_ui(ip=ip, location=location)
        except:
            return 'Please, check yout connection!'


    def connect_dnsleak(self):
        url = 'https://dnsleaktest.com/'
        html = requests.get(url)
        
        self.scrap_dns_leak(html.content)

    def show_pretty_ui(self, **kwargs):
        ip_addr = "Your Public IP Address: {}".format(kwargs['ip'])
        location = "Your location: {}".format(kwargs['location'])
        
        print("", end = '\n')
        print("", end = '\n')
        print("[%s]" % ("+" * 40), end = '\n')
        print(ip_addr)
        print(location)
        print("[%s]" % ("+" * 40), end = '\n')

    def progress_bar(self):
        toolbar_width = 40

        # setup toolbar
        sys.stdout.write(Fore.GREEN+"Gathering Information \n")
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

        for i in range(toolbar_width):
            time.sleep(0.1) # do real work here
            # update the bar
            sys.stdout.write("-")
            sys.stdout.flush()

        sys.stdout.write("]\n") # this ends the progress bar
    
    def show_author(self):
        print('Author   : Fizi Kurniawan')
        print('Thx      : https://dnsleaktest.com')
        print('email    : fizi@tux.co.id')

if __name__ == '__main__':
    cl = CheckLocation()
