# -*- coding: utf-8 -*-


import re
import datetime
import pandas
import requests
import matplotlib.pyplot as plt
from fake_headers import Headers
from params import *

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 显示中文标签

header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)
headers = header.generate()
headers["Referer"] = "http://data.weibo.com/index/newindex"
headers["Origin"] = "https://data.weibo.com"

"""
https://data.weibo.com/index/ajax/newindex/searchword
http://data.weibo.com/index/ajax/newindex/getchartdata
"""


def get_items(word="股票") -> dict:
    """
    :param word:
    :return:
    """
    r = requests.post(
        url=interface_dict["index_weibo_get_items"], data={
            "word": word
        }, headers=headers
    )
    if r.status_code == 200:
        return {
            word: re.findall(r"\d+", r.json()["html"])[0]
        }
    else:
        return {}


def get_index_data(wid, time_type) -> pandas.DataFrame:
    """
    :param wid:
    :param time_type:
    :return:
    """
    r = requests.get(
        url=interface_dict["index_weibo_get_index_data"], params={
            "wid": wid,
            "dateGroup": time_type,
        }, headers=headers
    )
    data_json = r.json()
    data = {
        "index": data_json["data"][0]["trend"]["x"],
        "value": data_json["data"][0]["trend"]["s"],
    }
    return pandas.DataFrame(data)


def get_process_index(index) -> str:
    """
    
    :param index: 
    :return: 
    """
    now = datetime.datetime.now()
    curr_year = now.year
    curr_date = "%04d%02d%02d" % (now.year, now.month, now.day)
    if "月" in index:
        tmp = index.replace("日", "").split("月")
        date = "%04d%02d%02d" % (curr_year, int(tmp[0]), int(tmp[1]))
        if date > curr_date:
            date = "%04d%02d%02d" % (curr_year - 1, int(tmp[0]), int(tmp[1]))
        return date
    return index


def get_weibo_index(word="python", time_type="3month") -> pandas.DataFrame:
    """
    weibo index
    :param word:
    :param time_type: 1hour, 1day, 1month, 3month
    :return:
    """
    try:
        dict_keyword = get_items(word)
        df_list = []
        for keyword, wid in dict_keyword.items():
            df = get_index_data(wid, time_type)
            if df is not None:
                df.columns = ["index", keyword]
                df["index"] = df["index"].apply(lambda x: get_process_index(x))
                df.set_index("index", inplace=True)
                df_list.append(df)
        if len(df_list) > 0:
            df = pandas.concat(df_list, axis=1)
            if time_type == "1hour" or "1day":
                df.index = pandas.to_datetime(df.index)
            else:
                df.index = pandas.to_datetime(df.index, format="%Y%m%d")
            return df
    except:
        return pandas.DataFrame({})
