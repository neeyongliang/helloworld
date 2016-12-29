from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter09.views',
    url(r'^$', 'chapter_09', name="chapter_09"),
    url(r'^ex01/$', 'ex_0901', name="ex0901"),
    url(r'^ex02/$', 'ex_0902', name="ex0902"),
    url(r'^ex03/$', 'ex_0903', name="ex0903"),
    url(r'^ex04/$', 'ex_0904', name="ex0904"),
)
