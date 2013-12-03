#!/usr/bin/python


import os 
import subprocess
subprocess.call("sudo rm -r 2013-12-02", shell=True)

subprocess.call("sudo python ELEC-FaceCloud.py", shell=True)

