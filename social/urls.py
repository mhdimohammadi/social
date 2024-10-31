from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = "social"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name="login"),
    path('logout/', views.log_out, name="logout"),
    path('', views.profile, name="profile"),
    path('register/', views.register, name='register'),
    path('user/edit', views.edit_user, name='edit_account'),
    path('ticket', views.ticket, name='ticket'),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url='done'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url='done'), name="password_reset"),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(success_url='/blog/password_reset/complete'),
         name="password_reset_confirm"),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('posts/', views.post_list, name="post_list"),
    path('posts/<slug:tag_slug>/', views.post_list, name='posts_by_tag'),
    path('posts/post/create_post', views.create_post, name="create_post"),
    path('posts/<int:id>', views.post_detail, name="post_detail"),
    path('edit_post/<post_id>', views.edit_post, name="edit_post"),
    path('profile/delete_post/<post_id>', views.delete_post, name="delete_post"),
    path('like_post/', views.like_post, name="like_post"),
    path('saved_post/', views.save_post, name="save_post"),
    path('users/', views.user_list, name='user_list'),
    path('users/<username>/', views.user_detail, name='user_detail'),
    path('follow/', views.user_follow, name="user_follow"),
    path('users/<username>/follow_list/', views.follow_list, name="follow_list")
]
