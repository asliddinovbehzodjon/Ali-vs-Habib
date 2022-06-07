from  django.urls import path
from .views import *
urlpatterns = [
    path('',alltodo),
    path('delete/<int:id>',deletetodo),
     path('edit/<int:id>',edittodo),
     path('donetodo/<int:id>',donetodo),
     path('register',registerPage,name='register'),
     path('login',loginPage,name='login'),
     path('logout',logout_view,name='logout')
]
