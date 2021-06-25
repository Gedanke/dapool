# -*- coding: utf-8 -*-


import pandas
import requests
from fake_headers import Headers
from params import *

"""
link : http://datainterface.eastmoney.com
"""

header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)
headers = header.generate()


def get_basic(name: str) -> pandas.DataFrame:
    """
    通用方法
    :param name: 方法名称
    :return:
    """
    r = requests.get(
        interface_dict[name], params=params_dict[name], headers=headers
    )
    r.encoding = "utf-8"
    content = str(r.text)
    rows = content[content.find("[") + 2:-3]
    data_list = [
        row.split(",") for row in rows.split('","')
    ]
    data = pandas.DataFrame(data_list, columns=table_dict[name])
    return data


def get_marco_cmlrd() -> pandas.DataFrame:
    """
    中国宏观杠杆率
    :return:
    """
    data = pandas.read_excel(
        interface_dict["get_marco_cmlrd"], sheet_name="Data", header=0, skiprows=1
    )
    data["Period"] = pandas.to_datetime(data["Period"]).dt.strftime("%Y-%m")
    table = list(data.columns)
    data = data[table[:len(marco_cmlrd_table)]]
    data.columns = marco_cmlrd_table
    return data


def get_gdp_quarter() -> pandas.DataFrame:
    """
    季度国内生产总值
    :return:
    """
    return get_basic("get_gdp_quarter")


def get_cpi() -> pandas.DataFrame:
    """
    居民消费价格指数数据
    :return:
    """
    return get_basic("get_cpi")


def get_ppi() -> pandas.DataFrame:
    """
    工业品出厂价格指数数据
    :return:
    """
    return get_basic("get_ppi")


def get_pmi() -> pandas.DataFrame:
    """
    获取采购经理人指数
    :return:
    """
    return get_basic("get_pmi")


def get_rrr() -> pandas.DataFrame:
    """
    存款准备金率数据
    :return:
    """
    return get_basic("get_rrr")


def get_money_supply() -> pandas.DataFrame:
    """
    货币供应量数据
    :return:
    """
    return get_basic("get_money_supply")


def get_gold_foreign_reserves() -> pandas.DataFrame:
    """
    外汇储备
    :return:
    """
    return get_basic("get_gold_and_foreign_reserves")


def get_industrial_growth() -> pandas.DataFrame:
    """
    工业增加值增长
    :return:
    """
    return get_basic("get_industrial_growth")


def get_fiscal_revenue() -> pandas.DataFrame:
    """
    财政收入
    :return:
    """
    return get_basic("get_fiscal_revenue")


def get_consumer_total() -> pandas.DataFrame:
    """
    社会消费品零售总额
    :return:
    """
    return get_basic("get_consumer_total")


def get_credit_data() -> pandas.DataFrame:
    """
    信贷数据
    :return:
    """
    return get_basic("get_credit_data")


def get_fdi_data() -> pandas.DataFrame:
    """
    外商直接投资数据(FDI)
    :return:
    """
    data = get_basic("get_fdi_data")
    # data['当月(亿元)'] = data['当月(亿元)'].map(lambda x: int(x)/100000)
    # data['累计(亿元)'] = data['累计(亿元)'].map(lambda x: int(x)/100000)
    return data
