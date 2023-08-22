#!/bin/bash

login_history() {
  last
  if [ -n "$1" ]
    then
      echo "Your argument is $1"
  fi
  echo "This is the login history"
}

login_history "very good"
login_history
login_history