#!/bin/bash

ps aux

echo "Please enter a PID to kill"
read -r pid

kill $pid