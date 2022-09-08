from django.urls import path 
from . import views
# ######:80000/other
urlpatterns = [
    path('',views.simple_view)
]