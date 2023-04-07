from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from accounts.models import User 
from accounts.models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, *args, **kwargs):
    instance.profile.save()