from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'charts.views.chart_index', name='chart_index'),
    url(r'^total_incomes/$', 'charts.views.total_incomes', name='total_incomes'),
    url(r'^incomes/(?P<year>\d{4})/(?P<scope>\S+)$', 'charts.views.incomes_by_year_and_scope', name='incomes_by_year_and_scope'),
    url(r'^incomes/(?P<year>\d{4})$', 'charts.views.incomes_by_year', name='incomes_by_year'),
    url(r'^incomes_by_project/$', 'charts.views.incomes_by_project_index', name='incomes_by_project_index'),
    url(r'^incomes_by_project/(?P<project_slug>\S+)$', 'charts.views.incomes_by_project', name='incomes_by_project'),
)

urlpatterns += staticfiles_urlpatterns()
