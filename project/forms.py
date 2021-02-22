from django import forms
from .models import project


class projectForm(forms.ModelForm):
    class Meta:
        model   = project
        fields  = ["Project_Name", "Project_Category", "Student_Name", "Mentor_Name", "Project_Image", "Project_Video_url", "Project_Description"]
        widgets = {
            'Project_Name': forms.TextInput(attrs={'class' : 'form-control'}),
            'Project_Category': forms.TextInput(attrs={'class' : 'form-control'}),
            'Student_Name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Mentor_Name': forms.TextInput(attrs={'class' : 'form-control'}),
            'Project_Image': forms.FileInput(attrs={'class' : 'form-control'}),
            'Project_Video_url': forms.TextInput(attrs={'class' : 'form-control'}),
            'Project_Description': forms.Textarea(attrs={'class' : 'form-control'}),
        }