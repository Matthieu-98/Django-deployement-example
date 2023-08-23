from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('page_resto',views.page_resto, name='resto'),
]