from django.contrib import admin
from django.urls import path, include

#From project
from base.views import TaskList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
