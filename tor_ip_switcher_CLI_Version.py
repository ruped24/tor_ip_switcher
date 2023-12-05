#!/usr/bin/env python2
"""
tor_switcher.py reloaded and refactored by Rupe to work with toriptables2.py.
tor_ip_switcher.py is a light interface for issuing NEWNYM signals over TOR's control port.
Useful for making any DoS attack look like a DDoS attack.
"""

from getpass import getpass
from json import load
from telnetlib import Telnet
from time import sleep
from random import random
from urllib2 import URLError, urlopen

class TorSwitcher:

    def __init__(self, host='localhost', port=9051):
        self.host = host
        self.port = port
        self.interval = self.get_interval()
        self.ident = random()

        # Prompt user for password securely
        self.passwd = getpass("Enter Tor Control Port Password: ")

    def get_interval(self):
        while True:
            try:
                interval = int(input("Enter the interval for IP change in seconds: "))
                if interval > 0:
                    return interval
                else:
                    print("Please enter a positive interval.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def start(self):
        print('TOR Switcher starting.')
        self.newnym()

    def stop(self):
        print('TOR Switcher stopping.')
        self.ident = random()

    def write(self, message):
        print(message)

    def error(self):
        print('Tor daemon not running!')

    def newnym(self):
        key = self.ident
        host = self.host
        port = self.port
        passwd = self.passwd
        interval = self.interval

        try:
            telnet = Telnet(host, port)
            telnet.write("AUTHENTICATE \"%s\"\r\n" % passwd)
            res = telnet.read_until('250 OK', 5)

            if res.find('250 OK') > -1:
                self.write('AUTHENTICATE accepted.')
            else:
                self.write('Control responded,' + "\n"
                           'Incorrect password.')
                key = self.ident + 1
                self.write('Quitting.')
        except Exception:
            self.write('There was an error!')
            self.error()
            key = self.ident + 1
            self.write('Quitting.')

        while key == self.ident:
            try:
                telnet.write("signal NEWNYM\r\n")
                res = telnet.read_until('250 OK', 5)
                if res.find('250 OK') > -1:
                    try:
                        my_new_ident = load(urlopen('https://check.torproject.org/api/ip'))
                        self.write('Your IP is %s' % my_new_ident['IP'])
                    except (URLError, ValueError):
                        my_new_ident = getoutput('wget -qO - ifconfig.me')
                        self.write('Your IP is %s' % my_new_ident)
                else:
                    key = self.ident + 1
                    self.write('Quitting.')
                sleep(interval)
            except Exception as ex:
                self.write('There was an error: %s.' % ex)
                key = self.ident + 1
                self.write('Quitting.')

        try:
            telnet.write("QUIT\r\n")
            telnet.close()
        except:
            pass

if __name__ == '__main__':
    switcher = TorSwitcher()
    switcher.start()
