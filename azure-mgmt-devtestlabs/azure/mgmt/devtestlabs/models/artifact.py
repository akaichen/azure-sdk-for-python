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


class Artifact(Model):
    """An artifact.

    :param title: The title of the artifact.
    :type title: str
    :param description: The description of the artifact.
    :type description: str
    :param file_path: The file path of the artifact.
    :type file_path: str
    :param icon: The icon of the artifact.
    :type icon: str
    :param target_os_type: Gets or sets the type of the target os.
    :type target_os_type: str
    :param parameters: The parameters of the artifact.
    :type parameters: object
    :param id: The identifier of the resource.
    :type id: str
    :param name: The name of the resource.
    :type name: str
    :param type: The type of the resource.
    :type type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict
    """ 

    _attribute_map = {
        'title': {'key': 'properties.title', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'file_path': {'key': 'properties.filePath', 'type': 'str'},
        'icon': {'key': 'properties.icon', 'type': 'str'},
        'target_os_type': {'key': 'properties.targetOsType', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, title=None, description=None, file_path=None, icon=None, target_os_type=None, parameters=None, id=None, name=None, type=None, location=None, tags=None):
        self.title = title
        self.description = description
        self.file_path = file_path
        self.icon = icon
        self.target_os_type = target_os_type
        self.parameters = parameters
        self.id = id
        self.name = name
        self.type = type
        self.location = location
        self.tags = tags
