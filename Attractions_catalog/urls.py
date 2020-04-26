from django.contrib import admin
from django.urls import re_path, path, include
from FirstPage import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Attractions import views as atrviews

extrapatternsRequests = [
                            re_path(r'^page/(?P<page_number>\d+)/$', views.page_users_request),
                            re_path('', views.page_users_request),
                        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

extrapatternsSearch = [
                          re_path(r'^page/(?P<page_number>\d+)/$', views.search_attr_by_name),
                          re_path('', views.search_attr_by_name),
                      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

extrapatternsFilter = [
                          re_path(r'^page/(?P<page_number>\d+)/$', views.filter_attr_mainpage),
                          re_path('', views.filter_attr_mainpage),
                      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
                  path('admin', admin.site.urls),

                  re_path(r'profile', views.page_profile_ap),

                  re_path(r'^users_requests/', include(extrapatternsRequests)),  #
                  re_path(r'^request/', views.page_create_request),
                  re_path(r'^search/', include(extrapatternsSearch)),  #
                  re_path(r'^filter/', include(extrapatternsFilter)),  #
                  re_path(r'^accept_request/', atrviews.accept_request),
                  re_path(r'^decline_request/', atrviews.decline_request),

                  re_path(r'attraction/', include('Attractions.urls')),
                  re_path(r'auth/', include('loginsys.urls')),

                  re_path(r'^page/(\d+)/$', views.main_page),

                  re_path(r'^$', views.main_page),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
