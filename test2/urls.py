from django.urls import path
from firstapp import views
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('gm_ipadr/', views.gm_ipadr),
    path('list/<int:id>/', views.list),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
]
