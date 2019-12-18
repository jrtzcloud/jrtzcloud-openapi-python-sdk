# !/usr/bin/env python
# coding:utf-8
# 天眼分析师预测排名数据接口调用示例

from data_api.v20191119.ana_rank_est_idu import AnaRankEstIdu
from common.exception.jrtzcloud_sdk_exception import CloudSDKException


def get_ana_rank_est_idu(secret_id, secret_key):
    try:
        ana_rank_est_idu = AnaRankEstIdu(secret_id, secret_key)
        request_parameter = {
            'BeginDate': '20140429',
            'EndDate': '20190528',
            'IduId': 'A',
            'IduCl': 'INDUS2_CL',
            'Page': '1',
            'PageCount': '10'
        }
        result = ana_rank_est_idu.get_data(**request_parameter)
        result.print_result()
    except CloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_ana_rank_est_idu("D8xc9JKzEmEvry8XRhkP8JPm5b530pdW", "w70qzZjKn7kl72FJ7BQ8oHoFFzZ0cUmj")