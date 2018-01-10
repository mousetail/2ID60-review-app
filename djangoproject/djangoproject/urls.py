"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as authviews
from django.conf import settings

from tureview import views as tuview
from tureview import rest as turest
urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', tuview.home, name='home'),
    url(r'^search', tuview.search, name='search'),
    url(r'^course/(?P<code>[0-9a-zA-Z]+)/$', tuview.course,
        name='course'), #note to convert to upper case
    url(r'^course/(?P<code>[0-9a-zA-Z]+)/review/$', tuview.review,
        name='review'),
    url(r'^accounts/login$', authviews.login, name='login'),
    url(r'^accounts/logout$', authviews.logout, {'next-page': '/'},
        name='logout'),
    url(r'^accounts/register$', tuview.register),
    url(r'^api/search$', turest.search)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
