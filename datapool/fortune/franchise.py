# -*- coding: utf-8 -*-


import pandas
import requests
from fake_headers import Headers
from params import *

"""
http://txjy.syggs.mofcom.gov.cn/
http://txjy.syggs.mofcom.gov.cn/index.do
https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/franchise/franchise_china.csv
"""

header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)
headers = header.generate()


def get_franchise_china() -> pandas.DataFrame:
    """
    中国-商业特许经营信息管理
    中国-商业特许经营的所有企业
    http://txjy.syggs.mofcom.gov.cn/
    :return:
    """
    outer_data = pandas.read_csv(
        interface_dict["get_franchise_china_file"], encoding="gbk", index_col=0
    )
    try:
        for page in range(1, 5):
            payload = {
                "method": "entps",
                "province": "",
                "city": "",
                "cpf.cpage": str(page),
                "cpf.pagesize": "100",
            }
            r = requests.get(
                interface_dict["get_franchise_china"], params=payload, headers=headers
            )
            temp_data = pandas.read_html(r.text)[1]
            inner_data = temp_data.iloc[:, 0].str.split("  ", expand=True)
            inner_data.columns = ["特许人名称", "备案时间", "地址"]
            outer_data = outer_data.append(inner_data, ignore_index=True)
    except:
        pass
    outer_data.drop_duplicates(inplace=True)
    return outer_data
