from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('delete/<int:id>/',views.delete_data , name="deletestudent"),
    path('update/<int:id>/',views.update_data , name="updatedata ")


]