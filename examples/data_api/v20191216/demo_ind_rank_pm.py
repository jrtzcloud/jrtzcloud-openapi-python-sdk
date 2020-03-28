# !/usr/bin/env python
# coding:utf-8
# 价格动能模型数据接口调用示例

from data_api.v20191119.ind_rank_pm import IndRankPm
from common.exception.jrtzcloud_sdk_exception import CloudSDKException


def get_ind_rank_pm(secret_id, secret_key):
    try:
        ind_rank_pm = IndRankPm(secret_id, secret_key)
        request_parameter = {
            'BeginDate': '20190429',
            'EndDate': '20190528',
            'SecCd': '000300',
            'OperType': '1',
            'Page': '1',
            'PageCount': '10'
        }
        result = ind_rank_pm.get_data(**request_parameter)
        result.print_result()
    except CloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_ind_rank_pm("nT3GoChoSilVSWskjjCxEKA1G8R6otAO", "ZWqy9tQXHVzwOvBULX5GS0QWjv7E8Bz8")
