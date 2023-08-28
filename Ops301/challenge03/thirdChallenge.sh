#!/bin/bash

pwd

printf "Please enter a relative directory path.\n"
read drp

printf "Please enter the permissions code to set\n"
read prm

chmod -R $prm $drp

ls -l $drp