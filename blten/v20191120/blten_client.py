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


class BltenClient(AbstractClient):
    _apiVersion = '2019-11-19'
    _endpoint = 'blten.jrtzcloud.cn'
    _svc_path = 'blten'

    def __init__(self,secret_id,secret_key,region=None, profile=None):
        # 实例化一个认证对象，入参需要传入Investoday云账户secretId，secretKey
        cred = credential.Credential(secret_id,secret_key)
        AbstractClient.__init__(self,cred,region,profile)

    def check_source(self,resource_name):
        if resource_name in ['get_project_info', 'stop_project', \
                             'get_result', 'set_project', 'get_daily']:
            return '/'.join(['',self._svc_path,resource_name])
        else:
            raise CloudSDKException(message="!!! Resource name:%s error! not support !!!" % resource_name)

    def get_data(self,resource_name,request=None,**params):
        """

        """
        try:
            req = request or AbstractModel()
            req._deserialize(params)
            api_name = self.check_source(resource_name)
            body = self.call(api_name, req._serialize())
            response = json.loads(body)
            if response.get("message"):  #router error
                raise CloudSDKException(message=response.get("message"))
            status = response.get("Status")
            if status in ['ok']:
                model = models.DescribeInstancesResponse()
                model._deserialize(response)
                return model
            elif status in ['error']:
                code = response.get("MessagesId")
                message = response.get("Messages")
                reqid = response.get("RequestId")
                raise CloudSDKException(code, message, reqid)
            raise CloudSDKException(message=response)
        except Exception as e:
            if isinstance(e, CloudSDKException):
                raise e
            else:
                raise CloudSDKException(message=e)
