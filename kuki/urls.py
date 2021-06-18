from django.urls import path
from kuki import views


urlpatterns=[
    path('',views.index,name="home"),
    path('get/<stri>/',views.indexd,name="get"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.my_profile_view, name='my'),
    path('detail/', views.detail, name="detail"),

    
]