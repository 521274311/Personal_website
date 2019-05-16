
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^$', views.index),
    url(r'^run_python', views.run_python),
] + static(settings.USER_DATA_URL,document_root=settings.USER_DATA_ROOT)
