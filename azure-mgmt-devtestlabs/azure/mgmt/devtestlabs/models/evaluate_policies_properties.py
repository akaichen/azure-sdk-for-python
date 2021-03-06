# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EvaluatePoliciesProperties(Model):
    """Properties for evaluating a policy set.

    :param fact_name: The fact name.
    :type fact_name: str
    :param fact_data: The fact data.
    :type fact_data: str
    :param value_offset: The value offset.
    :type value_offset: str
    """ 

    _attribute_map = {
        'fact_name': {'key': 'factName', 'type': 'str'},
        'fact_data': {'key': 'factData', 'type': 'str'},
        'value_offset': {'key': 'valueOffset', 'type': 'str'},
    }

    def __init__(self, fact_name=None, fact_data=None, value_offset=None):
        self.fact_name = fact_name
        self.fact_data = fact_data
        self.value_offset = value_offset
