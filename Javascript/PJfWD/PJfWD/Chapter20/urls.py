from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter20.views',
    url(r'^$', 'chapter_20', name="chapter_20"),
    url(r'^ex01/$', 'ex_2001', name="ex2001"),
    url(r'^ex02/$', 'ex_2002', name="ex2002"),
    url(r'^ex03/$', 'ex_2003', name="ex2003"),
)
