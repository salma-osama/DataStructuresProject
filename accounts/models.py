from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    # website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs): #kwargs key word arguments
    if kwargs['created']: #if the user object downward have been created then create userprofile
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
#signals are builtin in django they allow us to execute some particular code based on a certain thing that is happening in the database
#ana hena 3ayzah awel m ycreate user fldatabase y create userprofile el ana m3rfah fo2 da
