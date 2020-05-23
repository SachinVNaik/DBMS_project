import smtplib
from essential import gmail
import random


def shorten_mail(email):
    lst = email.split('@')
    email = lst[0][:3]
    for i in range(3, len(lst[0])):
        email += '*'
    email += lst[1]
    return email


def send_email(reciever):
    # creates SMTP session
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(gmail['sender'], gmail['password'])

        # message to be sent
        secret_key = random.randint(100000, 999999)
        subject = "YES TRAVELS password reset code"
        text = f"Hello Sir/Madam \n use this code for resetting your password\n {secret_key}"
        message = 'Subject: {}\n\n{}'.format(subject, text)

        # sending the mail
        s.sendmail(gmail['sender'], reciever, message)

        # terminating the session
        s.quit()
        return secret_key
    except Exception as e:
        print('error in sending mail')


def read_status():
    file = open('login_status.txt', 'r')
    file_data = file.read()
    file_data = file_data.split()
    status = bool(int(file_data[0]))
    file.close()
    return status


def write_status(status, name):
    file = open('login_status.txt', 'w')
    line = int(status)
    file.writelines(str(line))
    file.writelines('\n')
    file.writelines(str(name))
    file.close()
    return


def read_name():
    file = open('login_status.txt', 'r')
    try:
        file_data = file.read()
        file_data = file_data.split()
        name = str(file_data[1])
        return name
    except IndexError as e:
        print(e)
    finally:
        file.close()
