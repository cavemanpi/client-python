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
from kubernetes.client.models.v1_scale_status import V1ScaleStatus


class TestV1ScaleStatus(unittest.TestCase):
    """ V1ScaleStatus unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ScaleStatus(self):
        """
        Test V1ScaleStatus
        """
        model = kubernetes.client.models.v1_scale_status.V1ScaleStatus()


if __name__ == '__main__':
    unittest.main()
