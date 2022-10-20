from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomerLoginView, RegisterPage

urlpatterns = [
    path("login/", CustomerLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name="register"),

    path("", TaskList.as_view(), name='list'),
    path("task/<int:pk>", TaskDetail.as_view(), name='detail'),
    path('create-task', TaskCreate.as_view(), name='create'),
    path('update-task/<int:pk>',  TaskUpdate.as_view(), name='update'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete')
]