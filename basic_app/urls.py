from django.urls import path
from . import views

urlpatterns=[
    path('', views.PostListView.as_view(), name = 'post_list'),
    path('post/predict', views.predict, name='predict'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish')
]
