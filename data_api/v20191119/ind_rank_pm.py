# !/usr/bin/env python
# coding:utf-8
# 价格动能模型数据获取接口

from data_api.v20191119.data_api_client import DataApiClient


class IndRankPm(object):

    def __init__(self, secret_id, secret_key):
        self.secret_id = secret_id
        self.secret_key = secret_key

    def get_data(self, **params):
        data_api_client = DataApiClient(self.secret_id, self.secret_key)

        result = data_api_client.get_data("ind_rank_pm", **params)

        return result
