import smtplib
import time
import datetime
import random
import os
import fade
import colorama
from colorama import Fore, Back, Style
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Esender by c0urted
# Todo:
#  add unicode invis symbols to get around spam filters
#  fix user input so it only takes numbers
#

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


xyz = random.randint(0,1000000)
idnum = xyz
try:
    spamlist = open("spamlist.txt", "r")
except FileNotFoundError:
    print("file not found")
    spamlist = open("spamlist.txt", "w+")
    print("empty spamlist.txt created. Please enter your targs there and restart esender")
    time.sleep(5)


def main():
    clear_terminal()
    menu_options = int(input("Welcome to Espam!\nUse the number keys to navigate the menu\nWhat would you like to do?\n1) SMS Sendouts\n2) Email Sendouts\n3) Exit\n"))
    clear_terminal()
    while menu_options > 3 or menu_options <=0:
        menu_options = int(input("How could you fuck this up?? Just press a fucking number!!\n1) SMS Sendouts\n2) Email Sendouts\n3) Exit\n"))
# login for smtp server here
    email = "Put SMTP email here"
    passwd = "Put SMTP password here"
    smtp_address = "smtp.gmail.com"
    smtp_port = 465
    clear_terminal()
    if menu_options == 1:
        sms(email, passwd, smtp_address, smtp_port)
    elif menu_options == 2:
        clear_terminal()
        letter_choice = int(input("Do you have a letter to use?\n1) Yes\n2) No\n"))
        while letter_choice < 1 or letter_choice > 2:
            print("Fix your input retard. 1 or 2 its not that fucking hard\n")
        if letter_choice == 1:
            email_letter_sendout(email, passwd, smtp_address, smtp_port)
        else:
            email_sendout(email, passwd, smtp_address, smtp_port)
    elif menu_options == 3:
        #################
        # add email validator
        # 
        #################
        pass
    else:
        exit

# clears terminal and prints menu logo
def clear_terminal():
    #deinit keeps colorama from fucking up the fade module
    colorama.deinit()
    os.system("cls")
    faded = fade.purplepink(fade_me)
    print(faded)
    #initilizes colorama. deinit or fade wont work
    colorama.init()
    print(Fore.MAGENTA, "")

def supportnum():
    global idnum
    idnum += 1

def email_letter_sendout(user, passwd, smtp_address, smtp_port):
    # Remove the .SMTP_SSL if your smtp server doesnt support ssl
    # replace it with smtplib.SMTP instead
    server = smtplib.SMTP_SSL(smtp_address, smtp_port)
    server.login(user, passwd)
    html = open("paypal.html")
    msg = MIMEText(html.read(), "html")
    msg["subject"] = f"Account Case [{idnum}]"
    for i in spamlist:
        supportnum()
        server.sendmail(
            user,
            i,
            msg.as_string())
        server.quit()
        print("message sent to", i)
        x = random.randint(8,20)
        time.sleep(x)


def email_sendout(user, passwd, smtp_address, smtp_port):
    server = smtplib.SMTP_SSL(smtp_address, smtp_port)
    server.login(user, passwd)
    msg = MIMEText("Message here")
    msg["subject"] = f"Account Case [{idnum}]"
    for i in spamlist:
        supportnum()
        server.sendmail(
            user,
            i,
            msg.as_string())
        server.quit()
        print("message sent to", i)
        x = random.randint(1,10)
        time.sleep(x)


def sms(user, passwd, smtp_address, smtp_port):
    server = smtplib.SMTP_SSL(smtp_address, smtp_port)
    server.login(user, passwd)
    date_alert = datetime.datetime.now() + datetime.timedelta(days=30)
    message = f"PayPal Account Service DPT\nCase[{idnum}]\nYour account has been locked due to fraudulent activity. Please contact us by:{date_alert:%m-%d-%Y} or the account will be permanently disabled."
    for i in spamlist:
        server.sendmail(
            user,
            i,
            message)
        server.quit()
        print("message sent to", i)
        time.sleep(1)


main()
