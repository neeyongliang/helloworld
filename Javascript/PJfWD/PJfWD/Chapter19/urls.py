from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.Chapter19.views',
    url(r'^$', 'chapter_19', name="chapter_19"),
)
