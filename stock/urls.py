"""stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rose.views import Rose, Harden
from optional.views import Optional, CheckCode, KLine
from limitup.views import LimitUp
from django.views.generic import TemplateView
from django.views import static
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^rose/$', Rose.as_view(), name='Rose'),
    url(r'^optional/$', Optional.as_view(), name='Optional'),
    url(r'^check/$', CheckCode.as_view(), name='CheckCode'),
    url(r'^kline/$', KLine.as_view(), name='KLine'),
    url(r'^limitup/$', LimitUp.as_view(), name='LimitUp'),
    url(r'^harden/$', Harden.as_view(), name='Harden'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
