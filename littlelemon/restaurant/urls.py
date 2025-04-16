#define URL route for index() view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menuitem'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
