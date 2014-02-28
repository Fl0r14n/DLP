from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DLP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),    
)

from survey import views as sv

urlpatterns += patterns('',
    url(r'^$', sv.home),
    url(r'^survey/$', sv.show_forms),
    url(r'^survey/form/(\d+)/$', sv.fill_form),    
    url(r'^survey/result/(?P<form_id>(\d+))?/?$', sv.show_results),
)