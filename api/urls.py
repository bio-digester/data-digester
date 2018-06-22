from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^samples/$', views.BiodigesterList.as_view()),
    url(r'^predict/$', views.Predict.as_view()),
    url(r'^optimize/$', views.Optimize.as_view()),
    url(r'^drop/$', views.Drop.as_view()),
    url(r'^samples/(?P<pk>[0-9]+)/$', views.BiodigesterDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
