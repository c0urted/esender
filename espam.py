import smtplib
import time
import random
import os
import fade
import colorama
from colorama import Fore, Back, Style

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

#SMTP SERVER LOGIN
user = "username here"
passwd = "password here"
xyz = random.randint(0,100000)
idnum = xyz

print("sms format is like 1234567890@txt.att.net")
victim = input("please input victim email or phone here\n")
isnum = input("is this a number [Y/N]\n")

wordlist = open("wordlist.txt", "r")
wordlist_data = wordlist.readlines()


def supportnum():
    global idnum
    idnum += 1


def sms_sender():
    w = random.choice(wordlist_data)
    x = random.choice(wordlist_data)
    y = random.choice(wordlist_data)
    z = random.choice(wordlist_data)
    sms_msg = "[" + str(idnum) + "]" + "\n" + x + " " + y + " " + z
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(user , passwd)
    server.sendmail(
        user,
        victim,
        sms_msg)
    server.quit()

def sms_spam():
    spam_count = int(input("how many texts to send?\n"))
    for i in range(spam_count):
            sms_sender()
            supportnum()
            print("message sent with ID [{}]!".format(idnum))
            rand_num = random.randint(0,5)
            time.sleep(rand_num)


def mail_sender():
    w = random.choice(wordlist_data)
    x = random.choice(wordlist_data)
    y = random.choice(wordlist_data)
    z = random.choice(wordlist_data)
    subject = "[{}]".format(idnum)
    msg = w + " " + x + " " + y + " " + z
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
            supportnum()
            print("message sent with ID [{}]!".format(idnum))
            rand_num = random.randint(0,5)
            time.sleep(rand_num)

if isnum.lower().startswith("y") == True:
    sms_spam()
elif isnum.lower().startswith("n") == True:
    spam()
else:
    print("try again")
