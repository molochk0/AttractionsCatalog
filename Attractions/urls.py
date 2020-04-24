from django.urls import re_path, path
from Attractions import views

urlpatterns = [

    # Первое приложение
    re_path(r'^moderation/(?P<id>\d+)/', views.page_attraction_moderation),
    re_path(r'^(?P<id>\d+)/', views.page_attraction),
    # re_path(r'^attraction_ap/(?P<id>)\d+$', views.page_attraction_ap),
    # path('attraction_m', views.page_attraction_moderation),

]
