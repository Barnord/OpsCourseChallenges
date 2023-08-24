#!/bin/bash

echo "System name:"
hostname

stats=`lshw`

echo "CPU:"
echo $stats | grep "*-cpu" -A 5

echo "RAM"
echo $stats | grep "*-memory" -A 3

echo "Display Adapter"
echo $stats | grep "*-display" -A 10

echo "Network Adapter"
echo $stats | grep "*-network" -A 15

# Inquiring minds knowledgable in bash may look at this and say hey, that's going to work poorly. This is true, but I don't want to run lshw five times and I'm tired of messing with this.