from django.contrib import admin
from django.urls import re_path, path, include
from FirstPage import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin', admin.site.urls),
                  # path('profile_m', views.page_profile_manager),

                  re_path(r'profile', views.page_profile_ap),

                  re_path(r'^users_requests/', views.page_users_request),
                  re_path(r'^request/', views.page_create_request),
                  re_path(r'^search/', views.search_attr_by_name),
                  re_path(r'^filter/', views.filter_attr_mainpage),

                  re_path(r'attraction/', include('Attractions.urls')),
                  re_path(r'auth/', include('loginsys.urls')),

                  re_path(r'^$', views.main_page),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
