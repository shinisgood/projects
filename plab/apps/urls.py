from distutils.log import Log
from django.urls import path, include
from dj_rest_auth.urls import LoginView
from dj_rest_auth.registration.views import RegisterView

# from .resources import products
urlpatterns = [
    #### 유저
    path("signin/", LoginView.as_view()), # 로그인
    path("signup/", RegisterView.as_view()), # 회원가입
]