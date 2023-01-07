import smtplib
import time
import random
import os
import fade
import colorama
from colorama import Fore, Back, Style
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fade_me = """
8888888888 .d8888b.                                  
888       d88P  Y88b                                 
888       Y88b.                                      
8888888    "Y888b.   88888b.   8888b.  88888b.d88b.  
888           "Y88b. 888 "88b     "88b 888 "888 "88b 
888             "888 888  888 .d888888 888  888  888 
888       Y88b  d88P 888 d88P 888  888 888  888  888 
8888888888 "Y8888P"  88888P"  "Y888888 888  888  888 
                     888                             
                     888                             
                     888                      By: c0urted"""
faded = fade.purplepink(fade_me)
print(faded)

colorama.init()
print(Fore.MAGENTA + "")

xyz = random.randint(0,100000)
idnum = xyz
user = "USERNAME HERE"
passwd = "PASSWORD HERE"
spamlist = open("email.txt", "r")
html = open("paypal.html")      # change to your letter in the same folder

def supportnum():
    global idnum
    idnum += 1


def targs():
    msg = MIMEText(html.read(), "html")
    msg["subject"] = "Account Case [{}]".format(idnum)
    for i in spamlist:
        supportnum()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(user , passwd)
        server.sendmail(
            user,
            i,
            msg.as_string())
        server.quit()
        print("message sent to", i)
        x = random.randint(1,15)
        time.sleep(x)

## sms isnt finished bcs these drugs aint gonna do themselves

def sms():
    message = "Your account has been locked. Please sign on to unlock it\nhttps://PayPal.com/"
    for i in spamlist:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(user , passwd)
        server.sendmail(
            user,
            i,
            message)
        server.quit()
        print("message sent to", i)
        time.sleep(1)

run = input("Are you spamming Emails or SMS?\n1) emails\n2) SMS\n")
if run.startswith("1"):
    targs()
elif run.startswith("2"):
    sms()
else:
    quit()
