from django.urls import re_path, path
from Attractions import views

urlpatterns = [

    re_path(r'^moderation/(?P<id>\d+)/', views.page_attraction_moderation),
    re_path(r'(?P<id>\d+)/set_mark/', views.set_mark),
    re_path(r'^(?P<id>\d+)/', views.page_attraction),

]
