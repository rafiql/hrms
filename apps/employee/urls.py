#from django.conf.urls import url, include
from django.urls import re_path as url
from . import api
from django.conf import settings
from django.conf.urls.static import static


app_name = 'apps.employee'


urlpatterns = [

    url(r'^api/create-employee/$', api.UserViewSet.as_view(), name='emp_create'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
