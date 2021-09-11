# -*- coding: utf-8 -*-


import json
import pandas
import requests
from params import *

"""
http://data.eastmoney.com/cjsj/oil_default.html
http://data.eastmoney.com/cjsj/oil_default.html
"""


def get_energy_oil_hist() -> pandas.DataFrame:
    """
    汽柴油历史调价信息
    http://data.eastmoney.com/cjsj/oil_default.html
    :return: 汽柴油历史调价数
    """
    try:
        r = requests.get(
            url=interface_dict["get_energy_oil_hist"],
            params=params_dict["get_energy_oil_hist"], headers=headers
        )
        data_text = r.text
        data_json = json.loads(data_text[data_text.find("{"): -1])
        data = pandas.DataFrame(data_json["result"]["data"])
        data.columns = [
            "日期", "汽油价格", "柴油价格", "汽油涨幅", "柴油涨幅"
        ]
        return data
    except:
        return pandas.DataFrame({})


def get_energy_oil_detail(date="2020-03-19") -> pandas.DataFrame:
    """
    地区油价
    http://data.eastmoney.com/cjsj/oil_default.html
    :param date:
    :return:
    """
    try:
        params_dict["get_energy_oil_detail"]["filter"] = f'(dim_date="{date}")'
        r = requests.get(
            url=interface_dict["get_energy_oil_detail"],
            params=params_dict["get_energy_oil_detail"], headers=headers
        )
        data_text = r.text
        data_json = json.loads(data_text[data_text.find("{"): -1])
        data = pandas.DataFrame(data_json["result"]["data"]).iloc[:, 1:]
        return data
    except:
        return pandas.DataFrame({})
