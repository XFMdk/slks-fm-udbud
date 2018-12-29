from twilio.rest import Client

class Messenger:
    def __init__(self, twilio_acc = None, twilio_token = None, sender_name = None, email_sender = None):
        self.twilio_acc = twilio_acc
        self.twilio_token = twilio_token
        self.sender_name = sender_name
        self.email_sender = email_sender

    def can_email(self):
        if self.email_sender == None:
            return False
        return True
    
    def can_sms(self):
        if self.twilio_acc == None:
            return False
        elif self.twilio_token == None:
            return False
        elif self.sender_name == None:
            return False
        return True

    def email(self, receiver, subject, body):
        if not self.can_email():
            raise("Cannot email without email configuration.")

    def sms(self, receiver_number, message):
        if not self.can_sms():
            raise("Cannot SMS without SMS configuration")
        client = Client(self.twilio_acc, self.twilio_token)
        client.messages.create(to=receiver_number, from_=self.sender_name, body=message)

