from django.urls import re_path
from Attractions_Catalog_App.loginsys.views import *

urlpatterns = [
    re_path(r'^login/$', login),
    re_path(r'^logout/$', logout),
    re_path(r'^registration/$', register),
]
