
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='new'),
    path('blog/',views.blog,name='blog'),
    path('single/',views.single_blog,name='single'),

]


