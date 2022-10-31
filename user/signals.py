from django.core.mail import send_mail

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.conf import settings
from user.views import views
USER=get_user_model()

   #email
@receiver(post_save,sender=USER)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        email=instance.email
        print(email)
        send_mail(
            'Thank you for the signup',
            'WELCOME TO BLOGGING PORT,PUBLISH UR PASSION.',
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
                )
        
        
       
       