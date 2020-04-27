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
from jrtzcloudsdkblten.v20191119 import models

class BltenClient(AbstractClient):
    _apiVersion = "2019-11-19"
    _endpoint = "blten.test.investoday.net"

    def CreateProject(self, request):
        """本接口（CreateProject）用于修改用户自定义模型接口
        :param request: Request instance for CreateProject.
        :type request: :class:`jrtzcloudsdkblten.v20191119.models.CreateProjectRequest`
        """
        return self._project_request("CreateProject", "POST", "/blten/projects", request)

    def PatchProject(self, request):
        """本接口（PatchProject）用于修改用户自定义模型接口
        :param request: Request instance for PatchProject.
        :type request: :class:`jrtzcloudsdkblten.v20191119.models.PatchProjectRequest`
        """
        return self._project_request("PatchProject", "PATCH", "/blten/projects/" + request.ProjectId, request)

    def ReplaceProject(self, request):
        """本接口（ReplaceProject）用于替换用户自定义模型接口
        :param request: Request instance for ReplaceProject.
        :type request: :class:`jrtzcloudsdkblten.v20191119.models.ReplaceProjectRequest`
        """
        return self._project_request("ReplaceProject", "PUT", "/blten/projects/" + request.ProjectId, request)

    def DescribeProject(self, request):
        """本接口（DescribeProject）用于替换用户自定义模型接口
        :param request: Request instance for DescribeProject.
        :type request: :class:`jrtzcloudsdkblten.v20191119.models.DescribeProjectRequest`
        """
        return self._project_request("DescribeProject", "GET", "/blten/projects/" + request.ProjectId)

    def DescribeModelData(self, request):
        """本接口（DescribeModelData）用于替换用户自定义模型接口
        :param request: Request instance for DescribeModelData.
        :type request: :class:`jrtzcloudsdkblten.v20191119.models.DescribeModelDataRequest`
        """
        return self._model_data_request("DescribeModelData", "GET", "/blten/model-data/projects/" + request.ProjectId, request)




    def _model_data_request(self, action, method, path, request=None):
        """公共请求方法
        :param action: Request action name.
        :param path: Request path.
        :param request: Request instance.
        :rtype: :class:`jrtzcloudsdkblten.v20191119.models.ProjectResponse`
        """
        try:
            if request != None and hasattr(request, "ProjectId"):
                delattr(request, "ProjectId")
            params = None if request is None else request._serialize()
            body = self.call(action, method, path, params)
            response = json.loads(body)
            if response.get("Message"):
                raise JrtzCloudSDKException(response.get("Code"),
                                            response.get("Message"),
                                            response.get("RequestId"))
                raise JrtzCloudSDKException(code, message, reqid)
            else:
                model = models.DescribeModelDataResponse()
                model._deserialize(response)
                return model
        except Exception as e:
            if isinstance(e, JrtzCloudSDKException):
                raise
            else:
                raise JrtzCloudSDKException("JrtzCloudSDKClientError", e.message)


    def _project_request(self, action, method, path, request=None):
        """公共请求方法
        :param action: Request action name.
        :param path: Request path.
        :param request: Request instance.
        :rtype: :class:`jrtzcloudsdkblten.v20191119.models.ProjectResponse`
        """
        try:
            if request != None and hasattr(request, "ProjectId"):
                delattr(request, "ProjectId")
            params = None if request is None else request._serialize()
            body = self.call(action, method, path, params)
            response = json.loads(body)
            if response.get("Message"):
                raise JrtzCloudSDKException(response.get("Code"),
                                            response.get("Message"),
                                            response.get("RequestId"))
                raise JrtzCloudSDKException(code, message, reqid)
            else:
                model = models.ProjectResponse()
                model._deserialize(response)
                return model
        except Exception as e:
            if isinstance(e, JrtzCloudSDKException):
                raise
            else:
                raise JrtzCloudSDKException("JrtzCloudSDKClientError", e.message)
