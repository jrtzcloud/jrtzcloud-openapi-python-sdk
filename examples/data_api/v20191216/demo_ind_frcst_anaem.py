# !/usr/bin/env python
# coding:utf-8
# 分析师动能数据接口调用示例

from data_api.v20191119.ind_frcst_anaem import IndFrcstAnaem
from common.exception.jrtzcloud_sdk_exception import JrtzCloudSDKException


def get_ind_frcst_anaem(secret_id, secret_key):
    try:
        ind_frcst_anaem = IndFrcstAnaem(secret_id, secret_key)
        request_parameter = {
            'BeginDate': '20190429',
            'EndDate': '20190528',
            'SecCd': '000300',
            'OperType': '1',
            'Page': '1',
            'PageCount': '10'
        }
        result = ind_frcst_anaem.get_data(**request_parameter)
        result.print_result()
    except JrtzCloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_ind_frcst_anaem("nT3GoChoSilVSWskjjCxEKA1G8R6otAO", "ZWqy9tQXHVzwOvBULX5GS0QWjv7E8Bz8")
