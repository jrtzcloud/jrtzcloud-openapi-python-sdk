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
from jrtzcloudsdkconsensus.v20191119 import models

class ConsensusClient(AbstractClient):
    _apiVersion = "2019-11-19"
    _endpoint = "dataapi.investoday.net"

    def DescribeEstBsc(self, request):
        """本接口（DescribeEstBsc）用于查询盈利预测数据列表。
        :param request: Request instance for DescribeEstBsc.
        :type request: :class:`jrtzcloudsdkconsensus.v20191119.models.DescribeEstBscRequest`
        """
        return self._request("DescribeEstBsc", "/consensus/est-bsc", request)

    def DescribeGrdBsc(self, request):
        """本接口（DescribeGrdBsc）用于查询投资评级数据列表。
        :param request: Request instance for DescribeGrdBsc.
        :type request: :class:`jrtzcloudsdkconsensus.v20191119.models.DescribeGrdBscRequest`
        """
        return self._request("DescribeGrdBsc", "/consensus/grd-bsc", request)

    def DescribeIndFrcstHist(self, request):
        """本接口（DescribeIndFrcstHist）用于查询一致预期历史数据列表。
        :param request: Request instance for DescribeIndFrcstHist.
        :type request: :class:`jrtzcloudsdkconsensus.v20191119.models.DescribeIndFrcstHistRequest`
        """
        return self._request("DescribeIndFrcstHist", "/consensus/ind-frcst-hist", request)

    def DescribeIduClsRef(self, request):
        """本接口（DescribeIduClsRef）用于查询行业分类参数列表数据接口。
        :param request: Request instance for DescribeIduClsRef.
        :type request: :class:`jrtzcloudsdkconsensus.v20191119.models.DescribeIduClsRefRequest`
        """
        return self._request("DescribeIduClsRef", "/consensus/idu-cls-ref", request)

    def DescribeResOrgRef(self, request):
        """本接口（DescribeResOrgRef）用于查询研究机构参数列表数据接口。
        :param request: Request instance for DescribeResOrgRef.
        :type request: :class:`jrtzcloudsdkconsensus.v20191119.models.DescribeResOrgRefRequest`
        """
        return self._request("DescribeResOrgRef", "/consensus/res-org-ref", request)

    def DescribeAnaRankEstIdu(self, request):
        """本接口（DescribeAnaRankEstIdu）用于查询天眼分析师预测排名（按行业）数据列表接口。
        :param request: Request instance for DescribeAnaRankEstIdu.
        :type request: :class:`jrtzcloudsdkconsensus.v20191119.models.DescribeAnaRankEstIduRequest`
        """
        return self._request("DescribeAnaRankEstIdu", "/consensus/ana-rank-est-idu", request)
































    def _request(self, action, path, request):
        """公共请求方法
        :param action: Request action name.
        :param path: Request path.
        :param request: Request instance.
        :rtype: :class:`jrtzcloudsdkconsensus.v20191119.models.DescribeConsensusResponse`
        """
        try:
            params = request._serialize()
            body = self.call(action, path, params)
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
                raise JrtzCloudSDKException("JrtzCloudSDKClientError", e.message)
