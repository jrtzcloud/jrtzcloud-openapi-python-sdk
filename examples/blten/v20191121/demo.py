# -*- coding: utf-8 -*-

from common.exception.jrtzcloud_sdk_exception import JrtzCloudSDKException
# 导入对应产品模块的client models。
from blten.v20191120.blten_client import BltenClient
import json

# 导入可选配置类
from common.profile.client_profile import ClientProfile
from common.profile.http_profile import HttpProfile


def testdata():
    return dict(
        AssetList=["ASHARE", "USSHARE", "HKSHARE", "ABS_RETURN", "OIL",
                   "GOLD", "TREASURY", "CN_CREDIT", "GLOBAL_DEBT", "CASH"],
        OriginalExpRtnDict={
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


def daily_data(client):
    ret = client.req_call('daily-data/2020-02-04')
    print(ret)


def model_data(client):
    guid = '4987324e-577a-11ea-a43a-c60aaec77637'
    start_date = '2016-01-01'
    end_date = '2016-06-30'
    ret = client.req_call('model-data/projects/%s' % guid, StartDate=start_date, EndDate=end_date, RiskN=1)
    print(ret)

def project(client):
    ret = client.req_call('projects/f863b416-06be-11ea-b4e9-000c2947adc4')
    print(ret)

def project_patch(client):
    data = testdata()
    start = '2019-10-01'
    stop = '2019-11-11'

    patch = [
        {'op': 'replace', 'path': '/Model', 'value': data},
        {'op': 'replace', 'path': '/StartDate', 'value': "2019-09-01"},
        {'op': 'replace', 'path': '/StopDate', 'value': "2029-09-01"},
    ]
    ret = client.req_call('projects/1b269b24-feb0-11e9-a52f-000c2947adc4', method='PATCH', Patch=patch)
    print(ret)


def project_post(client):
    data = testdata()
    # guid = '1b269b24-feb0-11e9-a52f-000c2947adc4'
    start = '2016-01-01'
    stop = '2119-11-11'

    param = dict(Model=data,
                StartDate=start,
                StopDate=stop
                )
    # print(param)
    ret = client.req_call('projects', method='POST', **param)
    print(ret)

def project_put(client):
    data = testdata()
    guid = '1cfe0776-06bb-11ea-9e13-000c2947adc4'
    start = '2016-01-01'
    stop = '2219-11-12'

    param = dict(Model=data,
                StartDate=start,
                StopDate=stop)

    ret = client.req_call('projects/1cfe0776-06bb-11ea-9e13-000c2947adc4',method='PUT', **param)
    print(ret)

if __name__ == '__main__':
    # 密钥参数
    secret_id = "QlaLiAmJq8iQkKEEaBxLSCwqyuQJKfKP"#"D8xc9JKzEmEvry8XRhkP8JPm5b530pdW"
    secret_key = "0bVX3wlJQRj3VQr92I0T0pIgXxsF19Le"#"w70qzZjKn7kl72FJ7BQ8oHoFFzZ0cUmj"
    profile = HttpProfile(
        endpoint='blten.jrtzcloud.cn',
        svc_path='blten',
        apiVersion='2019-11-19',
        region='ap-shenzhen'
    )
    # client = BltenClient(secret_id, secret_key)
    # project_post(client)  # ok ok
    # project_put(client)  # ok
    # project(client)
    # daily_data(client)
    # model_data(client)
    # project_patch(client)
    # model_data(client)  # ok
    try:
        client = BltenClient(secret_id, secret_key, profile=profile)
        # daily_data(client)  #ok  ok
        model_data(client)  #ok
        # project_put(client)  #ok
        # project_post(client)  #ok ok
        # project(client)    #ok  ok
        # project_patch(client)  #ok--
        #         # ret = client.req_call('daily-data/2020-02-03')
        #         # print(ret)
        #         #
        #         # guid = 'f863b416-06be-11ea-b4e9-000c2947adc4'
        #         # start_date = '2020-01-04'
        #         # end_date = '2020-02-04'
        #         # ret = client.req_call('projects/%s/model-data' % guid, StartDate=start_date, EndDate=end_date)
        #         # print(ret)
        #         # # #
        #         # guid = 'f863b416-06be-11ea-b4e9-000c2947adc4'
        #         # stop = '2019-12-23'
        #         #
        #         # ret = client.get_data('projects', method='PATCH', param=param)
        #         # print(ret)
        #         # #
        #         # guid = 'f863b416-06be-11ea-b4e9-000c2947adc4'
        #         # ret = client.get_data('get_project_info',guid=guid)
        #         # print(ret)
        #         #
        #         # data = testdata()
        #         # # # guid = '1b269b24-feb0-11e9-a52f-000c2947adc4'
        # start = '2019-10-01'
        # stop = '2019-11-11'
        # data = dict(ProjectParam=data,
        #             StartDate=start,
        #             StopDate=stop)
        #
        # param = json.dumps(data)
        # ret = client.put('projects/1b269b24-feb0-11e9-a52f-000c2947adc4', param=param)

        # # param = param if guid is None else None
        # ret = client.get_data('set_project',guid=guid,param=param,start=start,stop=stop)
        # print(ret)
    except JrtzCloudSDKException as err:
        print(err)
