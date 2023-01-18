#!/usr/bin/python

import subprocess
import time
from datetime import datetime


print("Please enter an IP to ping.")
adrs = input()

while True:
  logs = open('logs.txt', 'a')
  lstPng = subprocess.run(['ping', '-c1', adrs], capture_output=True).returncode
  stamp = datetime.now()
  if lstPng == 0:
    result = f'{stamp}, {adrs}, Network Active'
  else:
    result = f'{stamp}, {adrs}, Oh no.'
  print(result)
  logs.writelines(f'{result}\n')
  time.sleep(2)
