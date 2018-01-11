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
        name='course'),
    url(r'^course/(?P<code>[0-9a-zA-Z]+)/review/$', tuview.review,
        name='review'),
    url(r'^accounts/login$', authviews.login, name='login'),
    url(r'^accounts/logout$', authviews.logout, {'next-page': '/'},
        name='logout'),
    url(r'^accounts/register$', tuview.register),
    url(r'^accounts/profile$', tuview.profile),
    url(r'^api/search$', turest.search)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
