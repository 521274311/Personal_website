from django.conf.urls import include, url
from . import views
urlpatterns = [
    # ... snip ...
    url(r'^$', views.index, name='index'),
    url(r'^doc/',views.doc, name='doc'),
]