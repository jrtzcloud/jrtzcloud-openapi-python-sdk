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
from jrtzcloudsdkcore.abstract_client import AbstractClient
from jrtzcloudsdkcore.profile.http_profile import HttpProfile
from jrtzcloudsdkcore.profile.client_profile import ClientProfile
from jrtzcloudsdkcore import credential
from jrtzcloudsdkcore.exception.jrtzcloud_sdk_exception import JrtzCloudSDKException
from jrtzcloudsdkcore.abstract_model import AbstractModel
from jrtzcloudsdkconsensus.v20200330.models import DataApiResponse




class DataapiClient(AbstractClient):
    _apiVersion = "2019-11-19"
    _endpoint = "dataapi.investoday.net"
    _svc_path = "consensus"
    _resource_list = ['est-bsc',
                      'grd-bsc',
                      'ind-frcst-hist',
                      'idu-cls-ref',
                      'res-org-ref',
                      'ana-rank-est-idu',
                      'ana-rank-grd',
                      'ind-frcst-anaem',
                      'ind-frcst-iduem',
                      'ind-frcst-tianyan',
                      'ind-rank-eq-idu',
                      'ind-rank-pm',
                      'ind-rank-rv-idu',
                      'res-org-rank']

    def __init__(self, secret_id, secret_key, region=None, profile=None):
        # 实例化一个认证对象，入参需要传入Investoday云账户secretId，secretKey
        cred = credential.Credential(secret_id, secret_key)
        http_profile = HttpProfile()
        http_profile.reqMethod = "GET"  # post请求(默认为post请求)
        client_profile = ClientProfile(httpProfile=http_profile)
        AbstractClient.__init__(self, cred, region, profile or client_profile)

    def check_resource(self, resource_name):
        if resource_name in self._resource_list:
            return '/'.join(['', self._svc_path, resource_name])
        else:
            raise JrtzCloudSDKException(message="!!! Resource name:%s error! not support !!!" % resource_name)

    def get_data(self, resource_name, request=None, **params):
        try:
            req = request or AbstractModel()
            req._deserialize(params)
            api_name = self.check_resource(resource_name)
            body = self.call(api_name, req._serialize())
            response = json.loads(body)
            if response.get("Message"):
                raise JrtzCloudSDKException(code=response.get("Code"),
                                        message=response.get("Message"),
                                        requestId=response.get("RequestId"))
            model = DataApiResponse()
            model._deserialize(response)
            return model

        except Exception as e:
            if isinstance(e, JrtzCloudSDKException):
                raise e
            else:
                raise JrtzCloudSDKException(message=e)
