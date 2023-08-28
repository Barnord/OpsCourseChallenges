#!/bin/bash

numbers=('1' '2' '3' '4')

for i in "${numbers[@]}"; do
  mkdir dir$i
  touch dir$i/txt$i.txt
done