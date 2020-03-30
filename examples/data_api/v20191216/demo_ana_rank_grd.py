# !/usr/bin/env python
# coding:utf-8
# 天眼分析师评级排名数据接口调用示例

from data_api.v20191119.ana_rank_grd import AnaRankGrd
from common.exception.jrtzcloud_sdk_exception import JrtzCloudSDKException


def get_ana_rank_grd(secret_id, secret_key):
    try:
        ana_rank_grd = AnaRankGrd(secret_id, secret_key)
        request_parameter = {
            'BeginDate': '20190429',
            'EndDate': '20190528',
            'IduId': 'A',
            'IduCl': 'INDUS2_CL',
            'Page': '1',
            'PageCount': '10'
        }
        result = ana_rank_grd.get_data(**request_parameter)
        result.print_result()
    except JrtzCloudSDKException as e:
        print(e.get_request_id())
        print(e.get_message())
        print(e.get_code())


if __name__ == '__main__':
    get_ana_rank_grd("nT3GoChoSilVSWskjjCxEKA1G8R6otAO", "ZWqy9tQXHVzwOvBULX5GS0QWjv7E8Bz8")
