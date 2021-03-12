from django import forms
from .models import project
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
        }

class Project_CategorySelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        return option

        fields = ['Project_Category']
        widgets = {
            'Project_Category': Project_CategorySelect
            }