#!/usr/bin/env python3

# Import libraries

import os

# Declaration of variables

### Read user input here into a variable
userInput = input("Please enter the filepath for your chosen directory.\n")
# Declaration of functions

### Declare a function here

def walker(userInput):
  for (root, dirs, files) in os.walk(userInput):
      ### Add a print command here to print ==root==
      print(root)
      ### Add a print command here to print ==dirs==
      print(dirs)
      ### Add a print command here to print ==files==
      print(files)

# Main
walker(userInput)

### Pass the variable into the function here

# End