# -*- coding: utf-8 -*-


import pandas


def get_industry_classified(standard='sina') -> pandas.DataFrame:
    """
    获取行业分类数据
    :param standard: sina: 新浪行业 sw: 申万 行业
    :return:
    :data:
    data.columns
    code: 股票代码
    name: 股票名称
    c_name: 行业名称
    """
    try:
        if standard == 'sw':
            df = pandas.read_csv(
                'http://img.kekepu.com/industry_sw.csv', dtype={'code': object}
            )
        else:
            df = pandas.read_csv(
                'http://img.kekepu.com/industry.csv', dtype={'code': object}
            )
        return df
    except:
        return pandas.DataFrame({})


def get_concept_classified() -> pandas.DataFrame:
    """
    获取概念分类数据
    :return:
    :data:
    data.columns
    code: 股票代码
    name: 股票名称
    c_name: 概念名称
    """
    try:
        df = pandas.read_csv(
            'http://img.kekepu.com/concept.csv', dtype={'code': object}
        )
        return df
    except:
        return pandas.DataFrame({})
