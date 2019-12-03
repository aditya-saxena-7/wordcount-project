
from . import views
from django.urls import path

urlpatterns = [
   
   path('page2/', views.homepage, name= 'home'),
   path('count/', views.count, name='count'),
   path('about/', views.about, name= 'about'),
]
