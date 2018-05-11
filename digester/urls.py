from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Data digester API')
#router = routers.DefaultRouter()
#router.register(r'biodigesters', BiodigestersViewSet, base_name='biodigesters')

urlpatterns = [
    url(r'^$', schema_view),
    #url(r'^api/', include(router.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
]
