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
    url(r'^course/(?P<code>[0-9a-zA-Z]{4,8})/$', tuview.course,
        name='course'),
    url(r'^course/(?P<code>[0-9a-zA-Z]{4,8})/review/$', tuview.review,
        name='review'),
    url(r'^course/(?P<code>[0-9a-zA-Z]{4,8})/thumbs/$', turest.thumbs, name='thumbs'),
    url(r'^accounts/login/$', authviews.login, name='login'),
    url(r'^accounts/logout/$', authviews.logout, {'next_page': '/'},
        name='logout'),
    url(r'^accounts/register$', tuview.register, name='register'),
    url(r'^accounts/profile/$', tuview.profile, name='profile'),
    url(r'^accounts/profile/thumbs/$', turest.thumbsProfile, name='profileThumbs'),
    url(r'^accounts/profile/(?P<username>.+)/thumbs/$', turest.thumbsUserprofile, name='userprofileThumbs'),
    url(r'^accounts/profile/(?P<username>.+)/$', tuview.userprofile, name='userprofile'),
    url(r'^api/search$', turest.search)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
