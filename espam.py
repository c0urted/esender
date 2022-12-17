import smtplib
import time
import random
from random_word import RandomWords

user = "support@accounthelp.org"
passwd = "asfJbuZoyQy243"

def mail_sender():
    r = RandomWords()
    x = r.get_random_word()
    subject = x
    msg = "Totally not spam or anything"
    message = "Subject:" + subject + "\n" + msg
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(user , passwd)
    server.sendmail(
        #from acc
        "support@accounthelp.org", 
        #to victim lol
        "johnnyjmolloy@gmail.com", 
        message)
    server.quit()

print("yo shitty test gui for now")

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
        time.sleep(5)
        exit()
spam()
