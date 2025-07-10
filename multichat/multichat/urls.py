from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

# from chat.views import index
# from . import views


# urlpatterns = [
#     path('', index),
#     path('accounts/login/', LoginView.as_view(), name='login'),
#     path('accounts/logout/', LogoutView.as_view(), name='logout'),
#     path('admin/', admin.site.urls),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    path('', include('chat.urls')),
]

# urlpatterns = [
#     path('', views.lobby, name='lobby'),
#     path('<str:room_name>/', views.room, name='room'),
# ]