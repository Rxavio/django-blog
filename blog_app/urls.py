from django.urls import path
from .views import (
    # HomeList,
	# HomeDetail,
    NewPostView,
    PostDelView,
    PostUpdateView,
    UserPostView,
    # AddCommentView
        
)
from . import views
#from .views import video

urlpatterns = [
    # path('', HomeList.as_view(), name='home'),
    path('', views.home, name="home"),
    path('detail/<int:pk>/', views.post_detail, name='post-detail'),

    # path('detail/<int:pk>/', HomeDetail.as_view(), name='detail'),
    path('new-post/', NewPostView.as_view(), name='new-post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDelView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostView.as_view(), name='user-posts'),

    # path('detail/<int:pk>/comment', AddCommentView.as_view(), name='add-comment'),


    path('like/', views.like_post, name="like_post"),

    path('favourites/', views.post_favourite_list, name="post_favourite_list"),
    path('post/<int:pk>/favourite_post/', views.favourite_post, name="favourite_post"),

    #path('how-it-works/', video)
    path('how-it-works/', views.video, name="how-it-works"),
 
    
]
