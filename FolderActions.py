#!/bin/python

import os 
import time


def makedailyfolder(): 

	DailyFolder=time.strftime("%F")
	DailySubFolder=DailyFolder+"/"+"Detected-Faces"
	
	if os.path.exists(DailyFolder) == False: 	
		os.mkdir(DailyFolder)
		os.mkdir(DailySubFolder)
	

def newlog():


        DailyFolder1=time.strftime("%F")
        name='/log.txt'
	name=DailyFolder1+name
	
	if os.path.exists(name) == False: 
		faces = open(name, "w+b")
		faces.write("0,0\n")
		faces.close()


def updatelog(dt, image_scale, haar_scale):

        DailyFolder1=time.strftime("%F")
        name="/log.txt"
        name=DailyFolder1+name

	ourlog = file(name, "a+r")
	data=ourlog.read(2)
	
	clocko=time.strftime("%H:%M:%S")
	outputstring=clocko + "," + str(dt)+" Image_Scale: " +str(image_scale) + " Haar_Scale: " + str(haar_scale) +"\n"
	
	ourlog.write(outputstring)
        ourlog.close()






