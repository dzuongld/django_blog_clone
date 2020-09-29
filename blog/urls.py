from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete',
         views.PostDeleteView.as_view(),
         name='post_delete'),
    path('dafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment/',
         views.add_comment_to_post,
         name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',
         views.approve_comment,
         name='approve_comment'),
    path('comment/<int:pk>/delete/',
         views.remove_comment,
         name='remove_comment'),
    path('post/<int:pk>/publish/', views.publish_post, name='publish_post'),
]
