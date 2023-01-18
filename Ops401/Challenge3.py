#!/usr/bin/python

#Imports
import os
import time
import smtplib
import subprocess
import getpass
from decouple import config
from datetime import datetime

# Function Declarations
def checkPing(address):
  png = subprocess.run(['ping', '-c1', address], capture_output=True).returncode
  stmp = datetime.now()
  if png == 0:
    msg = f'{stmp}, {adrs}, Network Active'
  else:
    msg = f'{stmp}, {adrs}, Oh no.'
  return [png, stmp, msg]

def sendMail(pngCd):
  stmp = datetime.now()
  if pngCd == 0:
    msg = f'{stmp} Host at {adrs} is back online'
  elif pngCd == 1:
    msg = f'{stmp} Host at {adrs} is not responding'
  else:
    msg = f'Host at {adrs} gave a different code. That\'s not good.'
  mail.sendmail(user, recipient, msg) # When testing this sent an email, but there was no message or subject.

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()

if os.path.exists("Ops401/.env"):
  # Environment variables, pulled from .env using the python-decouple module installed from pip since WSL (I think) was messing with my access to user environment variables.
  user = config('user', default='')
  passw = config('pass', default='')
else:
  user = input("Please enter a valid gmail address you would like to use\n")
  passw = getpass.getpass("Please enter the password for the gmail address you chose\n")

recipient = input("Please enter a valid destination address for email updates.\n")

mail.login(user, passw)

adrs = input("Please enter an IP to ping.\n")

logs = open('logs.txt', 'a')

crntPng = checkPing(adrs)

while True:
  lstPng = crntPng[0]
  crntPng = checkPing(adrs)

  if lstPng != crntPng[0]:
    sendMail(crntPng[0])

  print(crntPng[2])
  logs.writelines(f'{crntPng[2]}\n')
  time.sleep(2)
