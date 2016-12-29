from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter16.views',
    url(r'^$', 'chapter_16', name="chapter_16"),
    url(r'^ex01/$', 'ex_1601', name="ex1601"),
    url(r'^ex02/$', 'ex_1602', name="ex1602"),
    url(r'^ex03/$', 'ex_1603', name="ex1603"),
    url(r'^ex04/$', 'ex_1604', name="ex1604"),
    url(r'^ex05/$', 'ex_1605', name="ex1605"),
)
