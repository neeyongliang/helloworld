from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter11.views',
    url(r'^$', 'chapter_11', name="chapter_11"),
    url(r'^ex01/$', 'ex_1101', name="ex1101"),
    url(r'^ex02/$', 'ex_1102', name="ex1102"),
    url(r'^ex03/$', 'ex_1103', name="ex1103"),
    url(r'^ex04/$', 'ex_1104', name="ex1104"),
    url(r'^ex05/$', 'ex_1105', name="ex1105"),
)
