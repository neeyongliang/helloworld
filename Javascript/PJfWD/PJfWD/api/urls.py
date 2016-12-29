from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('PJfWD.api.views',
    url(r'^$', 'api', name="apiList"),
    url(r'^testforget$', 'testforget', name="testforget"),
)
