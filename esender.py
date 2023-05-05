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
#  check for bounced emails
#  create a count for bounced emails and show it on the menu

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

def file_check():
    try:
        # spamlist might not work. dont wanna fix rn do later.
        global spamlist
        spamlist = open("spamlist.txt", "r")
    except FileNotFoundError:
        print("Spamlist.txt not found. Creating it now.")
        with open("spamlist.txt", "w+") as spamlist:
            print("Spamlist.txt has been created. Please enter your targs there and restart the sender.")
            time.sleep(5)

    try:
        with open("login.txt", "r") as login:
            login_info = login.readline().strip().split(":")
            email = login_info[0]
            passwd = login_info[1]
            smtp_address = login_info[2]
            smtp_port = int(login_info[3])
            encryption = int(login_info[4])

    except FileNotFoundError:
        print("login.txt not found. Making it now.")
        enter_login()

    # except IndexError:
    #     print("Login file missing login info. Please enter it now.")
    #     enter_login()
    return email, passwd, smtp_address, smtp_port, encryption

def enter_login():
    with open("login.txt", "w+") as login:
        email = input("Enter your email address: ")
        passwd = input("Enter your password: ")
        smtp_address = input("Enter your SMTP server: ")
        smtp_port = int(input("Enter your smtp port: "))
        encryption = input("Does your smtp use any ecnryption?\n1) SSL\n2) TLS\n3) None\n")
        login.write(f"{email}:{passwd}:{smtp_address}:{smtp_port}:{encryption}")

def main():
    email, passwd, smtp_address, smtp_port, encryption = file_check()
    clear_terminal()
    while True:
        try:
            menu_options = int(input("Welcome to Espam!\nUse the number keys to navigate the menu\nWhat would you like to do?\n1) SMS Sendouts\n2) Email Sendouts\n3) Edit login info\n0) Exit\n"))
            break
        except ValueError:
            clear_terminal()
            print("Please use 0-9 for the menu.")
        except KeyboardInterrupt:
            clear_terminal()
            print("\nProgram terminated by user.")

    clear_terminal()
    try:
        if menu_options == 1:
            if encryption == 1:
                sms_ssl(email, passwd, smtp_address, smtp_port)
            elif encryption == 2:
                sms_tls(email, passwd, smtp_address, smtp_port)
            else:
                sms_no_encryption(email, passwd, smtp_address, smtp_port)

        elif menu_options == 2:
            while True:
                clear_terminal()
                try:
                    letter_choice = int(input("Do you have a letter to use?\n1) Yes\n2) No\n0) Exit\n"))
                    if letter_choice == 1:
                        email_letter_sendout(email, passwd, smtp_address, smtp_port)
                        break
                    elif letter_choice == 2:
                        email_sendout(email, passwd, smtp_address, smtp_port)
                        break
                    elif letter_choice == 0:
                        exit()
                    else:
                        print("Please pick 1, 2 or 0")
                        time.sleep(3)
                except ValueError:
                    print("Please enter a number.")
                    time.sleep(3)

        elif menu_options == 3:
            with open("login.txt", "w+") as login:
                email = input("Enter your email address: ")
                passwd = input("Enter your password: ")
                smtp_address = input("Enter your SMTP server: ")
                smtp_port = int(input("Enter your smtp port: "))
                encryption = input("Does your smtp use any ecnryption?\n1) SSL\n2) TLS\n3) None\n")
                login.write(f"{email}:{passwd}:{smtp_address}:{smtp_port}:{encryption}")
                print("SMTP login info updated!")
                time.sleep(2)
                main()
        else:
            exit
    except ValueError:
        print("stuff")
    except smtplib.SMTPAuthenticationError:
        print("Error: Incorrect email or password.")
    except smtplib.SMTPConnectError:
        print("Error: Could not connect to SMTP server.")
    except smtplib.SMTPException as fuckup:
        print("Error:", fuckup)


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
    html_letter_name = input("Please make sure your letter is in the same folder as the sender.\nPlease input the filename of the letter: ")
    html = open(html_letter_name)
    msg = MIMEText(html.read(), "html")
    msg["subject"] = f"Account Case [{idnum}]"
    for i in spamlist:
        supportnum()
        server.sendmail(
            user,
            i,
            msg.as_string())
        server.quit()
        print("[*]\tMessage sent to:", i)
# Change the numbers for seconds to sleep between emails sent
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


def sms_no_encryption(user, passwd, smtp_address, smtp_port):
    server = smtplib.SMTP(smtp_address, smtp_port)
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


def sms_ssl(user, passwd, smtp_address, smtp_port):
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


def sms_tls(user, passwd, smtp_address, smtp_port):
    server = smtplib.SMTP(smtp_address, smtp_port)
    server.starttls()
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


if __name__ == "__main__":
    main()