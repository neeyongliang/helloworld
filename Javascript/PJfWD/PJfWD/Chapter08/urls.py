from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter08.views',
    url(r'^$', 'chapter_08', name="chapter_08"),
    url(r'^ex01/$', 'ex_0801', name="ex0801"),
    url(r'^ex02/$', 'ex_0802', name="ex0802"),
    url(r'^ex03/$', 'ex_0803', name="ex0803"),
    url(r'^ex04/$', 'ex_0804', name="ex0804"),
    url(r'^ex05/$', 'ex_0805', name="ex0805"),
    url(r'^ex06/$', 'ex_0806', name="ex0806"),
)
