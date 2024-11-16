import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = "465"

    username = "eric.codes.qa@gmail.com"
    password = "hadg oawd xgds ylen"

    my_context = ssl.create_default_context()
    receiver = "eric.codes.qa@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
