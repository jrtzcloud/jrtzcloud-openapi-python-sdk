# !/usr/bin/env python
# coding:utf-8
# 行业分类参数数据接口调用示例

from data_api.v20191119.idu_cls_ref import IduClsRef
from common.exception.jrtzcloud_sdk_exception import CloudSDKException


def get_idu_cls_ref(secret_id, secret_key):
    try:
        idu_cls_ref = IduClsRef(secret_id, secret_key)
        request_parameter = {
            'QueryType': '1',
            'IduCl': 'INDUS2_CL'
        }
        result = idu_cls_ref.get_data(**request_parameter)
        result.print_result()
    except CloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_idu_cls_ref("D8xc9JKzEmEvry8XRhkP8JPm5b530pdW", "w70qzZjKn7kl72FJ7BQ8oHoFFzZ0cUmj")
