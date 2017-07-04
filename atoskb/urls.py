from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_table, name='post_table'),
    url(r'post_list/', views.post_list, name='post_list'),
    url(r'edit_post/', views.edit_post, name='edit_post')
]