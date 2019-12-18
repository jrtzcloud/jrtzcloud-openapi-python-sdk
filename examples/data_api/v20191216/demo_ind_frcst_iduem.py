# !/usr/bin/env python
# coding:utf-8
# 分析师行业动能数据接口调用示例

from data_api.v20191119.ind_frcst_iduem import IndFrcstIduem
from common.exception.jrtzcloud_sdk_exception import CloudSDKException


def get_ind_frcst_iduem(secret_id, secret_key):
    try:
        ind_frcst_iduem = IndFrcstIduem(secret_id, secret_key)
        request_parameter = {
            'BeginDate': '20190429',
            'EndDate': '20190528',
            'IduCl': 'INDUS2_CL',
            'IduId': 'A',
            'Page': '1',
            'PageCount': '10'
        }
        result = ind_frcst_iduem.get_data(**request_parameter)
        result.print_result()
    except CloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_ind_frcst_iduem("D8xc9JKzEmEvry8XRhkP8JPm5b530pdW", "w70qzZjKn7kl72FJ7BQ8oHoFFzZ0cUmj")
