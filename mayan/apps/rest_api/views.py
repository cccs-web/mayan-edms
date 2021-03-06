"""Views file for the rest_api app"""
from __future__ import absolute_import

import logging

from django.utils.translation import ugettext_lazy as _

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .classes import APIEndPoint

logger = logging.getLogger(__name__)

registered_version_0_endpoints = [
]


class APIBase(generics.GenericAPIView):
    """
    Main entry point of the API.
    """

    def get(self, request, format=None):
        return Response([
            {'name': 'Version 0', 'url': reverse('api-version-0', request=request, format=format)}
        ])


class Version_0(generics.GenericAPIView):
    """
    API version 0 entry points.
    """

    def get(self, request, format=None):
        return Response({
            'apps': [
                {'name': unicode(endpoint), 'url': reverse('api-version-0-app', args=[unicode(endpoint)], request=request, format=format)} for endpoint in APIEndPoint.get_all()
            ],
        })


class APIAppView(generics.GenericAPIView):
    """
    Entry points of the selected app.
    """

    def get(self, request, app_name, format=None):
        result = []

        api_app = APIEndPoint.get(app_name)
        for endpoint in api_app.endpoints:
            result.append(
                {
                    'description': endpoint['description'],
                    'url': reverse(endpoint['view_name'], request=request, format=format),
                }
            )

        return Response({
            'endpoints': result
        })
