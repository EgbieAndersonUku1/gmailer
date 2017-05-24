# Egbie Uku

class BaseEmail(object):
    """BaseEmail(class): The base that would be used for the Email classes"""
    def __init__(self, gmail_addr, receiptant_addr, subject, body_text):
        self._gmail_addr = gmail_addr
        self._receiptant_addr = receiptant_addr
        self._subject = subject
        self._body_text = body_text
        self._are_fields_empty()

    def _are_fields_empty(self):
        """Check whether the parameters are empty. Raises an exception if the
        fields are empty.
        """
        if not self._gmail_addr:
            raise Exception('The gmail email address cannot be empty.')
        if not self._receiptant_addr:
            raise Exception("The receiptant address cannot be empty.")
        if not self._subject:
            self.subject = ''
        if not self._body_text:
            raise Exception('The email body text cannot both be empty.')

    # Change this one later to use the Flask version which renders HTML better
    def _to_html(self, text):
          """to_html(str) -> return str
          Changes ordinary plaintext to html format
          """
          return"""
                <HTML>
                        <BODY>
                                <P>
                                        {}
                                </P>
                        </BODY>
                </HTML>
          """.format(text)
    
    def set_gmail_addr(self, gmail_addr):
        """set a new source address"""
        self._gmail_addr = gmail_addr

    def set_receiver_addr(self, receiptant_addr):
        """set a new receiver address"""
        self._receiptant_addr = receiptant_addr

    def set_subject(self, subject):
        """set a new subject"""
        self._subject = subject

    def set_body_text(self, body_text):
        """File:text. Set a new body for text body email"""
        self._body_text = body_text

    def get_subject(self):
         """Return the subject"""
         return self._subject

    def get_gmail_addr(self):
         """Return the source address """
         return self._gmail_addr

    def get_receiptant_addr(self):
         """Return the receiptant address """
         return self._receiptant_addr

    def get_body_text(self):
          """Return the body of the email in plain text"""
          return self._body_text

    def get_body_html(self):
         """Return the body of the email in HTML"""
         return self._to_html(self.get_body_text())
    
