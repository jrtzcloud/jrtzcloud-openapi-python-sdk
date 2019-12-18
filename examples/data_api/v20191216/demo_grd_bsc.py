# !/usr/bin/env python
# coding:utf-8
# 投资评级数据接口调用示例

from data_api.v20191119.grd_bsc import GrdBsc
from common.exception.jrtzcloud_sdk_exception import CloudSDKException


def get_grd_bsc(secret_id, secret_key):
    try:
        grd_bsc = GrdBsc(secret_id, secret_key)
        request_parameter = {
            'BeginDate': '20190429',
            'EndDate': '20190529',
            'SecCd': '000300',
            'OperType': '1',
            'Page': '1',
            'PageCount': '10'
        }
        result = grd_bsc.get_data(**request_parameter)
        result.print_result()
    except CloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_grd_bsc("D8xc9JKzEmEvry8XRhkP8JPm5b530pdW", "w70qzZjKn7kl72FJ7BQ8oHoFFzZ0cUmj")
