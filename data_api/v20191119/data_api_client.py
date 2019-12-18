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
from common.abstract_client import AbstractClient
from common.profile.http_profile import HttpProfile
from common.profile.client_profile import ClientProfile
from common import credential
from common.exception.jrtzcloud_sdk_exception import CloudSDKException
from common.abstract_model import AbstractModel
from data_api.v20191119.models import DataApiResponse


class DataApiClient(AbstractClient):
    _apiVersion = "2019-11-19"
    _endpoint = "dataapi.jrtzcloud.cn"
    _svc_path = "dataapi/consensus"
    _resource_list = ['grd_bsc',
                      'est_bsc',
                      'ind_frcst_hist',
                      'ind_rank_rv_idu',
                      'ind_rank_pm',
                      'ind_rank_eq_idu',
                      'ana_rank_grd',
                      'ana_rank_est_idu',
                      'res_org_rank',
                      'ind_frcst_iduem',
                      'ind_frcst_anaem',
                      'ind_frcst_tianyan',
                      'idu_cls_ref',
                      'res_org_ref']

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
            raise CloudSDKException(message="!!! Resource name:%s error! not support !!!" % resource_name)

    def get_data(self, resource_name, request=None, **params):
        try:
            req = request or AbstractModel()
            req._deserialize(params)
            api_name = self.check_resource(resource_name)
            body = self.call(api_name, req._serialize())
            response = json.loads(body)
            if response.get("Message"):
                raise CloudSDKException(code=response.get("Code"),
                                        message=response.get("Message"),
                                        requestId=response.get("RequestId")
                                        )
            model = DataApiResponse()
            model._deserialize(response)
            return model

        except Exception as e:
            if isinstance(e, CloudSDKException):
                raise e
            else:
                raise CloudSDKException(message=e)