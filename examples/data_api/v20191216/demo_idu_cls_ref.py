# !/usr/bin/env python
# coding:utf-8
# 行业分类参数数据接口调用示例

from data_api.v20191119.idu_cls_ref import IduClsRef
from common.exception.jrtzcloud_sdk_exception import JrtzCloudSDKException


def get_idu_cls_ref(secret_id, secret_key):
    try:
        idu_cls_ref = IduClsRef(secret_id, secret_key)
        request_parameter = {
            'QueryType': '1',
            'IduCl': 'INDUS2_CL'
        }
        result = idu_cls_ref.get_data(**request_parameter)
        result.print_result()
    except JrtzCloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_idu_cls_ref("nT3GoChoSilVSWskjjCxEKA1G8R6otAO", "ZWqy9tQXHVzwOvBULX5GS0QWjv7E8Bz8")
