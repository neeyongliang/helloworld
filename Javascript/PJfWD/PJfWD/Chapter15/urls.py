from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter15.views',
    url(r'^$', 'chapter_15', name="chapter_15"),
    url(r'^ex01/$', 'ex_1501', name="ex1501"),
    url(r'^ex02/$', 'ex_1502', name="ex1502"),
    url(r'^ex03/$', 'ex_1503', name="ex1503"),
    url(r'^ex04/$', 'ex_1504', name="ex1504"),
)
