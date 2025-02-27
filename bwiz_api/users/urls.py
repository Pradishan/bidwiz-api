from django.urls import path
from . import views
from knox.views import LogoutView,LogoutAllView

urlpatterns = [
    # path('create-standard/', views.post),
    path('create-user/', views.CreateUserAPI.as_view()),
    path('update-user/<str:pk>', views.UpdateUserAPI.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),

]
#crate urls