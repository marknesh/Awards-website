from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('home2/', views.home, name="home2"),
    re_path(r'^update/profile', views.updatemyprofile, name='update_profile'),
    re_path(r'^update/project', views.updatemyprojects, name='update_projects'),
    path('profile/', views.myprofile, name='profile'),
    re_path(r'^project/(\d+)', views.editproject, name='article'),
    path('search/', views.search_project, name='search_results'),
    path('create/', views.create, name='create'),
    path('vote/<poll_id>/', views.vote, name='vote'),
    path('results/<poll_id>/', views.results, name='results'),
    re_path(r'^api/profileAPI/$', views.MerchList.as_view(),name="profileapi"),
    re_path(r'^api/projectAPI/$', views.MerchList2.as_view(), name="projectapi")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
