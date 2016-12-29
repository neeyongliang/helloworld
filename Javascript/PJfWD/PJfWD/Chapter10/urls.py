from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter10.views',
    url(r'^$', 'chapter_10', name="chapter_10"),
    url(r'^ex01/$', 'ex_1001', name="ex1001"),
    url(r'^ex02/$', 'ex_1002', name="ex1002"),
    url(r'^ex03/$', 'ex_1003', name="ex1003"),
)
