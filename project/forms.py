from django import forms
from .models import project


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
        if value:
            option['attrs']['data-price'] = value.instance.price
        return option

        fields = ['Project_Category']
        widgets = {
            'Project_Category': Project_CategorySelect
            }