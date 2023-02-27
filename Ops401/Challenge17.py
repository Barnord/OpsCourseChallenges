#!/usr/bin/python

import time
import getpass
import paramiko

def Brute():
  global path
  doc = open(path)
  line = doc.readline()

  while line:
    line = line.rstrip()
    print(line)
    time.sleep(1)
    line = doc.readline()
  doc.close()

def Defend():
  pswd = getpass.getpass("Please enter password to be checked\n")
  global path
  doc = open(path).read()
  print(pswd in doc)

host = input("Where are we going?")
user = input("Who are we going to be?")
password = getpass.getpass("Password:")
port = 22

path = input("Please enter the path to the dictionary\n")

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, port, user, password)