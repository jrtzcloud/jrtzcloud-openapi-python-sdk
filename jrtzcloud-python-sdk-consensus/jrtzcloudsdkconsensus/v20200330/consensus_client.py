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

import json
from jrtzcloudsdkcore.exception.jrtzcloud_sdk_exception import JrtzCloudSDKException
from jrtzcloudsdkcore.abstract_client import AbstractClient
from jrtzcloudsdkconsensus.v20200330 import models

class ConsensusClient(AbstractClient):
    _apiVersion = "2019-11-19"
    _endpoint = "dataapi.investoday.net"
    _svc_path = "consensus"

    def DescribeEstBsc(self, request):
        """本接口（DescribeEstBsc）用于查询盈利预测数据列表。
        :param request: Request instance for DescribeEstBsc.
        :type request: :class:`jrtzcloudsdkconsensus.v20200330.models.DescribeEstBscRequest`
        :rtype: :class:`jrtzcloudsdkconsensus.v20200330.models.DescribeConsensusResponse`
        """
        try:
            params = request._serialize()
            body = self.call("DescribeEstBsc", params)
            response = json.loads(body)
            if response.get("Message"):
                raise JrtzCloudSDKException(response.get("Code"),
                                            response.get("Message"),
                                            response.get("RequestId"))
                raise JrtzCloudSDKException(code, message, reqid)
            else:
                model = models.DescribeConsensusResponse()
                model._deserialize(response)
                return model
        except Exception as e:
            if isinstance(e, JrtzCloudSDKException):
                raise
            else:
                raise JrtzCloudSDKException(e.message, e.message)
