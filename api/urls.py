from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^biodigesters/$', views.BiodigesterList.as_view()),
    url(r'^biodigesters/(?P<pk>[0-9]+)/$', views.BiodigesterDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
