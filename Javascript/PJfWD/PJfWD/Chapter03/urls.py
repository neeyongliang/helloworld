from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter03.views',
    url(r'^$', 'chapter_03', name="chapter_03"),
    url(r'^ex01', 'chapter_03_ex_01', name="chapter_03_ex_01"),
    
)
