import smtplib
import sys
import time
import datetime
import random
import os
import fade
import colorama
from colorama import Fore, Back, Style
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import threading

RECIPIENTS = "recipients.txt"
SENDERS = "sender_list.txt"

INVIS_CHARS = [
    '\u0009', '\u0020', '\u00A0', '\u00AD', '\u034F', '\u061C', '\u070F',
    '\u115F', '\u1160', '\u1680', '\u17B4', '\u17B5', '\u180E', '\u2000',
    '\u2001', '\u2002', '\u2003', '\u2004', '\u2005', '\u2006', '\u2007',
    '\u2008', '\u2009', '\u200A', '\u200B', '\u200C', '\u200D', '\u200E',
    '\u200F', '\u202F', '\u205F', '\u2060', '\u2061', '\u2062', '\u2063',
    '\u2064', '\u206A', '\u206B', '\u206C', '\u206D', '\u206E', '\u206F',
    '\u3000', '\u2800', '\u3164', '\uFEFF', '\uFFA0', '\u110B1', '\u1BCA0',
    '\u1BCA1', '\u1BCA2', '\u1BCA3', '\u1D159', '\u1D173', '\u1D174',
    '\u1D175', '\u1D176', '\u1D177', '\u1D178', '\u1D179', '\u1D17A']

def read_config() -> str:
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        print("[X] Config file 'config.json` not found. Please create the file with SMTP configuration.")
        sys.exit(-1)

config = read_config()
SMTP_USERNAME = config["SMTP_USERNAME"] 
SMTP_PASSWORD = config["SMTP_PASSWORD"]
SMTP_SERVER = config["SMTP_SERVER"]
SMTP_PORT = config["SMTP_PORT"]
EMAIL_SUBJECT = config["EMAIL_SUBJECT"]
EMAIL_LETTER = config["EMAIL_LETTER"]

# Esender by c0urted
# Todo:
#  add unicode invis symbols to get around spam filters
#  add utf-8 encoding for html letters

START_MSG = """
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


def main():
    try:
        global recipient_list
        recipient_list = open(RECIPIENTS, "r")
    except FileNotFoundError:
        print("[X] File 'recipients.txt` not found. Please read the README file.")
        recipient_list = open(RECIPIENTS, "w+")
        print("[-] Empty 'recipients.txt` file created. Enter your email recipients there and restart the script.")
        sys.exit(-1)
    except Exception as e:
        print(f"[X] {e}")
        
    # loop until we get valid input from the menu
    menu_options = get_menu_option()
    clear_terminal()


    clear_terminal()
    if menu_options == 1:
        sms(SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT)
    elif menu_options == 2:
        clear_terminal()
        print("[*] Do you have a letter to use?")
        print("[1] Yes")
        print("[2] No")
        letter_choice = None
        while letter_choice is None:
            try:
                letter_choice = int(input("[*] Please enter your choice: "))
                if letter_choice not in [1, 2]:
                    raise ValueError
            except ValueError:
                print("[X] Invalid input. Please enter 1 or 2.")
                letter_choice = None
        if letter_choice == 1:
            print("[*] Do you want to use unicode characters to bypass spam filters?")
            print("[1] Yes")
            print("[2] No")
            unicode_choice = None
            while unicode_choice is None:
                try:
                    unicode_choice = int(input("[*] Please enter your choice: "))
                    if unicode_choice not in [1, 2]:
                        raise ValueError
                except ValueError:
                    print("[X] Invalid input. Please enter 1 or 2.")
                    unicode_choice = None
            if unicode_choice == 1:
                email_letter_unicode_sendout(SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT)
            else:
                email_letter_sendout(SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT)
        else:
            unicode_menu_option()
            if unicode_choice == 1:
                #email_unicode_sendout(SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT)
                pass
            else:
                email_sendout(SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT)
    elif menu_options == 3:
        # todo: add email validator
        # use paid api bcs easier
        pass
    else:
        sys.exit(0)


def unicode_antispam_bypass() -> str:
    email_subject = EMAIL_SUBJECT
    unicode_subject = ""
    for char in email_subject:
        unicode_subject += char + random.choice(INVIS_CHARS)
    return unicode_subject

def unicode_menu_option() -> int:
    print("[*] Do you want to use unicode characters to bypass spam filters?")
    print("[1] Yes")
    print("[2] No")
    unicode_choice = None
    while unicode_choice is None:
        try:
            unicode_choice = int(input("[*] Please enter your choice: "))
            if unicode_choice not in [1, 2]:
                raise ValueError
            else:
                return unicode_choice
        except ValueError:
            print("[X] Invalid input. Please enter 1 or 2.")
            unicode_choice = None

def get_menu_option() -> int:
    return_input = None
    while return_input is None:
        try:
            clear_terminal()
            menu_options = int(input(
                "[*] Welcome to Espam!\n"
                "[*] Use the number keys to navigate the menu.\n"
                "[1] SMS Sendouts\n"
                "[2] Email Sendouts\n"
                "[3] Email Validator (not added yet)\n"
                "[?] What would you like to do?\n\n"))
            # validate the input and loop if invalid
            if menu_options not in [1, 2, 3]:
                continue
            else:
                return menu_options
        except Exception as e:
            print(f"[X] Failed parsing menu option. Try again. Error: {e}")
        return_input = None  # ensure the menu loops

def clear_terminal() -> None:
    # function clears the terminal and prints menu logo. dont fuck with it
    # deinit keeps colorama from fucking up the fade module
    colorama.deinit()
    os.system("cls")
    faded = fade.purplepink(START_MSG)
    print(faded)
    # initilizes colorama. deinit or fade wont work
    colorama.init()
    print(Fore.MAGENTA, "")

def supportnum() -> None:
    global account_case
    account_case = random.randint(0, 1000000)
    account_case += 1

def email_letter_sendout(SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT) -> None:
    # Remove the .SMTP_SSL if your smtp server doesn't support SSL/TLS
    # Replace it with smtplib.SMTP instead
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        # todo: make it so ppl can change the file name for html letter and subject
        html = open(EMAIL_LETTER)
        msg = MIMEText(html.read(), "html")
        msg["subject"] = f"Account Case [{account_case}]".encode('utf-8')
        for i in recipient_list:
            supportnum()
            # send the email to the user with the msg content
            server.sendmail(SMTP_USERNAME, i, msg.as_string())
            print(f"[-] Message sent to '{i}'")
            # quit from the email server after a random time to evade detection and
            # todo: this should be async/threaded so it doesn't block other sends
            x = random.randint(8, 20)
            time.sleep(x)
            server.quit()
    except Exception as fuckup:
        print(f"Oops something went wrong. Error output on the next line.\n{fuckup}")
        time.sleep(10)

def email_letter_unicode_sendout(SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT) -> None:
    # Remove the .SMTP_SSL if your smtp server doesn't support SSL/TLS
    # Replace it with smtplib.SMTP instead
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        html = open(EMAIL_LETTER)
        msg = MIMEText(html.read(), "html")
        msg["subject"] = unicode_antispam_bypass()
        for i in recipient_list:
            supportnum()
            # send the email to the user with the msg content
            server.sendmail(SMTP_USERNAME, i, msg.as_string())
            print(f"[-] Message sent to '{i}'")
            x = random.randint(8, 20)
            time.sleep(x)
            server.quit()
    except Exception as fuckup:
        print(f"Oops something went wrong. Error output on the next line.\n{fuckup}")
        time.sleep(10)

def email_sendout(SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT):
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        msg = MIMEText("Message here")
        msg["subject"] = f"Account Case [{account_case}]"
        for i in recipient_list:
            supportnum()
            server.sendmail(
                SMTP_USERNAME,
                i,
                msg.as_string())
            server.quit()
            print("message sent to", i)
            x = random.randint(1, 10)
            time.sleep(x)
    except Exception as fuckup:
        print(f"Oops something went wrong. Error output on the next line.\n{fuckup}")
        time.sleep(10)

def sms(SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT):
    # todo: add loop to retry failed sends
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        date_alert = datetime.datetime.now() + datetime.timedelta(days=30)
        # todo: purge message before upload
        message = f"PayPal Account Service DPT\nCase[{account_case}]\nYour account has been locked due to fraudulent activity. " \
                    f"Please contact us by:{date_alert:%m-%d-%Y} or the account will be permanently disabled."
        for i in recipient_list:
            server.sendmail(
                SMTP_USERNAME,
                i,
                message)
            server.quit()
            print("message sent to", i)
            time.sleep(1)
    except Exception as fuckup:
        print(f"Oops something went wrong. Error output on the next line.\n{fuckup}")
        time.sleep(10)

if __name__ == "__main__":
    main()
