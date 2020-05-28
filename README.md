# Raspbery Pi Camera Photos Uploaded to AWS S3 Bucket 
Code that takes pictures with the Raspberry Pi camera module and uploads those photos to an S3 bucket

## Raspberry Pi Image

The OS installed on the Raspberry Pi is Raspian https://www.raspberrypi.org/downloads/raspbian/. Create an "images" folder and a "code" folder on the Raspberry Pi desktop and make the images folder writeable. Save the camera.py file into the code folder and make it executable.

Install s3cmd on the Raspberry Pi. To do this, open up the command prompt tool and type sudo apt-get install s3cmd and follow the prompts. It will prompt you to enter in your AWS S3 settings so make sure you have AWS S3 setup before running this. You can view a list if s3cmd commands from https://s3tools.org/s3cmd-howto

## AWS Setup

You will need to setup an S3 bucket on AWS where you want to store the photos. The S3 bucket needs to be viewable for public if you want them accessible view a web page or by a url.

## CRON

To create a scheduled CRON that will run your camera.py script go into the command prompt tool and run crontab -e. Scroll to the bottom and add the following to have your script run every hour during 8am to 6pm. Modify this schedule for your needs.

0 8-18 * * * python /home/pi/Desktop/code/camera.py
