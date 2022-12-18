
import smtplib
import time
import random
import os
import fade
import colorama
from colorama import Fore
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

user = "EMAIL HERE"
passwd = "PASSWORD HERE"
#you will need to make the file below yourself
spamlist = open("email.txt", "r")
emails = spamlist.readlines()
#change to your html letter
html = open("paypal.html")


def targs():
    count = 0
    msg = MIMEText(html.read(), "html")
    #change the subject
    msg["subject"] = "Your Account has been locked"
    for i in emails:
        count += 1
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(user , passwd)
        server.sendmail(
            user,
            emails,
            msg.as_string())
        server.quit()
        print("message sent to", i)
        time.sleep(1)

targs()
