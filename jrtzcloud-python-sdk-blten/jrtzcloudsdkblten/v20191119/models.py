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

class DescribeProjectRequest(AbstractModel):
    """DescribeProject 请求参数结构体
    """
    def __init__(self):
        self.ProjectId = None

    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")

class CreateProjectRequest(AbstractModel):
    """CreateProject 请求参数结构体
    """
    def __init__(self):
        self.StartDate = None
        self.StopDate = None
        self.Model = None

    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.StopDate = params.get("StopDate")
        if params.get("Model") is not None:
            self.Model = Model()
            self.Model._deserialize(params.get("Model"))

class ReplaceProjectRequest(AbstractModel):
    """ReplaceProject 请求参数结构体
    """
    def __init__(self):
        self.ProjectId = None
        self.StartDate = None
        self.StopDate = None
        self.Model = None

    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.StartDate = params.get("StartDate")
        self.StopDate = params.get("StopDate")
        if params.get("Model") is not None:
            self.Model = Model()
            self.Model._deserialize(params.get("Model"))

class PatchProjectRequest(AbstractModel):
    """PatchProject 请求参数结构体
    """
    def __init__(self):
        self.ProjectId = None
        self.Patch = None

    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
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
        self.Op = "replace"
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
        if params.get("Project") is not None:
            self.Project = Project()
            self.Project._deserialize(params.get("Project"))


class Project(AbstractModel):
    """模型项目响应体"""

    def __init__(self):
        self.Model = None
        self.ProjectId = None
        self.StartDate = None
        self.StopDate = None
        self.TasksLength = None
        self.PredictTime = None

    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = Model()
            self.Model._deserialize(params.get("Model"))
        self.ProjectId = params.get("ProjectId")
        self.StartDate = params.get("StartDate")
        self.StopDate = params.get("StopDate")
        self.TasksLength = params.get("TasksLength")
        self.PredictTime = params.get("PredictTime")

class Model(AbstractModel):
    """模型响应体"""

    def __init__(self):
        self.AssetList = None
        self.ConstrainList = None
        self.BoundaryDict = None
        self.OriginalExpRtnDict = None

    def _deserialize(self, params):
        self.AssetList = params.get("AssetList")
        self.ConstrainList = params.get("ConstrainList")
        if params.get("BoundaryDict") is not None:
            self.BoundaryDict = BoundaryDict()
            self.BoundaryDict._deserialize(params.get("BoundaryDict"))
        if params.get("OriginalExpRtnDict") is not None:
            self.OriginalExpRtnDict = OriginalExpRtnDict()
            self.OriginalExpRtnDict._deserialize(params.get("OriginalExpRtnDict"))


class OriginalExpRtnDict(AbstractModel):
    """资产预期收益率字典"""

    def __init__(self):
        self.ABS_RETURN = None
        self.ASHARE = None
        self.CASH = None
        self.CN_CREDIT = None
        self.GLOBAL_DEBT = None
        self.GOLD = None
        self.HKSHARE = None
        self.OIL = None
        self.TREASURY = None
        self.USSHARE = None

    def _deserialize(self, params):
        self.ABS_RETURN = params.get("ABS_RETURN")
        self.ASHARE = params.get("ASHARE")
        self.CASH = params.get("CASH")
        self.CN_CREDIT = params.get("CN_CREDIT")
        self.GLOBAL_DEBT = params.get("GLOBAL_DEBT")
        self.GOLD = params.get("GOLD")
        self.HKSHARE = params.get("HKSHARE")
        self.OIL = params.get("OIL")
        self.TREASURY = params.get("TREASURY")
        self.USSHARE = params.get("USSHARE")

class BoundaryDict(AbstractModel):
    """资产持仓权重绝对值上下限字典"""

    def __init__(self):
        self.ABS_RETURN = None
        self.ASHARE = None
        self.CASH = None
        self.CN_CREDIT = None
        self.GLOBAL_DEBT = None
        self.GOLD = None
        self.HKSHARE = None
        self.OIL = None
        self.TREASURY = None
        self.USSHARE = None

    def _deserialize(self, params):
        self.ABS_RETURN = params.get("ABS_RETURN")
        self.ASHARE = params.get("ASHARE")
        self.CASH = params.get("CASH")
        self.CN_CREDIT = params.get("CN_CREDIT")
        self.GLOBAL_DEBT = params.get("GLOBAL_DEBT")
        self.GOLD = params.get("GOLD")
        self.HKSHARE = params.get("HKSHARE")
        self.OIL = params.get("OIL")
        self.TREASURY = params.get("TREASURY")
        self.USSHARE = params.get("USSHARE")

