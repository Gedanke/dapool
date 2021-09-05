# -*- coding: utf-8 -*-


import json
import pandas
import requests
import pandas
from params import *
from fake_headers import Headers

"""
https://huiyan.baidu.com/

"""

header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)
headers = header.generate()


def get_migration_area_baidu(area="武汉市", indicator="move_in", date="20200201") -> pandas.DataFrame:
    """
    百度地图慧眼-百度迁徙-XXX迁入地详情
    百度地图慧眼-百度迁徙-XXX迁出地详情
    以上展示 top100 结果，如不够 100 则展示全部
    迁入来源地比例: 从 xx 地迁入到当前区域的人数与当前区域迁入总人口的比值
    迁出目的地比例: 从当前区域迁出到 xx 的人口与从当前区域迁出总人口的比值
    https://qianxi.baidu.com/?from=shoubai#city=0
    :param area: 可以输入 省份 或者 具体城市 但是需要用全称
    :param indicator: move_in 迁入 or move_out 迁出
    :param date: 查询的日期 20200101 以后的时间
    :return:
    :data: 迁入地详情/迁出地详情的前50个
    """
    try:
        if area == "全国":
            payload = {
                "dt": "country",
                "id": 0,
                "type": indicator,
                "date": date,
            }
        else:
            city_dict.update(province_dict)
            inner_dict = dict(zip(city_dict.values(), city_dict.keys()))
            if inner_dict[area] in province_dict.keys():
                dt_flag = "province"
            else:
                dt_flag = "city"
            payload = {
                "dt": dt_flag,
                "id": inner_dict[area],
                "type": indicator,
                "date": date,
            }
        '''request'''
        url = interface_dict["get_migration_area_baidu"]
        r = requests.get(url, params=payload)
        data = json.loads(r.text[r.text.find("({") + 1: r.text.rfind(");")])
        return pandas.DataFrame(data["data"]["list"])
    except:
        return pandas.DataFrame({})


def get_migration_scale_baidu(area="武汉市", indicator="move_out", date="20210112") -> pandas.DataFrame:
    """
    百度地图慧眼-百度迁徙-迁徙规模
    * 迁徙规模指数：反映迁入或迁出人口规模，城市间可横向对比
    * 城市迁徙边界采用该城市行政区划，包含该城市管辖的区、县、乡、村
    https://qianxi.baidu.com/?from=shoubai#city=0
    :param area: 可以输入 省份 或者 具体城市 但是需要用全称
    :param indicator: move_in 迁入 or move_out 迁出
    :param date: 结束查询的日期 20200101 以后的时间
    :return:
    :data: 时间序列的迁徙规模指数
    """
    try:
        if area == "全国":
            payload = {
                "dt": "country",
                "id": 0,
                "type": indicator,
                "date": date
            }
        else:
            city_dict.update(province_dict)
            inner_dict = dict(zip(city_dict.values(), city_dict.keys()))
            try:
                if inner_dict[area] in province_dict.keys():
                    dt_flag = "province"
                else:
                    dt_flag = "city"

                payload = {
                    "dt": dt_flag,
                    "id": inner_dict[area],
                    "type": indicator,
                    "date": date
                }
            except Exception as e:
                return pandas.DataFrame({"省份": list(), "或者": list(), "具体城市名": list(), "错误": list()})
        '''request'''
        url = interface_dict["get_migration_scale_baidu"]
        r = requests.get(url, params=payload, headers=headers)
        json_data = json.loads(r.text[r.text.find("({") + 1: r.text.rfind(");")])
        temp_df = pandas.DataFrame.from_dict(json_data["data"]["list"], orient="index")
        temp_df.index = pandas.to_datetime(temp_df.index)
        temp_df.columns = ["迁徙规模指数"]
        return temp_df
    except:
        return pandas.DataFrame({})
