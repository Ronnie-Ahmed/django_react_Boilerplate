from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.UserView.as_view()),
    path('get/',views.GetUserView.as_view()),
    path('api/<int:pk>',views.GetSingleUserView.as_view()),
    path('get/<int:pk>',views.GetSingleUserView.as_view()),
    path('post/',views.PostUserView.as_view()),
]
