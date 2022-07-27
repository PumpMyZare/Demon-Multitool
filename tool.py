#Python Port Scanner
import sys
import time
import os
target = input("Enter Targets IP: ")
os.system("nmap " + target)
