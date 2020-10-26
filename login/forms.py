from django import forms
from .models import contactusMessage, userProfile

class contactusMessageForm(forms.ModelForm):
    class Meta:
        model= contactusMessage
        fields= ["fullname", "phone_num", "email", "message"]


class userProfileForm(forms.ModelForm):
    class Meta:
        model   = userProfile
        fields  = ["age", "phone_num", "profile_pic", 'user']