from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User


admin.site.register(Profile)

# mix profile information and the user information 
class profileInline(admin.StackedInline):
    model=Profile
  
# extends the user model
class userAdmin(admin.ModelAdmin):
    model=User
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines=[profileInline]
 
 
 
# Unregister the old way 
admin.site.unregister(User)

# re-register the new way  
admin.site.register(User,userAdmin)  
    