from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.employee_add, name='employee_add'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='studentapp/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path('reports/', views.reports, name='reports'),
]