import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password"
subject = "Subject title"
body = "Message"


# header
message = f"""From: Nickname{sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")

    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")



