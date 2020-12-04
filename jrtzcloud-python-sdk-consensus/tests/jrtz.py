import pandas as pd
import json
import os
import datetime

from jrtzcloudsdkcore.exception.jrtzcloud_sdk_exception import JrtzCloudSDKException
from jrtzcloudsdkconsensus.v20191119 import consensus_client, models

USER = os.environ.get("JRTZCLOUD_LYZT_DEV_SECRET_ID")
PWD = os.environ.get("JRTZCLOUD_LYZT_DEV_SECRET_KEY")

try:
    client = consensus_client.ConsensusClient(USER, PWD)
except JrtzCloudSDKException as err:
    print(err)


def change(da):
    da[0] = datetime.datetime.strptime(da[0], '%Y-%m-%d %H:%M:%S.0')
    return da

def fetch_jrtz_Anaem(client, models, start_date, end_date):
    '''
    req  : return from connect_jrtz()
    date : int 20190531
    index:
    '''

    ### 000001  399106, ###

    value = []
    req = models.DescribeIndFrcstAnaemRequest()

    params = '''{
		"BeginDate" : %s,
		"EndDate"	: %s,
		"SecCd"		: "000001",
		"OperType"	: "1",
		"RptRang"	: "1",
		"PageNo" 	: %s,
		"PageSize"  : "1000"
	 }'''

    HasNextPage = 1
    page = 1
    while HasNextPage:
        req.from_json_string(params % (start_date, end_date, page))
        resp = client.DescribeIndFrcstAnaem(req)
        # resp = client.DescribeEstBsc(req)
        resp_s = json.loads(resp.to_json_string())
        print(resp_s['PageNo'])
        value.append(resp_s['Fields'])
        value.extend([change(e) for e in resp_s['Data']])
        page += 1
        HasNextPage = resp_s['HasNextPage']

    #   "RptYr"     : "2019",
    params = '''{
		"BeginDate" : %s,
		"EndDate"	: %s,
		"SecCd"		: "399106",
		"OperType"	: "1",
		"RptRang"	: "1", 
		"PageNo"    : %s,
		"PageSize"  : "1000"
	 }'''
    HasNextPage = 1
    page = 1
    while HasNextPage:
        req.from_json_string(params % (start_date, end_date, page))
        resp = client.DescribeIndFrcstAnaem(req)
        # resp = client.DescribeEstBsc(req)
        resp_s = json.loads(resp.to_json_string())
        print(resp_s['PageNo'])
        # value.append(resp_s['Fields'])
        value.extend([change(e) for e in resp_s['Data']])
        page += 1
        HasNextPage = resp_s['HasNextPage']
    return value


def dump_jrtz(client, models, date):
    '''
    date:  20190531
    '''

    data = fetch_jrtz_Anaem(client, models, date, date)

    data = pd.DataFrame(data[1:], columns=data[0])
    print('总数据长度=> ' + str(len(data)))
    year = int(str(date)[:4])
    data = data[data['RptYr'] == year]
    print(str(year) + '数据长度=> ' + str(len(data)))
    # data.to_csv('{0}_{1}.csv'.format('jrtz', date), encoding='utf_8_sig', index=False)

    return 0


dump_jrtz(client, models, 20201123)

# import pdb;pdb.set_trace()