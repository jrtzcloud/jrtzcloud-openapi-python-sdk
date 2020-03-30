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


class DataApiResponse(AbstractModel):
    """DataApi公共响应体"""

    def __init__(self):
        self.TotalCount = None
        self.Data = None
        self.Page = None
        self.PageSize = None
        self.Pages = None
        self.RequestId = None
        self.NextPage = None
        self.LastPage = None
        self.HasNextPage = None

    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Data = params.get("Data")
        self.Page = params.get("Page")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.RequestId = params.get("RequestId")
        self.NextPage = params.get("NextPage")
        self.LastPage = params.get("LastPage")
        self.HasNextPage = params.get("HasNextPage")

    def print_result(self):
        print("RequestId: ", self.RequestId)
        print("Pages: ", self.Pages)
        print("Page: ", self.Page)
        print("PageSize: ", self.PageSize)
        print("Size: ", self.PageSize)
        print("TotalCount: ", self.TotalCount)
        print("Data: ", self.Data)
        print("NextPage: ", self.NextPage)
        print("LastPage: ", self.LastPage)
        print("HasNextPage: ", self.HasNextPage)
