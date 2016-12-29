from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter12.views',
    url(r'^$', 'chapter_12', name="chapter_12"),
    url(r'^ex01/$', 'ex_1201', name="ex1201"),
    url(r'^ex02/$', 'ex_1202', name="ex1202"),
    url(r'^ex03/$', 'ex_1203', name="ex1203"),
    url(r'^ex04/$', 'ex_1204', name="ex1204"),
    url(r'^ex05/$', 'ex_1205', name="ex1205"),
)
