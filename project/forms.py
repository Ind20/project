from django import forms
from .models import project


class projectForm(forms.ModelForm):
    class Meta:
        model   = project
        fields  = '__all__'
        widgets = {
            'Project_Name': forms.TextInput(attrs={'class' : 'form-control'}),
            'Project_Category': forms.TextInput(attrs={'class' : 'form-control'}),
            'Student_Name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Mentor_Name': forms.TextInput(attrs={'class' : 'form-control'}),
            'Project_Image': forms.FileInput(attrs={'style' : 'margin-top:15px'}),
            'Project_Video_url': forms.TextInput(attrs={'class' : 'form-control'}),
            'Project_Description': forms.Textarea(attrs={'class' : 'form-control'}),
        }