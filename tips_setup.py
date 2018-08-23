#! /usr/bin/env python2
#
# Configuration tool for tor_ip_switcher /etc/tor/torrc
#
# By Rupe 08.21.2018

from __future__ import print_function, unicode_literals

from commands import getoutput
from os import geteuid, system
from os.path import basename, isfile
from sys import argv

ControlHashedPassword = ''.join(
    getoutput('tor --hash-password "%s"' % ''.join(argv[1:])).split()[-1:])


def controlPort_setup():
  system("sed -i '/ControlPort /s/^#//' /etc/tor/torrc")
  system("sed -i '/HashedControlPassword /s/^#//' /etc/tor/torrc")


def controlHashed_password():
  system(
      "sed -i 's/^HashedControlPassword 16:.*[A-Z0-9]/HashedControlPassword %s/' /etc/tor/torrc"
      % ControlHashedPassword)


def reload_tor_config():
  tor_running = getoutput('pidof tor')
  if tor_running:
    system('kill -HUP $(pidof tor)')
    print("\n \033[92m[" + u'\u2714' + "]\033[0m Tor config: Reloaded")
  else:
    print(str())


if __name__ == '__main__':
  if geteuid() is not 0:
    exit('Run as super user!')
  if argv[1:] == list():
    exit(" \n[!] Usage: %s <your_new_password>\n" % basename(__file__))
  else:
    try:
      if isfile('/etc/tor/torrc'):
        controlPort_setup()
        controlHashed_password()
        reload_tor_config()
        print(" \033[92m[" + u'\u2714' + "]\033[0m ControlPort: Enabled\n",
              "\033[92m[" + u'\u2714' +
              "]\033[0m ControlHashedPassword: Enabled\n", "\033[92m[" +
              u'\u2714' + "]\033[0m /etc/tor/torrc updated successfully!\n",
              "\033[92m[" + u'\u2719' +
              "]\033[0m Password set to: %s\n" % ''.join(argv[1:]),
              "\033[92m[" + u'\u2719' +
              "]\033[0m ControlHashedPassword: %s\n" % ControlHashedPassword)
      else:
        exit("\033[91m[!]\033[0m /etc/tor/torrc missing.")
    except Exception as err:
      print(err)
