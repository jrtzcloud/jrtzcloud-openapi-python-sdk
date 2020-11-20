import pandas as pd
import json
import os

from jrtzcloudsdkcore.exception.jrtzcloud_sdk_exception import JrtzCloudSDKException
from jrtzcloudsdkconsensus.v20191119 import consensus_client, models

USER = os.environ.get("JRTZCLOUD_LYZT_DEV_SECRET_ID")
PWD = os.environ.get("JRTZCLOUD_LYZT_DEV_SECRET_KEY")

try:
    client = consensus_client.ConsensusClient(USER, PWD)
except JrtzCloudSDKException as err:
    print(err)


def fetch_jrtz_Anaem(client, models, start_date, end_date):
    '''
    req  : return from connect_jrtz()
    date : int 20190531
    index:
    '''

    ### 000001  399106, ###

    value = []
    req = models.DescribeIndFrcstAnaemRequest()

    # params = '''{
	# 	"BeginDate" : %s,
	# 	"EndDate"	: %s,
	# 	"SecCd"		: "000001",
	# 	"OperType"	: "1",
	# 	"RptRang"	: "1",
	# 	"PageNo" 		: %s,
	# 	"PageSize" : "1000"
	#  }'''
    #
    # HasNextPage = 1
    # page = 1
    # while HasNextPage:
    #     req.from_json_string(params % (start_date, end_date, page))
    #     resp = client.DescribeIndFrcstAnaem(req)
    #     # resp = client.DescribeEstBsc(req)
    #     resp_s = json.loads(resp.to_json_string())
    #     print(resp_s['Page'])
    #     value.extend(resp_s['Data'])
    #     page += 1
    #     HasNextPage = resp_s['HasNextPage']

    # 		"RptYr"     : "2019",
    params = '''{
		"BeginDate" : %s,
		"EndDate"	: %s,
		"SecCd"		: "399106",
		"OperType"	: "1",
		"RptRang"	: "1", 
		"PageNo" 		: %s,
		"PageSize" : "1000"
	 }'''
    HasNextPage = 1
    page = 1
    while HasNextPage:
        req.from_json_string(params % (start_date, end_date, page))
        resp = client.DescribeIndFrcstAnaem(req)
        # resp = client.DescribeEstBsc(req)
        resp_s = json.loads(resp.to_json_string())
        print(resp_s['Page'])
        value.extend(resp_s['Data'])
        page += 1
        HasNextPage = resp_s['HasNextPage']
    return value


def dump_jrtz(client, models, date):
    '''
    date:  20190531
    '''

    data = fetch_jrtz_Anaem(client, models, date, date)

    data = pd.DataFrame(data)
    print('总数据长度=> ' + str(len(data)))
    data = data[data['RptYr'] == int(str(date)[:4])]
    print('2019数据长度=> ' + str(len(data)))
    data.to_csv('{0}_{1}.csv'.format('jrtz', date), encoding='utf_8_sig')

    return 0


dump_jrtz(client, models, 20190531)

# import pdb;pdb.set_trace()