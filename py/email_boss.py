"""Demo: send an email."""

import time
import smtplib
from email.mime.text import MIMEText

from settings.emails import *

##
##

def main():

    print("\nSETTING UP SMTP MAIL SERVER.\n")

    # Set up the SMTP server & login
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # Note: sometimes ttls has to be turned off (?)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(FROM_ADDRESS, FROM_PASSWORD)

    # Create the msg outline & set contents
    print("CREATING EMAIL.")
    time.sleep(2)
    msg = MIMEText(EMAIL_TEXT)
    msg['From'] = FROM_ADDRESS
    msg['To'] = TO_ADDRESS
    msg['Subject'] = 'Working Really Hard!'

    # Check out the email
    print("\nPRINT OUT CREATED EMAIL:\n")
    print(msg)

    time.sleep(4)

    # Send message
    print("SENDING EMAIL")
    smtp.send_message(msg)
    time.sleep(1)
    print('EMAIL SENT!')

if __name__ == "__main__":
    main()