# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 Investoday company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from jrtzcloudsdkcore.abstract_model import AbstractModel


class PatchProjectRequest(AbstractModel):
    """PatchProject 请求参数结构体
    """
    def __init__(self):
        self.Patch = None

    def _deserialize(self, params):
        if params.get("Patch") is not None:
            self.Patch = []
            for item in params.get("Patch"):
                obj = Patch()
                obj._deserialize(item)
                self.Patch.append(obj)


class Patch(AbstractModel):
    """Patch 请求参数结构体
    """
    def __init__(self):
        self.Op = None
        self.Path = None
        self.Value = None

    def _deserialize(self, params):
        self.Op = params.get("Op")
        self.Path = params.get("Path")
        self.Value = params.get("Value")



class ProjectResponse(AbstractModel):
    """模型公共响应体"""

    def __init__(self):
        self.RequestId = None
        self.Project = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        self.Project = params.get("Project")

