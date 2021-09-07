# -*- coding: utf-8 -*-


import time
import pandas
import requests
from params import *
from fake_headers import Headers

"""
https://www.itjuzi.com/deathCompany
"""

header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)
headers = header.generate()


def get_death_company() -> pandas.DataFrame:
    """
    倒闭公司
    https://www.itjuzi.com/deathCompany
    :return:
    data
    """
    try:
        temp_data = pandas.read_csv(interface_dict["get_death_company"], index_col=0)
        r_data = requests.get(url=interface_dict["get_death_company_json"], headers=headers)
        r_data.encoding = "gbk"
        json_data = r_data.json()
        data_ = json_data["data"]["info"]
        data_ = pandas.DataFrame(data_)
        data_ = data_[
            [
                "com_name",
                "born",
                "com_change_close_date",
                "live_time",
                "total_money",
                "cat_name",
                "com_prov",
            ]
        ]
        data = temp_data.append(data_, ignore_index=True)
        data.drop_duplicates(inplace=True)
        return data
    except:
        return pandas.DataFrame({})


def get_nicorn_company(indicator="部分") -> pandas.DataFrame:
    """
    独角兽公司
    https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/data/data_juzi/nicorn_company.csv
    :return:
    data
    """
    try:
        all_data = pandas.read_csv(interface_dict["get_nicorn_company"], index_col=0, )
        r_data = requests.get(url=interface_dict["get_nicorn_company_json"], headers=headers)
        r_data.encoding = "gbk"
        data_json = r_data.json()
        data = pandas.DataFrame(data_json["data"]["horse"])
        if indicator == "部分":
            return all_data
        elif indicator == "详细":
            return data
        else:
            pandas.DataFrame({"参数不存在": list()})
    except:
        return pandas.DataFrame({})


def get_maxima_company() -> pandas.DataFrame:
    """
    千里马公司
    https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/data/data_juzi/maxima.csv
    https://www.itjuzi.com/api/maxima/?page=1&com_prov=&cat_id=&order_id=1&com_name=
    :return:
    """
    try:
        all_data = pandas.read_csv(interface_dict["get_maxima_company"], index_col=0)
        all_data.head().append(all_data.tail())
        r_data = requests.get(url=interface_dict["get_maxima_company_json"], headers=headers)
        r_data.encoding = "utf-8"
        data_json = r_data.json()
        data_ = data_json["data"]["data"]
        data_ = pandas.DataFrame(data_)
        data = all_data.append(data_, ignore_index=True)
        data.drop_duplicates(inplace=True)
        return data
    except:
        return pandas.DataFrame({})
