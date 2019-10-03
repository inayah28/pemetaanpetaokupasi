from django.conf.urls import url
from . import views

urlpatterns=[
# r=row

    url(r'^$',views.index),
]