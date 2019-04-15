#!/usr/bin/python

import requests     # 导入请求模块

url = 'https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&_v=0.16850602&x-zp-page-request-id=12be28ab1b54439e858c1f3c4cb2a001-1555335588614-536724'

def getJobList():
    res = requests.get(
        # 请求url
        url = url
    )
    result = res.json()     # 获取res中的json信息
    print(result)

getJobList()