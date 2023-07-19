from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.models import User 




class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject    = data['email_subject'],
            body       = data['email_body'],
            to         = [data['to_email']],
        )
        email.content_subtype = 'html'
        email.send()

def get_verify_code_and_send(email):
    try:
        user = User.objects.get(email=email)
        mail_code = user.verify_code
       
        context = {'user':user, 'mail_code':mail_code}
        message = render_to_string('mails/account_verification.html', context)

        data = {
            'email_subject':'Eminence Trading Academy VERIFICATION',
            'email_body': message,
            'to_email':user.email
        }
        Util.send_email(data)
    except User.DoesNotExist:
        user = None


def authenticate_code(code):
    user = User.objects.filter(verify_code=code)
    user.is_verified=True