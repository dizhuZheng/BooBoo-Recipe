from django.urls import path
from django.views.generic import TemplateView
from .views import image_view, success, PostDetailView, PostListView, CommentCreateView, CommentDeleteView, CreateRecipeView, PostEditView, PostDeleteView

app_name = 'posts'

urlpatterns = [
    path('', TemplateView.as_view(template_name="recipes/recipes_home.html"), name='recipes_home'),
    path('a/', image_view.as_view(), name='image_upload'),
    path('success/', success, name='success'),
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('create/', CreateRecipeView.as_view(), name='create'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<slug:slug>/update_post/', PostEditView.as_view(), name='update_post'),
    path('posts/<slug:slug>/add_comment/', CommentCreateView.as_view(), name='add_comment'),
    path('posts/<slug:slug>/delete_comment/<int:pk>/', CommentDeleteView.as_view(), name='delete_comment'),
    path('posts/<slug:slug>/delete_post/', PostDeleteView.as_view(), name='delete_post'),
]
