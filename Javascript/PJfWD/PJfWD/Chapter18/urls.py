from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter18.views',
    url(r'^$', 'chapter_18', name="chapter_18"),
    url(r'^ex01/$', 'ex_1801', name="ex1801"),
    url(r'^ex02/$', 'ex_1802', name="ex1802"),
    url(r'^ex03/$', 'ex_1803', name="ex1803"),
    url(r'^ex04/$', 'ex_1804', name="ex1804"),
)
