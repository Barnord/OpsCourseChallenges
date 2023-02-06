#!/usr/bin/python

import sys
from scapy.all import IP, ICMP, TCP, sr1

p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
  p.show()