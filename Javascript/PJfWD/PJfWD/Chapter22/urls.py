from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter22.views',
    url(r'^$', 'chapter_22', name="chapter_22"),
    url(r'^ex01/$', 'ex_2201', name="ex2201"),
    url(r'^ex02/$', 'ex_2202', name="ex2202"),
    url(r'^ex03/$', 'ex_2203', name="ex2203"),
    url(r'^ex04/$', 'ex_2204', name="ex2204"),
    url(r'^ex05/$', 'ex_2205', name="ex2205"),
    url(r'^ex06/$', 'ex_2206', name="ex2206"),
)
