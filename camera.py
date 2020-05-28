#!/usr/bin/python
from picamera import PiCamera
from time import sleep
import datetime as dt
import sys
import subprocess
import os

BUCKET = "s3://your-sws-s3-bucket-here/"
SRC_DIR = "/home/pi/Desktop/images/"
DEST = BUCKET + "sub-folder-in-your-bucket-here/"
CURRENT_DATE = dt.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
IMAGE_NAME = dt.datetime.now().strftime('%m%d%Y%H%M%S')

camera = PiCamera()

camera.resolution = (600, 600)
camera.framerate = 15
camera.start_preview()
camera.annotate_text = CURRENT_DATE

sleep(10)
camera.capture('/home/pi/Desktop/images/'+IMAGE_NAME+'.jpg')
camera.stop_preview()

CMD = "s3cmd put --acl-public %s/*.* %s" % (SRC_DIR, DEST)
subprocess.call(CMD, shell=True)

os.remove('/home/pi/Desktop/images/'+IMAGE_NAME+'.jpg')
