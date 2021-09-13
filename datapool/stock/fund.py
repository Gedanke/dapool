# -*- coding: utf-8 -*-


import json
import pandas
import requests
from py_mini_racer import MiniRacer
from params import *


def get_fund_etf_category_sina(symbol="封闭式基金") -> pandas.DataFrame:
    """
    基金列表
    http://vip.stock.finance.sina.com.cn/fund_center/index.html#jjhqetf
    :param symbol: choice of {"封闭式基金", "ETF基金", "LOF基金"}
    :return:
    指定 symbol 的基金列表
    """
    fund_map = {
        "封闭式基金": "close_fund",
        "ETF基金": "etf_hq_fund",
        "LOF基金": "lof_hq_fund",
    }
    params = {
        "page": "1",
        "num": "1000",
        "sort": "symbol",
        "asc": "0",
        "node": fund_map[symbol],
        "[object HTMLDivElement]": "qvvne",
    }
    r = requests.get(
        url=interface_dict["get_fund_etf_category_sina"],
        params=params, headers=headers
    )
    data_text = r.text
    data_json = json.loads(data_text[data_text.find("([") + 1:-2])
    temp_df = pandas.DataFrame(data_json)
    res_df = temp_df[["symbol", "name"]]
    return res_df


def get_fund_etf_hist_sina(symbol="sz159996") -> pandas.DataFrame:
    """
    ETF 基金的日行情数据
    http://finance.sina.com.cn/fund/quotes/159996/bc.shtml
    :param symbol: 基金名称, 可以通过 get_fund_etf_category_sina 函数获取
    :return:
    ETF 基金的日行情数据
    """
    url = f"https://finance.sina.com.cn/realstock/company/{symbol}/hisdata/klc_kl.js"
    r = requests.get(url=url, headers=headers)
    js_code = MiniRacer()
    # js_code.eval(js_code)
    dict_list = js_code.call('d', r.text.split("=")[1].split(";")[0].replace('"', ""))  # 执行 js 解密代码
    temp_df = pandas.DataFrame(dict_list)
    temp_df["date"] = pandas.to_datetime(temp_df["date"]).dt.date
    return temp_df
