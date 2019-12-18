# !/usr/bin/env python
# coding:utf-8
# 研究机构整体实力得分数据接口调用示例

from data_api.v20191119.res_org_rank import ResOrgRank
from common.exception.jrtzcloud_sdk_exception import CloudSDKException


def get_res_org_rank(secret_id, secret_key):
    try:
        res_org_rank = ResOrgRank(secret_id, secret_key)
        request_parameter = {
            'BeginDate': '20140429',
            'EndDate': '20190528',
            'IduId': 'A',
            'IduCl': 'INDUS2_CL',
            'Page': '1',
            'PageCount': '10'
        }
        result = res_org_rank.get_data(**request_parameter)
        result.print_result()
    except CloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_res_org_rank("D8xc9JKzEmEvry8XRhkP8JPm5b530pdW", "w70qzZjKn7kl72FJ7BQ8oHoFFzZ0cUmj")
