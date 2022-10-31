from django.urls import path
from . import views

urlpatterns = [
    path('b/',views.home,name="home"),
    path('c/',views.success,name="success"),
    path('d/',views.details,name="details"),
    path('delete/<int:id>',views.delete,name="delete")
]