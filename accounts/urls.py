from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',views.login_view, name='login'),
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='accounts/forgot_password.html'),
         name='forgot_password'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

     path('dashboard/', views.dashboard, name='dashboard'),

    path('change-password/', login_required(auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html', success_url='/dashboard/')), name='change_password'),

     path('profile/', views.profile, name='profile'),

     path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
