from django import forms
from .models import contactusMessage, userProfile

class contactusMessageForm(forms.ModelForm):
    class Meta:
        model   = contactusMessage
        fields  = ["fullname", "phone_num", "email", "message"]
        widgets = {
            'fullname': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_num': forms.NumberInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'message': forms.Textarea(attrs={'class' : 'form-control'}),
        }

class userProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False,widget=forms.FileInput)
    age         = forms.IntegerField(required=False)
    phone_num   = forms.CharField(max_length = 15, required=False)
    class Meta:
        model   = userProfile
        fields  = ["age", "phone_num", "profile_pic"]