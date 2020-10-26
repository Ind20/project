from django.contrib import admin
from .models import contactusMessage, userProfile

class contactusMessageAdmin(admin.ModelAdmin):
    list_display =('fullname', 'phone_num', 'email', 'message')

admin.site.register(contactusMessage, contactusMessageAdmin)


class userProfileAdmin(admin.ModelAdmin):
    list_display =('phone_num', 'age')

admin.site.register(userProfile, userProfileAdmin)
