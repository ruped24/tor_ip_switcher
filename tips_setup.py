#! /usr/bin/env python2
#
# Configuration tool for tor_ip_switcher /etc/tor/torrc
#
# By Rupe 08.21.2018

from __future__ import print_function, unicode_literals

from commands import getoutput
from os import system
from os.path import basename
from sys import argv

ControlHashedPassword = ''.join(
    getoutput('sudo tor --hash-password "%s"' % argv[1:]).split()[-1:])


def controlPort_setup():
  system("sudo sed -i '/ControlPort /s/^#//' /etc/tor/torrc")
  system("sudo sed -i '/HashedControlPassword /s/^#//' /etc/tor/torrc")


def controlHashed_password():
  system(
      "sudo sed -i 's/^HashedControlPassword 16:.*[A-Z0-9]*$/HashedControlPassword %s /' /etc/tor/torrc"
      % ControlHashedPassword)


if __name__ == '__main__':
  if argv[1:] == list():
    exit(" \n[!] Usage: %s <your_new_password>\n" % basename(__file__))
  else:
    try:
      controlPort_setup()
      controlHashed_password()
      print(
          "\n \033[92m[" + u'\u2714' + "]\033[0m ControlPort: Enabled\n",
          "\033[92m[" + u'\u2714' + "]\033[0m ControlHashedPassword: Enabled\n",
          "\033[92m[" + u'\u2714' +
          "]\033[0m /etc/tor/torrc updated successfully!\n", "\033[92m[" +
          u'\u2719' + "]\033[0m Password set to: %s\n" % ''.join(argv[1:]),
          "\033[92m[" + u'\u2719' +
          "]\033[0m ControlHashedPassword: %s\n" % ControlHashedPassword)
    except Exception as err:
      print(err)