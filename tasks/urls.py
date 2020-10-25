from django.urls import path
#from . import views
# from .views import SignUpView
# from .views import PasswordChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('changePassword/', auth_views.PasswordChangeView.as_view
    # (template_name = 'registration/changePassword.html',success_url = '/'), name='changePassword'),
]
