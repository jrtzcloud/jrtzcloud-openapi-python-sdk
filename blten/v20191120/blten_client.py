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
from common.exception.jrtzcloud_sdk_exception import CloudSDKException
from common.abstract_client import AbstractClient
from common.abstract_model import AbstractModel
from common import credential
from blten.v20191120 import models
from common.profile.http_profile import HttpProfile
from common.profile.client_profile import ClientProfile


class BltenClient(AbstractClient):
    _apiVersion = '2019-11-19'
    _endpoint = 'blten.jrtzcloud.cn'
    # _endpoint = 'bl-ten.jrtzcloud.cn'
    # _endpoint = 'blten-pro.jrtzcloud.cn'
    #
    # _endpoint = 'http://192.168.10.134:9050'
    _svc_path = 'blten'

    def __init__(self, secret_id, secret_key, region=None, profile=None):
        # 实例化一个认证对象，入参需要传入Investoday云账户secretId，secretKey
        cred = credential.Credential(secret_id, secret_key)

        # 实例化一个http选项，可选的，没有特殊需求可以跳过。
        httpProfile = profile or HttpProfile()
        httpProfile.reqMethod = "GET"  # post请求(默认为post请求)
        # httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
        # httpProfile.endpoint = 'blten.jrtzcloud.cn'  # 指定接入地域域名(默认就近接入)
        client_profile = ClientProfile(httpProfile=httpProfile)
        AbstractClient.__init__(self, cred, region, client_profile)

    def check_source(self, resource_name):
        svc_path = self.profile.httpProfile.svc_path or self._svc_path
        resources = resource_name.split('/')
        if resources[0] in ['projects', 'daily-data', 'model-data']:

            return '/'.join(['', svc_path, resource_name])
        else:
            raise CloudSDKException(message="!!! Resource name:%s error! not support !!!" % resource_name)

    def req_call(self, resource_name, request=None, method=None, **params):
        """

        """
        try:
            req = request or AbstractModel()
            req._deserialize(params)
            api_name = self.check_source(resource_name)
            self.profile.httpProfile.reqMethod = method or 'GET'
            # print(req._serialize())
            body = self.call(api_name, req._serialize())
            response = json.loads(body)

            if response is None:
                #service todo
                return
            # print(1111,response)
            # if response.get("message"):  #router error
            #     raise CloudSDKException(message=response.get("message"))

            if response.get('Instances'):

                model = models.DescribeInstancesResponse()
                model._deserialize(response)
                return model
            elif response.get('Project'):
                model = models.DescribeInstancesResponse()
                model._deserialize(response)
                return model
            elif response.get("Message"):
                return response
            raise CloudSDKException(message=response)
        except Exception as e:
            if isinstance(e, CloudSDKException):
                raise e
            else:
                raise CloudSDKException(message=e)
