from __future__ import absolute_import

from django.conf.urls import patterns, url

from .api import (APIStagingSourceListView, APIStagingSourceView,
    APIStagingSourceFileView, APIStagingSourceFileImageView)
from .literals import (SOURCE_CHOICE_WEB_FORM, SOURCE_CHOICE_STAGING,
    SOURCE_CHOICE_WATCH)
from .wizards import DocumentCreateWizard

urlpatterns = patterns('sources.views',
    url(r'^staging_file/(?P<staging_folder_pk>\d+)/(?P<filename>.+)/delete/$', 'staging_file_delete', name='staging_file_delete'),

    url(r'^upload/document/new/interactive/(?P<source_type>\w+)/(?P<source_id>\d+)/$', 'upload_interactive', (), 'upload_interactive'),
    url(r'^upload/document/new/interactive/$', 'upload_interactive', (), 'upload_interactive'),

    url(r'^upload/document/(?P<document_pk>\d+)/version/interactive/(?P<source_type>\w+)/(?P<source_id>\d+)/$', 'upload_interactive', (), 'upload_version'),
    url(r'^upload/document/(?P<document_pk>\d+)/version/interactive/$', 'upload_interactive', (), 'upload_version'),

    # Setup views

    url(r'^setup/interactive/%s/list/$' % SOURCE_CHOICE_WEB_FORM, 'setup_source_list', {'source_type': SOURCE_CHOICE_WEB_FORM}, 'setup_web_form_list'),
    url(r'^setup/interactive/%s/list/$' % SOURCE_CHOICE_STAGING, 'setup_source_list', {'source_type': SOURCE_CHOICE_STAGING}, 'setup_staging_folder_list'),
    url(r'^setup/interactive/%s/list/$' % SOURCE_CHOICE_WATCH, 'setup_source_list', {'source_type': SOURCE_CHOICE_WATCH}, 'setup_watch_folder_list'),

    url(r'^setup/interactive/(?P<source_type>\w+)/list/$', 'setup_source_list', (), 'setup_source_list'),
    url(r'^setup/interactive/(?P<source_type>\w+)/(?P<source_id>\d+)/edit/$', 'setup_source_edit', (), 'setup_source_edit'),
    url(r'^setup/interactive/(?P<source_type>\w+)/(?P<source_id>\d+)/delete/$', 'setup_source_delete', (), 'setup_source_delete'),
    url(r'^setup/interactive/(?P<source_type>\w+)/create/$', 'setup_source_create', (), 'setup_source_create'),

    url(r'^setup/interactive/(?P<source_type>\w+)/(?P<source_id>\d+)/transformation/list/$', 'setup_source_transformation_list', (), 'setup_source_transformation_list'),
    url(r'^setup/interactive/(?P<source_type>\w+)/(?P<source_id>\d+)/transformation/create/$', 'setup_source_transformation_create', (), 'setup_source_transformation_create'),
    url(r'^setup/interactive/source/transformation/(?P<transformation_id>\d+)/edit/$', 'setup_source_transformation_edit', (), 'setup_source_transformation_edit'),
    url(r'^setup/interactive/source/transformation/(?P<transformation_id>\d+)/delete/$', 'setup_source_transformation_delete', (), 'setup_source_transformation_delete'),

    # Document create views

    url(r'^create/from/local/multiple/$', DocumentCreateWizard.as_view(), name='document_create_multiple'),
    url(r'^(?P<document_id>\d+)/create/siblings/$', 'document_create_siblings', (), 'document_create_siblings'),
)

api_urls = patterns('',
    url(r'^staging_folders/file/(?P<staging_folder_pk>[0-9]+)/(?P<filename>.+)/image/$', APIStagingSourceFileImageView.as_view(), name='stagingfolderfile-image-view'),
    url(r'^staging_folders/file/(?P<staging_folder_pk>[0-9]+)/(?P<filename>.+)/$', APIStagingSourceFileView.as_view(), name='stagingfolderfile-detail'),
    url(r'^staging_folders/$', APIStagingSourceListView.as_view(), name='stagingfolder-list'),
    url(r'^staging_folders/(?P<pk>[0-9]+)/$', APIStagingSourceView.as_view(), name='stagingfolder-detail')
)
