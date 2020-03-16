from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage,name="homepage"),
    re_path(r'^update/profile', views.updatemyprofile, name='update_profile'),
    re_path(r'^update/project', views.updatemyprojects, name='update_projects'),
    path('profile/', views.myprofile, name='profile'),
    re_path(r'^project/(\d+)', views.editproject, name='article'),
    path('search/', views.search_user, name='search_results'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
