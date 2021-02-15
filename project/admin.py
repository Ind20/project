from django.contrib import admin
from .models import project


class projectAdmin(admin.ModelAdmin):
    list_display =('Project_Category', 'Project_Name', 'Student_Name','Mentor_Name', 'Project_Image_url', 'Project_Video_url', 'Project_Description')

admin.site.register(project, projectAdmin)