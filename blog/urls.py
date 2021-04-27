from django.urls import path
from .views import BlogView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, AddCommentView, CommentDeleteView

urlpatterns = [
    path('post/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post/post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('post/post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
    path('post/post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
    path('post/post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/', BlogListView.as_view(), name='home'),
    path('', BlogView.as_view(), name= 'firstpage'),

]


