"""shortener URL Configuration

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
from short_url import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    url(r'^log/admin/', admin.site.urls),
    # url(r'^(?P<Token>[\w-]+)/$', views.home),
    url(r'^home/$', views.home, name='home'),
    url(r'^game/$', views.game, name='game'),
    url(r'^crypto/$', views.crypto, name='crypto'),
    url(r'^article/(?P<slug>[\w-]+)/$', views.article, name='article'),
    url(r'^article/(?P<slug>[\w-]+)/(?P<Token>[\w-]+)/$', views.article, name='article2'),
    url(r'^search/$', views.search, name='search')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
