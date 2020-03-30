# !/usr/bin/env python
# coding:utf-8
# 研究机构接口参数数据获取接口

from data_api.v20191119.dataapi_client import DataapiClient


class ResOrgRef(object):

    def __init__(self, secret_id, secret_key):
        self.secret_id = secret_id
        self.secret_key = secret_key

    def get_data(self, **params):
        dataapi_client = DataapiClient(self.secret_id, self.secret_key)

        result = dataapi_client.get_data("res-org-ref", **params)

        return result
