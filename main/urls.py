from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('new_blog', views.new_blog, name='new_blog'),
    path('create', views.create, name='create'),
    path('blog', views.blogpage, name='blogpage'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('edit/<int:post_id>', views.edit, name='edit'),
    path('update/<int:post_id>', views.update, name='update'),
    path('delete/<int:post_id>', views.delete, name='delete'),
]