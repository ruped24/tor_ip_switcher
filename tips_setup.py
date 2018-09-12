#! /usr/bin/env python2
#
# Configuration tool for tor_ip_switcher /etc/tor/torrc
#
# Usage: tips_setup.py <your_new_password>
#
# By Rupe 08.21.2018

from __future__ import print_function, unicode_literals

from commands import getoutput
from os import geteuid
from subprocess import call
from os.path import basename, isfile
from sys import argv

ControlHashedPassword = ''.join(
    getoutput('tor --hash-password "%s"' % ''.join(argv[1:])).split()[-1:])


def controlPort_setup():
  call(["sed", "-i", "/ControlPort /s/^#//", "/etc/tor/torrc"])
  call(["sed", "-i", "/HashedControlPassword /s/^#//", "/etc/tor/torrc"])


def controlHashed_password():
  call([
      "sed", "-i",
      "s/^HashedControlPassword 16:.*[A-Z0-9]/HashedControlPassword %s/" %
      ControlHashedPassword, "/etc/tor/torrc"
  ])


def reload_tor_config():
  tor_running = getoutput('pidof tor')
  if tor_running:
    call(['kill', '-HUP', '%s' % tor_running])
    print("\n \033[92m[" + u'\u2714' + "]\033[0m Tor Config: Reloaded")
  else:
    print("\n \033[91m[" + u'\u2718' + "]\033[0m Tor Daemon: Not running")


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
        print(" \033[92m[" + u'\u2714' + "]\033[0m ControlPort 9051: Enabled\n",
              "\033[92m[" + u'\u2714' +
              "]\033[0m HashedControlPassword: Enabled\n", "\033[92m[" +
              u'\u2714' + "]\033[0m /etc/tor/torrc: Updated successfully\n",
              "\033[92m[" + u'\u2719' +
              "]\033[0m Password set to: %s\n" % ''.join(argv[1:]),
              "\033[92m[" + u'\u2719' +
              "]\033[0m HashedControlPassword: %s\n" % ControlHashedPassword)
      else:
        exit("\033[91m[!]\033[0m /etc/tor/torrc missing.")
    except Exception as err:
      print(err)
