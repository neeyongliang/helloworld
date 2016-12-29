from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter13.views',
    url(r'^$', 'chapter_13', name="chapter_13"),
    url(r'^ex01/$', 'ex_1301', name="ex1301"),
    url(r'^ex02/$', 'ex_1302', name="ex1302"),
    url(r'^ex03/$', 'ex_1303', name="ex1303"),
    url(r'^ex04/$', 'ex_1304', name="ex1304"),
    url(r'^ex05/$', 'ex_1305', name="ex1305"),
    url(r'^ex06/$', 'ex_1306', name="ex1306"),
    url(r'^ex07/$', 'ex_1307', name="ex1307"),
)
