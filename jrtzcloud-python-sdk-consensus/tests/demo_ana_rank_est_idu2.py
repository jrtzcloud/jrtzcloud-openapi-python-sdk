# !/usr/bin/env python
# coding:utf-8
# 天眼分析师预测排名数据接口调用示例

from jrtzcloudsdkcore.exception.jrtzcloud_sdk_exception import JrtzCloudSDKException
from jrtzcloudsdkconsensus.v20200330.ana_rank_est_idu import AnaRankEstIdu

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
    except JrtzCloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_ana_rank_est_idu("nT3GoChoSilVSWskjjCxEKA1G8R6otAO", "ZWqy9tQXHVzwOvBULX5GS0QWjv7E8Bz8")
