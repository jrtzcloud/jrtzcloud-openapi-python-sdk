# !/usr/bin/env python
# coding:utf-8
# 相对估值模型数据接口调用示例

from data_api.v20191119.ind_rank_rv_idu import IndRankRvIdu
from common.exception.jrtzcloud_sdk_exception import CloudSDKException


def get_ind_rank_rv_idu(secret_id, secret_key):
    try:
        ind_rank_rv_idu = IndRankRvIdu(secret_id, secret_key)
        request_parameter = {
            'BeginDate': '20190429',
            'EndDate': '20190528',
            'SecCd': '000300',
            'OperType': '1',
            'Page': '1',
            'PageCount': '10'
        }
        result = ind_rank_rv_idu.get_data(**request_parameter)
        result.print_result()
    except CloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_ind_rank_rv_idu("nT3GoChoSilVSWskjjCxEKA1G8R6otAO", "ZWqy9tQXHVzwOvBULX5GS0QWjv7E8Bz8")
