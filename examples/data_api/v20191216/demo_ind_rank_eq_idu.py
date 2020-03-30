# !/usr/bin/env python
# coding:utf-8
# 公司盈利质量数据接口调用示例

from data_api.v20191119.ind_rank_eq_idu import IndRankEqIdu
from common.exception.jrtzcloud_sdk_exception import JrtzCloudSDKException


def get_ind_eq_idu(secret_id, secret_key):
    try:
        ind_eq_idu = IndRankEqIdu(secret_id, secret_key)
        request_parameter = {
            'BeginDate': '20190429',
            'EndDate': '20190528',
            'SecCd': '000300',
            'OperType': '1',
            'Page': '1',
            'PageCount': '10'
        }
        result = ind_eq_idu.get_data(**request_parameter)
        result.print_result()
    except JrtzCloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_ind_eq_idu("nT3GoChoSilVSWskjjCxEKA1G8R6otAO", "ZWqy9tQXHVzwOvBULX5GS0QWjv7E8Bz8")
