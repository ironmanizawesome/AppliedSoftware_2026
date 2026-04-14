from djaango.urls import path
from . import views

urlpatterns = [
    path("about/" , views.about_me),
    path('', views.landing),
]
