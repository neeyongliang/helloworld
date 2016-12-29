from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter07.views',
    url(r'^$', 'chapter_07', name="chapter_07"),
    url(r'^ex01/$', 'ex_0701', name="ex0701"),
    url(r'^ex02/$', 'ex_0702', name="ex0702"),
    url(r'^ex03/$', 'ex_0703', name="ex0703"),
    url(r'^ex04/$', 'ex_0704', name="ex0704"),
    url(r'^ex05/$', 'ex_0705', name="ex0705"),
)
