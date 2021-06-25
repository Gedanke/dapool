# -*- coding: utf-8 -*-


import json
import pandas
import requests
import params
from fake_headers import Headers
from setting import date_kit as dk

"""
上海银行间同业拆放利率(Shibor)数据接口
"""
header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)


def get_shibor_data(year: int = None):
    """
    获取上海银行间同业拆放利率(Shibor)
    date : 日期
    ON : 隔夜拆放利率
    1W : 1 周拆放利率
    2W : 2 周拆放利率
    1M : 1 个月拆放利率
    3M : 3 个月拆放利率
    6M : 6 个月拆放利率
    9M : 9 个月拆放利率
    1Y : 1年拆放利率
    http://www.shibor.org/shibor/web/html/downLoad.html?nameNew=Historical_Shibor_Data_2019.xls&downLoadPath=data&nameOld=Shibor数据2019.xls&shiborSrc=http://www.shibor.org/shibor/
    :param year: 年份
    :return:
    """
    year = dk.get_year() if year is None else year
    lab = params.SHIBOR_TYPE['Shibor']
    try:
        url = params.SHIBOR_DATA_URL % (
            params.P_TYPE['http'], params.DOMAINS['shibor'], params.PAGES['dw'], 'Shibor', year, lab, year
        )
        r = requests.get(url, headers=header.generate())
        r.encoding = "utf-8"
        data = pandas.read_excel("/home/dfs/Downloads/Shibor数据2019.xls")
        data.columns = params.SHIBOR_COLS
        data["date"] = data["date"].map(lambda x: x.date())
        return data
    except:
        # return None
        return pandas.DataFrame({})


def get_shibor_quote_data(year: int = None):
    """
    获取 Shibor 银行报价数据
    date : 日期
    bank : 报价银行名称
    ON : 隔夜拆放利率
    ON_B : 隔夜拆放买入价
    ON_A : 隔夜拆放卖出价
    1W_B : 1 周买入
    1W_A : 1 周卖出
    2W_B : 买入
    2W_A : 卖出
    1M_B : 买入
    1M_A : 卖出
    3M_B : 买入
    3M_A : 卖出
    6M_B : 买入
    6M_A : 卖出
    9M_B : 买入
    9M_A : 卖出
    1Y_B : 买入
    1Y_A : 卖出
    :param year: 年份
    :return:
    """
    year = dk.get_year() if year is None else year
    lab = params.SHIBOR_TYPE['Quote']
    try:
        url = params.SHIBOR_DATA_URL % (
            params.P_TYPE['http'], params.DOMAINS['shibor'], params.PAGES['dw'], 'Quote', year, lab, year
        )
        r = requests.get(url, headers=header.generate())
        r.encoding = "utf-8"
        data = pandas.read_excel(r.content)
        data.columns = params.SHIBOR_Q_COLS
        data['date'] = data['date'].map(lambda x: x.date())
        return data
    except:
        return pandas.DataFrame({})


def get_shibor_means_data(year: int = None):
    """
    获取 Shibor 均值数据
    date : 日期
    其它分别为各周期 5、10、20 均价
    :param year: 年份
    :return:
    """
    year = dk.get_year() if year is None else year
    lab = params.SHIBOR_TYPE['Tendency']
    try:
        url = params.SHIBOR_DATA_URL % (
            params.P_TYPE['http'], params.DOMAINS['shibor'], params.PAGES['dw'], 'Shibor_Tendency', year, lab, year
        )
        r = requests.get(url, headers=header.generate())
        r.encoding = "utf-8"
        data = pandas.read_excel(r.content)
        data.columns = params.SHIBOR_MA_COLS
        data['date'] = data['date'].map(lambda x: x.date())
        return data
    except:
        return pandas.DataFrame({})


def get_lpr_data(start: str, end: str):
    """
    获取贷款市场报价利率(LPR)
    showDateCN:日期
    1Y : 1 年贷款基础利率
    5Y : 5 年贷款基础利率
    :param start: 起止日期
    :param end: 截止日期
    :return:
    """
    try:
        url = params.LPR_DATA_URL
        data = {
            "lang": "CN",
            "strStartDate": start,
            "strEndDate": end
        }
        r = requests.post(url, data=data, headers=header.generate())
        r.encoding = "utf-8"
        data_dict = json.loads(r.text)['records']
        data = pandas.DataFrame(data_dict)
        return data
    except:
        return pandas.DataFrame({})
