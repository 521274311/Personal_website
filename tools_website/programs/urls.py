
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.PythonView.as_view(), name='python3.7'),
    # url(r'^$', views.index, name='python3.7'),
    # url(r'^run_python', views.run_python, name='run_python'),
    url(r'^run_python', views.PythonView.as_view(), name='run_python'),
] + static(settings.USER_DATA_URL,document_root=settings.USER_DATA_ROOT)
