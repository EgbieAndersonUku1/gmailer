##############################################################################
# EmailGmail: Allows the user to send email using the gmail services.
#
# In order to send emails using an outside source for example an external
# app, scripts or in this case the EmailGmail one has to turn on the
# 'less secure app' function setting located in the settings of their gmail
# account setting page. Once this done the user will be able to send emails to any
# account
# 
# Egbie Uku
#
###############################################################################

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from base_email import BaseEmail


class EmailGmail(BaseEmail):
    """Email:(class) -> Allows the user to send an email to another
       email address to another using Gmail services.
    """
    def __init__(self, gmail_addr, receiver_addr, subject, body_text, passwd):
        BaseEmail.__init__(self, gmail_addr, receiver_addr, subject, body_text)
        self.passwd = passwd
        self._msg = self._construct_email()

    def _secure_and_connect(self):
        """Creates a secure connection between the email addresses"""

        assert self.passwd, 'Password cannot be empty.'
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo()

        try:
            conn.starttls() # Uses TLS to encrpyt the connection.
        except:
            raise Exception('Failed to connect your system does not support TLS')
        else:
            conn.ehlo()
            return conn

    def _login(self):
        """Login into the email address"""

        conn = self._secure_and_connect()
        try:
            conn.login(self.get_gmail_addr(), self.passwd)
        except:
            raise Exception('Failed to login, check username and password.')
        else:
            return conn

    def _construct_email(self):
        """Creates the typical stuff associated with an email,
        e.g. sender address, receiver addrss, subject, body, etc.
        """
        # construct the email
        email_msg = MIMEMultipart('alternative')
        email_msg['Subject'] = self.get_subject()
        email_msg['From'] = self.get_gmail_addr()
        email_msg['To'] = self.get_receiptant_addr()

        text_part = MIMEText(self.get_body_text(), 'plain')
        html_part = MIMEText(self.get_body_html(), 'html')

        email_msg.attach(text_part)
        email_msg.attach(html_part)
        return email_msg

    def send_email(self):
        """send_email(None) -> return(dict or boolean)

        Sends an email address from one email to another.
        Returns True if the email was sent or returns a dict
        containing elements of the fields that were not sent.

        >>> gmail_addr="egbieAndersonuku1@example.com"
        >>> receiver_addr="test@example.com"
        >>> subject = "I am sending you an email"
        >>> body_text = "Thanks for registering to the network"
        >>> email = Email(gmail_addr, receiver_addr, subject, body_text)
        >>> print(email.send_email())
        'True'
        """
        conn = self._login()
        res = conn.sendmail(self.get_gmail_addr(), self.get_receiptant_addr(), self._msg.as_string())
        conn.quit()
        return True if not res else res
