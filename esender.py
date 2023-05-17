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

RECIPIENTS = "recipients.txt"
SENDERS = "sender_list.txt"

SMTP_USERNAME = ""  # todo: move this to an .env or config file to avoid upload
SMTP_PASSWORD = ""  # todo: move this to an .env or config file to avoid upload
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 456

# Esender by c0urted
# Todo:
#  add unicode invis symbols to get around spam filters
#  fix user input so it only takes numbers

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

# todo: remove this to another section (inside main?)
account_case = random.randint(0, 1000000)

# try:
#     recipient_list = open(RECIPIENTS, "r")
# except FileNotFoundError:
#     print("[X] File 'recipients.txt` not found. Please read the README file.")
#     recipient_list = open(RECIPIENTS, "w+")
#     print("[-] Empty 'recipients.txt` file created. Enter your email recipients there and restart the script.")
#     sys.exit(-1)


def main():
    try:
        global recipient_list
        recipient_list = open(RECIPIENTS, "r")
    except FileNotFoundError:
        print("[X] File 'recipients.txt` not found. Please read the README file.")
        recipient_list = open(RECIPIENTS, "w+")
        print("[-] Empty 'recipients.txt` file created. Enter your email recipients there and restart the script.")
        sys.exit(-1)
    # loop until we get valid input from the menu
    menu_options = get_menu_option()
    clear_terminal()

    # get login details for smtp server here
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
        # todo: add email validator
        pass
    else:
        sys.exit(0)


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


# clears terminal and prints menu logo
def clear_terminal() -> None:
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
    account_case += 1


def email_letter_sendout(user, passwd, smtp_address, smtp_port) -> None:
    # Remove the .SMTP_SSL if your smtp server doesn't support SSL/TLS
    # Replace it with smtplib.SMTP instead
    try:
        server = smtplib.SMTP_SSL(smtp_address, smtp_port)
        server.login(user, passwd)
        # todo: make it so ppl can change the file name for html letter and subject
        html = open("paypal.html")
        msg = MIMEText(html.read(), "html")
        msg["subject"] = f"Account Case [{account_case}]"
        for i in recipient_list:
            supportnum()
            # send the email to the user with the msg content
            server.sendmail(user, i, msg.as_string())
            print(f"[-] Message sent to '{i}'")
            # quit from the email server after a random time to evade detection and
            # todo: this should be async/threaded so it doesn't block other sends
            x = random.randint(8, 20)
            time.sleep(x)
            server.quit()
    except Exception as fuckup:
        print(f"Oops something went wrong. Error output on the next line.\n{fuckup}")
        time.sleep(10)

def email_sendout(user, passwd, smtp_address, smtp_port):
    try:
        server = smtplib.SMTP_SSL(smtp_address, smtp_port)
        server.login(user, passwd)
        msg = MIMEText("Message here")
        msg["subject"] = f"Account Case [{account_case}]"
        for i in recipient_list:
            supportnum()
            server.sendmail(
                user,
                i,
                msg.as_string())
            server.quit()
            print("message sent to", i)
            x = random.randint(1, 10)
            time.sleep(x)
    except Exception as fuckup:
        print(f"Oops something went wrong. Error output on the next line.\n{fuckup}")
        time.sleep(10)

def sms(user, passwd, smtp_address, smtp_port):
    # todo: add loop to retry failed sends
    try:
        server = smtplib.SMTP_SSL(smtp_address, smtp_port)
        server.login(user, passwd)
        date_alert = datetime.datetime.now() + datetime.timedelta(days=30)
        # todo: message should be changed to an official paypal HTML email
        message = f"PayPal Account Service DPT\nCase[{account_case}]\nYour account has been locked due to fraudulent activity. " \
                    f"Please contact us by:{date_alert:%m-%d-%Y} or the account will be permanently disabled."
        for i in recipient_list:
            server.sendmail(
                user,
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
