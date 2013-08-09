#!/usr/bin/python

"""Parallel Port Interface for Windows in Python

Copyright 2008 Neil Fraser
http://neil.fraser.name/software/lpt/

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__author__ = 'fraser@google.com (Neil Fraser)'

from ctypes import *
inpout = windll.LoadLibrary('INPOUT32.DLL')

# The three standard port addresses
lpt1 = 0x3BC
lpt2 = 0x378
lpt3 = 0x278
# Choose the port to use
lpt = 0xD010
# Data byte:     lpt + 0
# Feedback byte: lpt + 1
# Control byte:  ltp + 2

# Read one byte from the port address.  Returns 0-255
def getByte(port):
  return inpout.Inp32(port)

# Send one byte to the port address.
def setByte(port, value):
  return inpout.Out32(port, value)

# Read one bit (0-7) from the port address.  Returns 0-1
def getBit(port, bit):
  if (getByte(port) & 2 ** bit) == 0:
    return 0
  else:
    return 1

# Send one bit (0-7) of a value (0-1) to the port address.
def setBit(port, bit, value):
  byte = getByte(port)
  mask = 2 ** bit
  if value == 0:
    byte = byte & (mask ^ 255)
  else:
    byte = byte | mask
  setByte(port, byte)

def test():
  print "Setting port byte to 5"
  setByte(lpt, 5)
  print "Getting port byte: %d" % getByte(lpt)
  for x in range(0, 8):
    print "Getting bit %d: %d" % (x, getBit(lpt, x))
  print "Setting bit 2 to 0"
  setBit(lpt, 2, 0)
  print "Setting bit 3 to 1"
  setBit(lpt, 3, 1)
  print "Getting port byte: %d" % getByte(lpt)
  for x in range(0, 8):
    print "Getting bit %d: %d" % (x, getBit(lpt, x))

#if __name__ == "__main__":
#  test()

