from django.contrib import admin

# Register your models here.

#for get models group and user from models admin
from django.contrib.auth.models import Group, User
# get profile from models.py
from .models import Profile, Meep




#for unregister group and user in admin page
admin.site.unregister(Group)
admin.site.unregister(User)

#Mix user profile info to user info
class ProfileInLine(admin.StackedInline):
    model = Profile

# extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    #to insert follows to useradmin models
    inlines = [ProfileInLine]

#for register just username in auth or user
admin.site.register(User, UserAdmin)

#register models profile to admin page, so we can see profile models in admin page
#admin.site.register(Profile) #comment because we no need again this, we just using profile info page in UserAdmin 

#register Meep
admin.site.register(Meep)