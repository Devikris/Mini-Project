from django.urls import path

from authy.views import Signup, PasswordChange, PasswordChangeDone, EditProfile, custom_logout
from django.contrib.auth import views as authViews


urlpatterns = [
	path('profile/edit', EditProfile, name='edit-profile'),
	path('signup/', Signup, name='signup'),
	path('login/', authViews.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
	path('changepassword/', PasswordChange, name='change-password'),
	path('changepassword/done', PasswordChangeDone, name='change-password-done'),
	path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
	path('passwordreset/done', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('passwordreset/complete', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	
]