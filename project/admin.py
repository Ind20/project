from django.contrib import admin
from .models import project, projectCategory


class projectAdmin(admin.ModelAdmin):
    list_display =('Project_Name', 'Project_Category', 'Student_Name','Mentor_Name', 'Project_Image', 'Project_Video_url', 'Project_Description')

admin.site.register(project, projectAdmin)

class projectCategoryAdmin(admin.ModelAdmin):
    list_display =('Category_Name', 'Category_Description', 'Category_Image')

admin.site.register(projectCategory, projectCategoryAdmin)