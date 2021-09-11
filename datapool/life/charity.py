# -*- coding: utf-8 -*-


import pandas
import requests
from tqdm import tqdm
from pyquery import PyQuery
from params import *


def get_page_num_charity_organization():
    """
    慈善中国-慈善组织查询-总页数
    :return: 总页数
    """
    url = "https://cszg.mca.gov.cn/biz/ma/csmh/a/csmhaindex.html"
    payload_params = {
        "aaee0102_03": "",
        "field": "aaex0131",
        "sort": "desc",
        "flag": "0",
    }
    payload_data = {"pageNo": "1"}
    r = requests.post(
        url=interface_dict["get_page_num_charity_organization"],
        params=payload_params["get_page_num_charity_organization"],
        data=payload_data, headers=headers
    )
    pages = r.text[r.text.find("第1页/共") + 5: r.text.rfind("页</font>")]
    return int(pages)


def get_charity_organization():
    """
    慈善中国-慈善组织查询
    https://cszg.mca.gov.cn/biz/ma/csmh/a/csmhaindex.html
    :return: 慈善中国-慈善组织查询
    :rtype: pandas.DataFrame
    """
    page_num = get_page_num_charity_organization()
    url = "https://cszg.mca.gov.cn/biz/ma/csmh/a/csmhaindex.html"
    params = {
        "field": "aaex0131",
        "sort": "desc",
        "flag": "0",
    }
    outer_df = pandas.DataFrame()
    for page in tqdm(range(1, page_num + 1)):
        # page = 1
        params["pageNo"] = str(page)

        r = requests.post(
            url=interface_dict["get_charity_organization"],
            params=params_dict["get_charity_organization"], headers=headers
        )
        inner_df = pandas.read_html(r.text)[0]
        outer_df = outer_df.append(inner_df, ignore_index=True)
    return outer_df
