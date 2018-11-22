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
from os.path import basename, isfile
from subprocess import call
from sys import argv, stdout
from time import sleep

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
      info = \
      """
      [\033[93m\u003F\033[0m] Gathering torrc config information [\033[93m\u003F\033[0m]
      """
      if isfile('/etc/tor/torrc'):
        if 'HashedControlPassword' not in open('/etc/tor/torrc').read():
          exit("\033[91m[!]\033[0m HashedControlPassword not in /etc/tor/torrc.")
        for i in info:
          sleep(.02)
          stdout.write(i)
          stdout.flush()
        controlPort_setup()
        controlHashed_password()
        reload_tor_config()
        print(" \033[92m[" + u'\u2714' + "]\033[0m ControlPort 9051: Enabled\n",
              "\033[92m[" + u'\u2714' +
              "]\033[0m HashedControlPassword: Enabled\n", "\033[92m[" +
              u'\u2714' + "]\033[0m /etc/tor/torrc: Updated successfully\n",
              "\033[92m[" + u'\u2719' + "]\033[0m Password set to: \033[92m" +
              "%s" % ''.join(argv[1:]) + "\033[0m" + "\n",
              "\033[92m[" + u'\u2719' +
              "]\033[0m HashedControlPassword %s\n" % ControlHashedPassword)
      else:
        exit("\033[91m[!]\033[0m /etc/tor/torrc missing.")
    except Exception as err:
      print(err)
