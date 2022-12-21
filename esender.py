
import smtplib
import time
import random
import os
import fade
import colorama
from colorama import Fore, Back, Style
from random_word import RandomWords
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

user = "services@accounthelp.org"
passwd = "ServiceSpam@1337"
spamlist = open("email.txt", "r")
html = open("paypal.html")      # change to your scampage name

def targs():
    msg = MIMEText(html.read(), "html")
    msg["subject"] = "Your Account has been locked"
    for i in spamlist:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(user , passwd)
        server.sendmail(
            user,
            i,
            msg.as_string())
        server.quit()
        print("message sent to", i)
        time.sleep(1)

def sms():
#    message = "Your account has been locked. Please sign on to unlock it\nhttps://PayPal.com/"
    message = "hi nigger\ngot it working"
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

run = input("Are you spamming Emails or SMS?\n1) emails\n2) SMS")
if run.startswith("1"):
    targs()
elif run.startswith("2"):
    sms()
else:
    quit()