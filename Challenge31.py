#!/usr/bin/python

# Pair programmed
# Driver: Ben Arno
# Navigator: Kevin Isaac

#Imports
import os
from sys import platform
#Ops401, Challenge2.py
def linuxSearch(file, dir):
  # TODO: Search each file in the directory by name
  os.system(f"find -wholename {dir}, {file}")
  # TODO: For each positive detection, print to the screen the file name and location
  # TODO: At the end of the search process, print to the screen how many files were searched and how many hits were found.
  print("linux")
def windowsSearch(file, dir):
  # TODO: Search each file in the directory by name
  # TODO: For each positive detection, print to the screen the file name and location
  # TODO: At the end of the search process, print to the screen how many files were searched and how many hits were found.
  print("windows")

# DONE: Prompt the user to type in a file name to search for
fName = input("Please enter a filename:\n")

# DONE: Prompt the user for a directory to search in
dName = input("Please enter the directory to search:\n")

if platform == "linux" or platform =="linux2":
  linuxSearch(fName, dName)
elif platform == "win32":
  windowsSearch(fName, dName)
