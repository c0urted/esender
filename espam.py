import smtplib
import time
import random
from random_word import RandomWords

user = "EMAIL"
passwd = "PASSWORD"
victim = input("please input victim email here\n")

def mail_sender():
    r = RandomWords()
    x = r.get_random_word()
    subject = x
    msg = "Totally not spam or anything"
    message = "Subject:" + subject + "\n" + msg
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(user , passwd)
    server.sendmail(
        user,
        victim,
        message)
    server.quit()

def spam():
    spam_count = int(input("how many emails to send? MUST BE UNDER 125\n"))
    if spam_count <= 125:
        print("we good. spamming now")
        for i in range(spam_count):
            mail_sender()
            print("message sent!")
            zzz = random.randint(1,9)
            time.sleep(zzz)

    else:
        print("the fuck wrong with u nigga\nthink about the shit u just did")
        time.sleep(2)
        exit()
spam()
