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
from kubernetes.client.models.v1_container_state_terminated import V1ContainerStateTerminated


class TestV1ContainerStateTerminated(unittest.TestCase):
    """ V1ContainerStateTerminated unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ContainerStateTerminated(self):
        """
        Test V1ContainerStateTerminated
        """
        model = kubernetes.client.models.v1_container_state_terminated.V1ContainerStateTerminated()


if __name__ == '__main__':
    unittest.main()
