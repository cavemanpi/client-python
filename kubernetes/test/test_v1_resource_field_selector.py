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
from kubernetes.client.models.v1_resource_field_selector import V1ResourceFieldSelector


class TestV1ResourceFieldSelector(unittest.TestCase):
    """ V1ResourceFieldSelector unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ResourceFieldSelector(self):
        """
        Test V1ResourceFieldSelector
        """
        model = kubernetes.client.models.v1_resource_field_selector.V1ResourceFieldSelector()


if __name__ == '__main__':
    unittest.main()
