# signals.py

import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Poll Me'
        html_message = render_to_string('accounts/templates/emails/welcome_email.html', {'user': instance, 'year': datetime.now().year})
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to = instance.email

        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
