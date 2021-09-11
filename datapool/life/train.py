# -*- coding: utf-8 -*-


import os
import demjson
import pandas
import requests
from pyquery import PyQuery
from params import *

"""
https://kyfw.12306.cn/otn/resources/js/framework/station_name.js
https://kyfw.12306.cn/otn/resources/js/query/train_list.js
"""


def get_station_name() -> pandas.DataFrame:
    """
    获取 12306 车站信息
    :return: 
    :data:
    data.columns
    拼音码, 站名, 电报码, 拼音, 首字母, ID
    """
    try:
        r = requests.get(url=interface_dict["get_station_name"], headers=headers)
        data_text = r.text
        tmp_str = data_text[data_text.find("='") + 3: -2]
        tmp_list = tmp_str.split('@')
        res_list = [
            li.split('|') for li in tmp_list
        ]
        columns = ["拼音码", "站名", "电报码", "拼音", "首字母", "ID"]
        data = pandas.DataFrame(res_list, columns=columns)
        data.set_index("ID", inplace=True)
        return data
    except:
        return pandas.DataFrame({})


def save_train_list():
    """

    :return:
    """
    r = requests.get(url=interface_dict["get_train_list"], headers=headers)
    data_text = r.text
    d = demjson.decode(data_text[data_text.find("={") + 1:])
    data = {
        "date": list(), "train_number": list(), "station_train_code": list(), "station_train_start": list(),
        "station_train_end": list(), "train_no": list()
    }
    for date_, v in d.items():
        for train_number_, vv in v.items():
            for i in vv:
                data["date"].append(date_)
                data["train_number"].append(train_number_)
                s = i["station_train_code"]
                idx = s.find("(")
                idx_ = s.find("-")
                data["station_train_code"].append(s[0:idx])
                data["station_train_start"].append(s[idx + 1:idx_])
                data["station_train_end"].append(s[idx_ + 1:-1])
                data["train_no"].append(i["train_no"])
    data = pandas.DataFrame(data)
    data.to_csv("train_data.csv", index=False)


if not os.path.exists("train_data.csv"):
    save_train_list()


def get_train_list() -> pandas.DataFrame:
    """

    :return:
    :data:
    data.columns
    date, TrainNumber, station_train_code, station_train_start, station_train_end, train_no
    """
    return pandas.read_csv("train_data.csv")


def get_train_time_table(train_number) -> pandas.DataFrame:
    """

    :param train_number:
    :return:
    :data:
    data.columns
    车次, 车型, 始发站, 终点站, 始发时, 终到时, 全程时间
    """
    try:
        url = "https://www.keyunzhan.com/dongche/%s/" % train_number
        r = requests.get(url=url, headers=headers)
        doc = PyQuery(r.text)
        tds = doc(".listTable td[bgcolor='#FFFFFF']")
        tmp = [
            v.text() for v in tds.items()
        ]
        res = {
            "车次": tmp[0],
            "车型": tmp[1],
            "始发站": tmp[2],
            "终点站": tmp[3],
            "始发时": tmp[4],
            "终到时": tmp[5],
            "全程时间": tmp[6]
        }
        data = pandas.DataFrame(res, index=[0])
        return data
    except:
        return pandas.DataFrame({})
