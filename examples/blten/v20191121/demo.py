# -*- coding: utf-8 -*-

from common.exception.jrtzcloud_sdk_exception import CloudSDKException
# 导入对应产品模块的client models。
from blten.v20191120.blten_client import BltenClient

# 导入可选配置类
from common.profile.client_profile import ClientProfile
from common.profile.http_profile import HttpProfile

def testdata():
    return dict(
        AssetList = ["ASHARE", "USSHARE", "HKSHARE", "ABS_RETURN", "OIL",
                      "GOLD", "TREASURY", "CN_CREDIT", "GLOBAL_DEBT", "CASH"],
        Original_ExpRtn_Dict={
                "ASHARE": 0.12,
                "USSHARE": 0.082,
                "HKSHARE": 0.082,
                "ABS_RETURN": 0.045,
                "OIL": 0.085,
                "GOLD": 0.06,
                "CN_CREDIT": 0.045,
                "TREASURY": 0.042,
                "GLOBAL_DEBT": 0.04,
                "CASH": 0.03,
            },
        BoundaryDict={
                "ASHARE": [0, 1.0],
                "USSHARE": [0, 1.0],
                "HKSHARE": [0, 1.0],
                "ABS_RETURN": [0, 0.10],
                "OIL": [0, 1.0],
                "GOLD": [0, 1.0],
                "TREASURY": [0.03, 1.0],
                "CN_CREDIT": [0, 1.0],
                "GLOBAL_DEBT": [0.0, 1.0],
                "CASH": [0.02, 1.0],
            },
        ConstrainList=[
            ["ineq", "(0.3 * ASHARE) - USSHARE"],
        ]

    )


if __name__=='__main__':
    # 密钥参数
    secret_id = "D8xc9JKzEmEvry8XRhkP8JPm5b530pdW"
    secret_key = "w70qzZjKn7kl72FJ7BQ8oHoFFzZ0cUmj"

    try:
        client = BltenClient(secret_id, secret_key)

        ret = client.get_data('get_daily',day='2019-11-11')
        print(ret)
        #
        # guid = 'f863b416-06be-11ea-b4e9-000c2947adc4'
        # start='2011-10-01'
        # end='2020-11-11'
        # ret = client.get_data('get_result',guid=guid,start=start,end=end)
        # print(ret)
        # #
        # guid = 'f863b416-06be-11ea-b4e9-000c2947adc4'
        # stop='2019-12-23'
        # ret = client.get_data('stop_project',guid=guid,stop=stop)
        # print(ret)
        #
        # # guid = 'f863b416-06be-11ea-b4e9-000c2947adc4'
        # ret = client.get_data('get_project_info',guid=guid)
        # print(ret)

        # param = testdata()
        # guid = None#'1b269b24-feb0-11e9-a52f-000c2947adc4'
        # start='2019-10-01'
        # stop='2019-11-11'
        # param = json.dumps(param)
        # # param = param if guid is None else None
        # ret = client.get_data('set_project',guid=guid,param=param,start=start,stop=stop)
        # print(ret)
    except CloudSDKException as err:
        print(err)