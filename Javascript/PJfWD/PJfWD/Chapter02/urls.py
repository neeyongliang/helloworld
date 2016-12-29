from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter02.views',
    url(r'^$', 'chapter_02', name="chapter_02"),
    url(r'^ex01$', 'chapter_02_ex_01', name="chapter_02_ex_01"),
    url(r'^ex02$', 'chapter_02_ex_02', name="chapter_02_ex_02"),
)
