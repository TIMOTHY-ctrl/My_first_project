from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def assign_user_group(sender, instance, created, **kwargs):
    if created: #Only assign groups when a new user is created
        if instance.role == "student":
            group, _ = Group.objects.get_or_create(name='Student')
        elif instance.role == "lecturer":
            group, _ = Group.objects.get_or_create(name="Lecturer")
        elif instance.role == "academic_registrar":
            group, _ = Group.objects.get_or_create(name="Academic Registrar")
        elif instance.role == "admin":
            group, _ = Group.objects.get_or_create(name="Adminstrator")
        else:
            return   #Skip if no valid role

            instance.groups.add(group) #Assign the user to the correct group