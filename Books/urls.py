from django.urls import path
from .views import Home,Title

urlpatterns = [
    path ('', Home, name='home'),
    path('/title',Title,name='title')
]
