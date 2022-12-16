#!/bin/bash

# Create a bash script that launches a menu system with the following options:

dumb=$'Please enter the number that corresponds with your choice.\n1. \"Hello world\"\n2. Ping self\n3. IP info\n4. Exit'
echo "$dumb"


while [[ "$userInput" != 4 ]]
do
  read userInput
  case $userInput in
    # Hello world (prints “Hello world!” to the screen)
    1)
      echo "Hello world!"
      ;;
    # Ping self (pings this computer’s loopback address)
    2)
      ping -c1 loopback
      ;;
    # IP info (print the network adapter information for this computer)
    3)
      ip a
      ;;
    # Exit
    4)
      ;;
    *)
      echo -n "Unrecognized response."
      userInput=5
      ;;
  esac
  echo 
  echo "Action completed."
  echo "$dumb"
done
# Next, the user input should be requested.
# The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
# Use a loop to bring up the menu again after the request has been executed.