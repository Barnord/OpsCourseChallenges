#!/usr/bin/python

import os
from cryptography.fernet import Fernet

path = ""

def makeKey():
  key = Fernet.generate_key()
  with open("key.key", "wb") as kFile:
    kFile.write(key)


def fEncrypt():
  path = input(f'Please enter a filepath relative to {os.system("pwd")}:\n')
  with open(path, "rb") as file:
    data = file.read()
  encrypted = crypt.encrypt(data)

  with open(path, "wb") as file:
    file.write(encrypted)
  
  return path


def fDecrypt():
  global path
  if path != "":
    res = input("Use last file encrypted? y/n\n")
    if res == "n":
      path = input(f'Please enter a filepath relative to {os.system("pwd")}:\n')

  with open(path, "rb") as file:
    encrypted = file.read()
    decrypted = crypt.decrypt(encrypted.encode)
  
  with open(path, "wb") as file:
    file.write(decrypted)
  

def mEncrypt():
  message = input("Enter a message to encrypt.\n").encode()
  return crypt.encrypt(message)

def mDecrypt():
  global message
  crypt.decrypt(message)

makeKey()
crypt = Fernet(open("key.key", "rb").read())

menu = ["Please select a menu item.", "1. Encrypt a file", "2. Decrypt a file", "3. Encrypt a message", "4. Decrypt a message."]

for item in menu:
  print(item)
sel = input()

if sel=="1":
  path = fEncrypt()
elif sel=="2":
  fDecrypt()
elif sel=="3":
  message = mEncrypt()
elif sel=="4":
  mDecrypt()
else:
  print("Goodbye.")