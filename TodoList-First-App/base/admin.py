#from django
from django.contrib import admin

#from project
from .models import Task

# Register your models here.
#admin.site.register(Task)

# Or 👇👇 do it as shown below

@dmin.register(Task)
class AdminTask(admin.ModelAdmin):
   list_display = ('user', 'title', 'created','complete')
   list_filter = ("created",)
   search_fields = ['title',]
