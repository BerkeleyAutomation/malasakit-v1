"""
This module defines how URLs should route to views.
"""

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

# pylint: disable=invalid-name
app_name = 'pcari'
urlpatterns = [
    # User-facing views
    url(r'^$', views.index, name='index'),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^personal-information/$', views.personal_information,
        name='personal-information'),
    url(r'^quantitative-questions/$', views.quantitative_questions,
        name='quantitative-questions'),
    url(r'^response-histograms/$', views.response_histograms,
        name='response-histograms'),
    url(r'^rate-comments/$', views.rate_comments, name='rate-comments'),
    url(r'^qualitative-questions/$', views.qualitative_questions,
        name='qualitative-questions'),
    url(r'^end/$', views.end, name='end'),

    # ServiceWorker script- special case
    url(r'^sw.js$',
        TemplateView.as_view(template_name='sw.js',
                             content_type='application/javascript'),
        name='sw.js'),

    # AJAX endpoints
    url(r'^fetch-comments/$', views.fetch_comments, name='fetch-comments'),
    url(r'^fetch-qualitative-questions/$', views.fetch_qualitative_questions,
        name='fetch-qualitative-questions'),
    url(r'^save-response/$', views.save_response, name='save-response'),
]