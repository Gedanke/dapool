# -*- coding: utf-8 -*-


import json
import pandas
import requests
from fake_headers import Headers
from params import *
from pyquery import PyQuery

pandas.options.mode.chained_assignment = None

"""
https://www.bjsoubang.com/#/
https://www.bjsoubang.com/api/getHistoryDaily
https://www.bjsoubang.com/api//getContentData
"""

header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)
headers = header.generate()


def get_history_daily() -> pandas.DataFrame:
    """
    历史上的今日
    :return:
    DataFrame
    year，title, type, link, desc, pic_calendar, pic_share, pic_index
    """
    try:
        url = interface_dict["get_history_daily"]
        r = requests.get(url=url, headers=headers)
        res_list = json.loads(r.text)['info']
        data = pandas.DataFrame(res_list)
        data = data.drop(['cover', 'festival', 'recommend'], axis=1)
        nums = len(data)
        data["title_shape"] = None
        data["content_shape"] = None
        for idx in range(nums):
            for table in ["title", "desc"]:
                c = PyQuery(data.loc[idx, table])
                data.loc[idx, table + "_shape"] = c.text()
        return data
    except:
        return pandas.DataFrame({})
