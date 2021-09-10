# -*- coding: utf-8 -*-


import json
import pandas
import requests
from params import *

"""
http://img.kekepu.com/gaoxiao.json
"""


def get_university() -> pandas.DataFrame:
    """
    获取全国普通高等学校名单
    :return:
    :data:
    data.columns:
    序号
    学校名称
    学校标识码
    主管部门
    所在省市
    所在地
    办学层次
    备注
    """
    try:
        r = requests.get(url=interface_dict["get_university"], headers=headers)
        datas = json.loads(r.text)
        res_list = list()
        for data in datas:
            for d in datas[data]:
                tmp = {}
                tmp['序号'] = d['序号']
                tmp['学校名称'] = d['学校名称']
                tmp['学校标识码'] = d['学校标识码']
                tmp['主管部门'] = d['主管部门']
                tmp['所在省市'] = data
                tmp['所在地'] = d['所在地']
                tmp['办学层次'] = d['办学层次']
                tmp['备注'] = d['备注']
                res_list.append(tmp)
        res_data = pandas.DataFrame(res_list)
        res_data.to_csv("data.csv")
        return res_data
    except:
        return pandas.DataFrame({})


def get_adult_university() -> pandas.DataFrame:
    """
    获取全国成人高等学校名单
    :return:
    :data:
    data.columns
    序号
    学校名称
    学校标识码
    主管部门
    备注
    """
    try:
        data = pandas.read_csv("data.csv")
        return data
    except:
        return pandas.DataFrame({})
