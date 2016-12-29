from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter05.views',
    url(r'^$', 'chapter_05', name="chapter_05"),
    url(r'^ex01/$', 'ex_0501', name="ex0501"),
    url(r'^ex02/$', 'ex_0502', name="ex0502"),
    url(r'^ex03/$', 'ex_0503', name="ex0503"),
    url(r'^ex04/$', 'ex_0504', name="ex0504"),
    url(r'^ex05/$', 'ex_0505', name="ex0505"),
    url(r'^ex06/$', 'ex_0506', name="ex0506"),
    url(r'^ex07/$', 'ex_0507', name="ex0507"),
)
