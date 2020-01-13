from picamera import PiCamera
from time import sleep
import smtplib
import time
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import RPi.GPIO as GPIO
import time

toaddr = 'PiArdTech@gmail.com'
me = 'ruellands@gmail.com'
Subject='alert'

GPIO.setmode(GPIO.BCM)

P=PiCamera()
P.resolution= (1024,768)
P.start_preview()
    
GPIO.setup(23, GPIO.IN)
while True:

	i=GPIO.input(23)
	if i==0:                 #When output from motion sensor is LOW
	print("No Motion...")
	time.sleep(2)
	elif i==1:               #When output from motion sensor is HIGH
	print "Motion..."
       
        #camera warm-up time
        time.sleep(2)
        P.capture('movement.jpg')
        time.sleep(10)
        subject='Security allert!!'
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = toaddr
        
        fp= open('movement.jpg','rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('ruellands@gmail.com','Lolipop12354')
        server.sendmail(me, toaddr, msg.as_string()) 
        server.quit()

