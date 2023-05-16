from django.db import models

#for get models form admin page
from django.contrib.auth.models import User
# we can save post when we doing something
from django.db.models.signals import post_save

#from django.dispatch import receiver

# Create your models here.

# create meep models
class Meep(models.Model):
    user = models.ForeignKey(
        User, related_name="meeps",
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='meep_likes', blank=True)
    
    
    # kepp track or count of likes
    def CountLikesMeep(self):
        return self.likes.count()
    
    
    
    def __str__(self):
        return (
            f"{self.user}"
            f"{self.created_at:%Y-%m-%d %H-%M}"
            f"{self.body}..."
        )


# create Profile models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="follow_by",
        symmetrical=False,
        blank=True
    )
    date_modified = models.DateTimeField(User, auto_now=True)
    
    # to add profile picture
    profile_pic = models.ImageField(blank=True, null=True, upload_to='images/') #<- upload to will upload pic to images file in media file
    
    # for make profile can return username, cuz' if we just using code above we can confuse. because code above just return object user not username
    def __str__(self) -> str:
        return self.user.username

#@receiver(post_save, sender=User) #this code and bottom code (post_save) have same function,
# but if we want to use code above, we should import "receiver" from django.dispatch
# create profile when new user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # have the user follows themselves 
        # for follow someone
        user_profile.follows.set([instance.profile.id])
        user_profile.save()
        
post_save.connect(create_profile,sender=User)