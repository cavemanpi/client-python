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
from kubernetes.client.models.v1_persistent_volume_claim_volume_source import V1PersistentVolumeClaimVolumeSource


class TestV1PersistentVolumeClaimVolumeSource(unittest.TestCase):
    """ V1PersistentVolumeClaimVolumeSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1PersistentVolumeClaimVolumeSource(self):
        """
        Test V1PersistentVolumeClaimVolumeSource
        """
        model = kubernetes.client.models.v1_persistent_volume_claim_volume_source.V1PersistentVolumeClaimVolumeSource()


if __name__ == '__main__':
    unittest.main()
