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

from common.abstract_model import AbstractModel
import json

class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param InstanceSet: 请求返回结果。
        :type InstanceSet: Instance or str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None

    def _deserialize(self, params):
        ret = params.get("Ret")
        if isinstance(ret,str):
            self.InstanceSet = ret
        elif isinstance(ret,dict):
            self.TotalCount = len(ret)
            if ret.get('Cov'):
                ret['Cov'] = json.loads(ret.pop('Cov'))
            self.InstanceSet = ret
        self.RequestId = params.get("RequestId")