# !/usr/bin/env python
# coding:utf-8
# 天眼分析师预测排名数据获取接口

from jrtzcloudsdkconsensus.v20200330.dataapi_client import DataapiClient

class AnaRankEstIdu(object):

    def __init__(self, secret_id, secret_key):
        self.secret_id = secret_id
        self.secret_key = secret_key

    def get_data(self, **params):
        dataapi_client = DataapiClient(self.secret_id, self.secret_key)

        result = dataapi_client.get_data("ana-rank-est-idu", **params)

        return result
