#! /usr/bin/env python2
"""
tor_switcher.py reloaded and refactored by Rupe to work with toriptables2.py.
tor_ip_switcher.py is a light GUI interface for issuing NEWNYM signals over TOR's control port.
Useful for making any DoS attack look like a DDoS attack.
"""

from commands import getoutput
from json import load
from random import random
from ScrolledText import ScrolledText
from telnetlib import Telnet
from thread import start_new_thread
from time import localtime, sleep
from Tkinter import *
from tkMessageBox import showerror
from urllib2 import URLError, urlopen


class Switcher(Tk):

  def __init__(self):
    Tk.__init__(self)
    self.resizable(0, 0)
    self.title(string=".o0O| TOR IP Switcher |O0o.")

    self.host = StringVar()
    self.port = IntVar()
    self.passwd = StringVar()
    self.time = DoubleVar()

    self.host.set('localhost')
    self.port.set('9051')
    self.passwd.set('')
    self.time.set('30')

    Label(self, text='Host:').grid(row=1, column=1, sticky=E)
    Label(self, text='Port:').grid(row=2, column=1, sticky=E)
    Label(self, text='Password:').grid(row=3, column=1, sticky=E)
    Label(self, text='Interval:').grid(row=4, column=1, sticky=E)

    Entry(self, textvariable=self.host).grid(row=1, column=2, columnspan=2)
    Entry(self, textvariable=self.port).grid(row=2, column=2, columnspan=2)
    Entry(self, textvariable=self.passwd, show='*').grid(
          row=3, column=2, columnspan=2)
    Entry(self, textvariable=self.time).grid(row=4, column=2, columnspan=2)

    Button(self, text='Start', command=self.start).grid(row=5, column=2)
    Button(self, text='Stop', command=self.stop).grid(row=5, column=3)

    self.output = ScrolledText(
        self,
        foreground="white",
        background="black",
        highlightcolor="white",
        highlightbackground="purple",
        wrap=WORD,
        height=8,
        width=40)
    self.output.grid(row=1, column=4, rowspan=5, padx=4, pady=4)

  def start(self):
    self.write('TOR Switcher starting.')
    self.ident = random()
    start_new_thread(self.newnym, ())

  def stop(self):
    try:
      self.write('TOR Switcher stopping.')
    except:
      pass
    self.ident = random()

  def write(self, message):
    t = localtime()
    try:
      self.output.insert(END,
                         '[%02i:%02i:%02i] %s\n' % (t[3], t[4], t[5], message))
      self.output.yview(MOVETO, 1.0)
    except:
      print('[%02i:%02i:%02i] %s\n' % (t[3], t[4], t[5], message))

  def error(self):
    showerror('TOR IP Switcher', 'Tor daemon not running!')

  def newnym(self):
    key = self.ident
    host = self.host.get()
    port = self.port.get()
    passwd = self.passwd.get()
    interval = self.time.get()

    try:
      telnet = Telnet(host, port)
      if passwd == '':
        telnet.write("AUTHENTICATE\r\n")
      else:
        telnet.write("AUTHENTICATE \"%s\"\r\n" % (passwd))
      res = telnet.read_until('250 OK', 5)

      if res.find('250 OK') > -1:
        self.write('AUTHENTICATE accepted.')
      else:
        self.write('Control responded,' + "\n"
                   'Incorrect password: "%s"' % (passwd))
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
            my_new_ident = load(urlopen('http://ident.me/.json'))['address']
          except URLError:
            my_new_ident = getoutput('wget -qO - v4.ifconfig.co')
          self.write('Your IP is %s' % (my_new_ident))
        else:
          key = self.ident + 1
          self.write('Quitting.')
        sleep(interval)
      except Exception, ex:
        self.write('There was an error: %s.' % (ex))
        key = self.ident + 1
        self.write('Quitting.')

    try:
      telnet.write("QUIT\r\n")
      telnet.close()
    except:
      pass


if __name__ == '__main__':
  mw = Switcher()
  mw.mainloop()
  mw.stop()
