# -*- coding: utf-8 -*-
import os

from jrtzcloudsdkcore.exception.jrtzcloud_sdk_exception import JrtzCloudSDKException
# 导入对应产品模块的client models。
from jrtzcloudsdkblten.v20191119 import blten_client, models

# 导入可选配置类
from jrtzcloudsdkcore.profile.client_profile import ClientProfile
from jrtzcloudsdkcore.profile.http_profile import HttpProfile
try:
    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    # httpProfile = HttpProfile()
    # httpProfile.reqTimeout = 30    # 请求超时时间，单位为秒(默认60秒)
    # httpProfile.endpoint = "blten.jrtzcloud.cn"  # 指定接入地域域名(默认就近接入)

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    # clientProfile = ClientProfile(httpProfile)

    # 实例化要请求产品的client对象，clientProfile是可选的。
    client = blten_client.BltenClient(
        os.environ.get("JRTZCLOUD_BLTEN_SECRET_ID"),
        os.environ.get("JRTZCLOUD_BLTEN_SECRET_KEY"))

    # 实例化一个实例信息查询请求对象,每个接口都会对应一个request对象。
    req = models.PatchProjectRequest()

    # 填充请求参数,这里request对象的成员变量即对应接口的入参。
    # 你可以通过官网接口文档或跳转到request对象的定义处查看请求参数的定义。
    req.ProjectId = "47244b5c-8850-11ea-a178-6ab4c551ca93"
    req.Patch = []
    patch = models.Patch()
    patch.Op = "replace"
    patch.Path = "/StartDate"
    patch.Value = "2020-03-08"
    patch2 = models.Patch()
    patch2.Op = "replace"
    patch2.Path = "/StopDate"
    patch2.Value = "2029-09-03"
    req.Patch.append(patch)
    req.Patch.append(patch2)

    # 这里还支持以标准json格式的string来赋值请求参数的方式。下面的代码跟上面的参数赋值是等效的。
    params = '''{
        "Patch": [
            {"Op": "replace", "Path": "/StartDate", "Value": "2020-03-09"},
            {"Op": "replace", "Path": "/StopDate", "Value": "2029-09-01"}
        ]
    }
    '''
    # req.from_json_string(params)

    # 通过client对象调用方法发起请求。注意请求方法名与请求对象是对应的。
    # 返回的resp是一个Response类的实例，与请求对象对应。
    resp = client.PatchProject(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string(indent=2))

    # 也可以取出单个值。
    # 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义。
    print(resp.Project.Model.BoundaryDict.ASHARE)

except JrtzCloudSDKException as err:
    print(err)