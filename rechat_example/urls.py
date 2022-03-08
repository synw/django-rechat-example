from django.urls import path

from .views import LoginView, IndexView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("", IndexView.as_view()),
]
