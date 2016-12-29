from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter17.views',
    url(r'^$', 'chapter_17', name="chapter_17"),
    url(r'^ex01/$', 'ex_1701', name="ex1701"),
    url(r'^ex02/$', 'ex_1702', name="ex1702"),
    url(r'^ex03/$', 'ex_1703', name="ex1703"),
    url(r'^ex04/$', 'ex_1704', name="ex1704"),
    url(r'^ex05/$', 'ex_1705', name="ex1705"),
)
