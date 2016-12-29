from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter01.views',
    url(r'^$', 'chapter_01', name="chapter_01"),
    url(r'^ex01$', 'chapter_01_ex_01', name="chapter_01_ex_01"),
    
)
