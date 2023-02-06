#!/usr/bin/python

import time
import getpass

def theThing():
  global path
  doc = open(path)
  line = doc.readline()

  while line:
    line.rstrip()
    print(line)
    time.sleep(1)
    line = doc.readline()
  doc.close()

def otherThing():
  pswd = getpass.getpass("Please enter password to be checked\n")
  global path
  doc = open(path).read()
  print(pswd in doc)

path = input("Please enter the path to the dictionary\n")
otherThing()