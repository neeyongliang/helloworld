"""PJfWD URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
import settings
from views import home, tables, framesetExample, topFrame, leftFrame, rightFrame, blueFrame, redFrame, form1, richtext, blank

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon.ico$', RedirectView.as_view(url=settings.STATIC_URL+'images/favicon.ico')),
    url(r'^$', home, name='home'),
]

# catalog
urlpatterns += [
    # Ajax
    url(r'api/', include('PJfWD.api.urls')),
    # Chapter
    url(r'ch01/', include('PJfWD.Chapter01.urls')),
    url(r'ch02/', include('PJfWD.Chapter02.urls')),
    url(r'ch03/', include('PJfWD.Chapter03.urls')),
    url(r'ch04/', include('PJfWD.Chapter04.urls')),
    url(r'ch05/', include('PJfWD.Chapter05.urls')),
    url(r'ch06/', include('PJfWD.Chapter06.urls')),
    url(r'ch07/', include('PJfWD.Chapter07.urls')),
    url(r'ch08/', include('PJfWD.Chapter08.urls')),
    url(r'ch09/', include('PJfWD.Chapter09.urls')),
    url(r'ch10/', include('PJfWD.Chapter10.urls')),
    url(r'ch11/', include('PJfWD.Chapter11.urls')),
    url(r'ch12/', include('PJfWD.Chapter12.urls')),
    url(r'ch13/', include('PJfWD.Chapter13.urls')),
    url(r'ch14/', include('PJfWD.Chapter14.urls')),
    url(r'ch15/', include('PJfWD.Chapter15.urls')),
    url(r'ch16/', include('PJfWD.Chapter16.urls')),
    url(r'ch17/', include('PJfWD.Chapter17.urls')),
    url(r'ch18/', include('PJfWD.Chapter18.urls')),
    url(r'ch19/', include('PJfWD.Chapter19.urls')),
    url(r'ch20/', include('PJfWD.Chapter20.urls')),
    url(r'ch21/', include('PJfWD.Chapter21.urls')),
    url(r'ch22/', include('PJfWD.Chapter22.urls')),
]

# element
urlpatterns += [
    url(r'^elements$', tables, name="elements_tables" ),
    url(r'^framesetExample$', framesetExample, name="elements_frame"),
    url(r'^topFrame$', topFrame, name="elements_topFrame"),
    url(r'^leftFrame$', leftFrame, name="elements_leftFrame"),
    url(r'^rightFrame$', rightFrame, name="elements_rightFrame"),
    url(r'^redFrame$', redFrame, name="elements_redFrame"),
    url(r'^blueFrame$', blueFrame, name="elements_blueFrame"),
    url(r'^forms$', form1, name="elements_forms"),
    url(r'^richtext$', richtext, name="elements_richtext"),
    url(r'^blank', blank, name="elements_blank"),
]
