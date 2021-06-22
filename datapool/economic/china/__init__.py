# -*- coding: utf-8 -*-
"""
@file: __init__.py.py
@time: 2021/6/22
@desc:
"""

"""

"""
interface_dict = {
    "get_marco_cmlrd": "http://114.115.232.154:8080/handler/download.ashx",
    "get_gdp_quarter": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
}

"""get_marco_cmlrd"""
marco_cmlrd_table = [
    "年份", "居民部门", "非金融企业部门", "中央政府", "地方政府", "政府部门", "实体经济部门", "金融部门资产方", "金融部门负债方"
]

"""get_gdp_quarter"""
gdp_quarter_params = {
    "type": "GJZB",
    "sty": "ZGZB",
    "p": "1",
    "ps": "200",
    "mkt": "20"
}
gdp_quarter_table = [
    "季度", "国内生产总值 绝对值(亿元)", "国内生产总值 同比增长", "第一产业 绝对值(亿元)", "第一产业 同比增长", "第二产业 绝对值(亿元)", "第二产业 同比增长", "第三产业 绝对值(亿元)",
    "第三产业 同比增长"
]

""""""
