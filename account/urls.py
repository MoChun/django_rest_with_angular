from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from account import views


urlpatterns=[
    url(r'^$',views.login_view,name='render_login_view'),
]