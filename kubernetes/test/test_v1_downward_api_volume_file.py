# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_downward_api_volume_file import V1DownwardAPIVolumeFile


class TestV1DownwardAPIVolumeFile(unittest.TestCase):
    """ V1DownwardAPIVolumeFile unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1DownwardAPIVolumeFile(self):
        """
        Test V1DownwardAPIVolumeFile
        """
        model = kubernetes.client.models.v1_downward_api_volume_file.V1DownwardAPIVolumeFile()


if __name__ == '__main__':
    unittest.main()
