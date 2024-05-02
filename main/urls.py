from django.urls import path

from .views import index, other_page, BbLoginView, profile, BbLogoutView, ChangeUserInfoView, BbPasswordChangeView

app_name = 'main'

urlpatterns = [
    path('accounts/login/', BbLoginView.as_view(), name='login'),
    path('accounts/logout/', BbLogoutView.as_view(http_method_names=['post', 'get', 'options']), name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', BbPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('<str:page>', other_page, name='other'),
    path('', index, name='index')
]