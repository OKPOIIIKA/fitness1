from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs_home, name='blogs_home'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:pk>', views.blogsDetailView.as_view(),name='blogs_detail'),
    path('<int:pk>/update', views.blogsUpdateView.as_view(),name='blogs_update'),
    path('<int:pk>/delete', views.blogsDeleteView.as_view(),name='blogs_delete')

]
