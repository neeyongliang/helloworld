from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter14.views',
    url(r'^$', 'chapter_14', name="chapter_14"),
    url(r'^ex01/$', 'ex_1401', name="ex1401"),
    url(r'^ex02/$', 'ex_1402', name="ex1402"),
    url(r'^ex03/$', 'ex_1403', name="ex1403"),
    url(r'^ex04/$', 'ex_1404', name="ex1404"),
    url(r'^ex05/$', 'ex_1405', name="ex1405"),
    url(r'^ex06/$', 'ex_1406', name="ex1406"),
)
