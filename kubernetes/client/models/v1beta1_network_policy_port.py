# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1NetworkPolicyPort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, port=None, protocol=None):
        """
        V1beta1NetworkPolicyPort - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'port': 'IntstrIntOrString',
            'protocol': 'str'
        }

        self.attribute_map = {
            'port': 'port',
            'protocol': 'protocol'
        }

        self._port = port
        self._protocol = protocol

    @property
    def port(self):
        """
        Gets the port of this V1beta1NetworkPolicyPort.
        If specified, the port on the given protocol.  This can either be a numerical or named port on a pod.  If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched.

        :return: The port of this V1beta1NetworkPolicyPort.
        :rtype: IntstrIntOrString
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this V1beta1NetworkPolicyPort.
        If specified, the port on the given protocol.  This can either be a numerical or named port on a pod.  If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched.

        :param port: The port of this V1beta1NetworkPolicyPort.
        :type: IntstrIntOrString
        """

        self._port = port

    @property
    def protocol(self):
        """
        Gets the protocol of this V1beta1NetworkPolicyPort.
        Optional.  The protocol (TCP or UDP) which traffic must match. If not specified, this field defaults to TCP.

        :return: The protocol of this V1beta1NetworkPolicyPort.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this V1beta1NetworkPolicyPort.
        Optional.  The protocol (TCP or UDP) which traffic must match. If not specified, this field defaults to TCP.

        :param protocol: The protocol of this V1beta1NetworkPolicyPort.
        :type: str
        """

        self._protocol = protocol

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
