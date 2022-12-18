import smtplib
import time
import random
import os
import fade
import colorama
from colorama import Fore, Back, Style
from random_word import RandomWords

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

print("sms format is like 1234567890@txt.att.net")
victim = input("please input victim email or phone here\n")
isnum = input("is this a number [Y/N]")

def sms_sender():
    r = RandomWords()
    x = r.get_random_word()
    y = r.get_random_word()
    z = r.get_random_word()
    sms_msg = x + " " + y + " " + z
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(user , passwd)
    server.sendmail(
        user,
        victim,
        sms_msg)
    server.quit()

def sms_spam():
    spam_count = int(input("how many texts to send?"))
    for i in range(spam_count):
            sms_sender()
            print("sms message sent!")
            zzz = random.randint(1,9)
            time.sleep(zzz)


def mail_sender():
    r = RandomWords()
    w = r.get_random_word()
    x = r.get_random_word()
    y = r.get_random_word()
    z = r.get_random_word()
    subject = w
    msg = x + " " + y + " " + z
    message = "Subject:" + subject + "\n" + msg
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(user , passwd)
    server.sendmail(
        user,
        victim,
        message)
    server.quit()

def spam():
    spam_count = int(input("how many emails to send?"))
    for i in range(spam_count):
            mail_sender()
            print("message sent!")
            zzz = random.randint(1,9)
            time.sleep(zzz)

if isnum.lower().startswith("y") == True:
    sms_spam()
elif isnum.lower().startswith("n") == True:
    spam()
else:
    print("try again")
