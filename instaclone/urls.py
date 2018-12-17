from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.timeline,name='timeline'),
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'^explore/', views.explore, name = 'expolre'),
    url(r'^profile/', views.profile, name = 'profile'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
