from django.urls import path
from .views import PostListView, PostDetailView, CommentUpdateView, AboutView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('about/', AboutView.as_view(), name='blog-about'),    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

