from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home),
    path('category/<int:category_id>', category, name='category'),
    path('post/<int:post_id>', last_post, name='post'),
]
