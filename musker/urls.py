from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('profile_list/', views.ProfileList, name='profile-list'),
    path('profile/<int:pk>/', views.ProfileView, name='profile-view'),
    path('login/', views.login_user, name="login"),
    path('logout', views.logout_user, name='logout'),
    path('register/', views.RegisterView, name='register'),
    path('Update_register/', views.UpdateUser, name='update-register'),
    path('meep_likes/<int:pk>', views.MeepLiks, name='meep-likes'),
    path('meep_show/<int:pk>', views.MeepShow, name='meep-show'),

]
