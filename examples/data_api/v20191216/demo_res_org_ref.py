# !/usr/bin/env python
# coding:utf-8
# 研究机构接口参数数据接口调用示例

from data_api.v20191119.res_org_ref import ResOrgRef
from common.exception.jrtzcloud_sdk_exception import CloudSDKException


def get_res_org_ref(secret_id, secret_key):
    try:
        res_org_ref = ResOrgRef(secret_id, secret_key)
        request_parameter = {
            'QueryType': '1'
        }
        result = res_org_ref.get_data(**request_parameter)
        result.print_result()
    except CloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_res_org_ref("D8xc9JKzEmEvry8XRhkP8JPm5b530pdW", "w70qzZjKn7kl72FJ7BQ8oHoFFzZ0cUmj")
