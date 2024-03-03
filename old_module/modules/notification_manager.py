# Todo get modules for sms and emails
class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, twilio_api_key, login_email, password_email):
        self.TWILIO_API_KEY = twilio_api_key
        self.LOGIN_EMAIL = login_email
        self.PASSWORD_EMAIL = password_email

    def send_sms_notification(self, message, to_phone_number):
        pass

    def send_email_notification(self, message, subject):
        pass

    pass
