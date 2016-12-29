from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter21.views',
    url(r'^$', 'chapter_21', name="chapter_21"),
    url(r'^ex01/$', 'ex_2101', name="ex2101"),
    url(r'^ex02/$', 'ex_2102', name="ex2102"),
    url(r'^ex03/$', 'ex_2103', name="ex2103"),
    url(r'^ex04/$', 'ex_2104', name="ex2104"),
    url(r'^ex05/$', 'ex_2105', name="ex2105"),
    url(r'^ex06/$', 'ex_2106', name="ex2106"),
    url(r'^ex07/$', 'ex_2107', name="ex2107"),
)
