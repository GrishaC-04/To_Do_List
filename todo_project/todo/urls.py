from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("delete/<int:task_id>",views.delete_task, name="delete_task" ),
    path("complete/<int:task_id>",views.complete_task, name="complete_task" ),
    
]
