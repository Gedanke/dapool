# -*- coding: utf-8 -*-
"""
@file: macro_china.py
@time: 2021/6/22
@desc:
"""

import pandas
import requests
from setting import *
from datapool.economic.china import *


def get_marco_cmlrd():
    """

    年份	居民部门	非金融企业部门	中央政府	地方政府	政府部门	实体经济部门	金融部门资产方	金融部门负债方
    :return:
    """
    data = pandas.read_excel(interface_dict["get_marco_cmlrd"], sheet_name="Data", header=0, skiprows=1)
    data["Period"] = pandas.to_datetime(data["Period"]).dt.strftime("%Y-%m")
    table = list(data.columns)
    data = data[table[:len(marco_cmlrd_table)]]
    data.columns = marco_cmlrd_table
    return data


def get_gdp_quarter():
    """

    :return:
    """
    r = requests.get(interface_dict["get_gdp_quarter"], params=gdp_quarter_params, headers=headers)
    r.encoding = "utf-8"
    content = str(r.text)
    rows = content[content.find("[") + 2:-3]
    rows_list = rows.split('","')
    data_list = [
        row.split(",") for row in rows_list
    ]
    data = pandas.DataFrame(data_list, columns=gdp_quarter_table)
    return data


if __name__ == '__main__':
    """"""
    # print(get_marco_cmlrd())
    print(get_gdp_quarter())
