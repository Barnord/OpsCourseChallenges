#!/bin/bash

echo "Please enter the name of the file or directory you would like to make."
read -r name

if [[ $name == *.* ]]; then
  touch $name
else
  mkdir $name
fi
