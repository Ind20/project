from django import forms
from django.contrib.auth.models import User
from .models import contactusMessage, userProfile, project


class contactusMessageForm(forms.ModelForm):
    class Meta:
        model   = contactusMessage
        fields  = ["fullname", "phone_num", "email", "message"]
        widgets = {
            'fullname': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_num': forms.NumberInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'message': forms.Textarea(attrs={'class' : 'form-control'})
        }



class userProfileForm(forms.ModelForm):
    class Meta:
        model   = userProfile
        fields  = ['age', 'phone_num']
        widgets = {
            'age': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_num': forms.TextInput(attrs={'class' : 'form-control'})
        }



class userProfileUpdateForm(forms.ModelForm):
    class Meta:
        model   = userProfile
        fields  = ['age', 'phone_num', 'profile_pic']
        widgets = {
            'age': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone_num': forms.TextInput(attrs={'class' : 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'style' : 'margin-top:15px'}),
        }



class userUpdateForm(forms.ModelForm):
    class Meta:
        model   = User
        fields  = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'})
        }



class projectForm(forms.ModelForm):
    class Meta:
        model   = project
        fields  = '__all__'
        widgets = {
            'Project_Name': forms.TextInput(attrs={'class' : 'form-control'}),
            'Student_Name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Mentor_Name': forms.TextInput(attrs={'class' : 'form-control'}),
            'Project_Image': forms.FileInput(attrs={'style' : 'margin-top:15px'}),
            'Project_Video_url': forms.TextInput(attrs={'class' : 'form-control'}),
            'Project_Description': forms.Textarea(attrs={'class' : 'form-control'}),
            'Attachment': forms.FileInput(attrs={'style' : 'margin-top:15px'})
        }



class Project_CategorySelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        return option

        fields = ['Project_Category']
        widgets = {
            'Project_Category': Project_CategorySelect
            }