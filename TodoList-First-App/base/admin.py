from django.contrib import admin
from .models import Task

# Register your models here.
#admin.site.register(Task)

# Or 👇👇 do it as shown below

@dmin.register(Task)
class AdminTask(admin.ModelAdmin):
  dixplay_list = ['user', 'title', 'completed', 'created')
