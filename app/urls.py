from  django.urls import path
from .views import *
urlpatterns = [
    path('',alltodo),
    path('delete/<int:id>',deletetodo),
     path('edit/<int:id>',edittodo),
     path('donetodo/<int:id>',donetodo)
]
