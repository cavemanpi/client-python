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
from kubernetes.client.models.v1_delete_options import V1DeleteOptions


class TestV1DeleteOptions(unittest.TestCase):
    """ V1DeleteOptions unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1DeleteOptions(self):
        """
        Test V1DeleteOptions
        """
        model = kubernetes.client.models.v1_delete_options.V1DeleteOptions()


if __name__ == '__main__':
    unittest.main()
