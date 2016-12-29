from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter06.views',
    url(r'^$', 'chapter_06', name="chapter_06"),
    url(r'^ex01/$', 'ex_0601', name="ex0601"),
    url(r'^ex02/$', 'ex_0602', name="ex0602"),
    url(r'^ex03/$', 'ex_0603', name="ex0603"),
    url(r'^ex04/$', 'ex_0604', name="ex0604"),
)
