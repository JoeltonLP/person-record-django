from django.urls import path
from .views import _index

urlpatterns = [
    path('person', _index)
]