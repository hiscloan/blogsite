from django.urls import path
from .views import PostListView, PostDetailView, CommentUpdateView, AboutView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('about/', AboutView.as_view(), name='blog-about'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout')
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
