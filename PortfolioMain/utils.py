from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings

def send_contact_email(mail_subject, mail_template, context):
    admin_info = User.objects.filter(is_superuser= True)
    print(admin_info)
    admin_email = []
    for i in admin_info:
        admin_email.append(i.email)
    print(admin_email)
    message = render_to_string(mail_template, context)
    
    mail = EmailMessage(mail_subject, message, to=admin_email)
    mail.content_subtype = "html"
    mail.send()