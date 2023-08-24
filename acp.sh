#!/bin/bash

if [[ $# == 3 ]]; then
  echo "Yep that's two."
  git add $1
  git commit -m $2
  git push origin $3
elif [[ $# -gt 3 ]]; then
  echo "More than two."
else
  echo "Invalid number of arugments."
fi
