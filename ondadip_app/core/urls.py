from django.urls import path

from . import views


app_name = 'core'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('user/<int:pk>/', views.UserView.as_view(), name='user'),
    path('security/<int:pk>/', views.SecurityView.as_view(), name='security'),
    path('user/<int:pk>/portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('user/<int:user_id>/portfolio/add/', views.security_add, name='security_add'),
    path('user/<int:pk>/portfolio/security_added/', views.SecurityAddedView.as_view(), name='security_added')
]