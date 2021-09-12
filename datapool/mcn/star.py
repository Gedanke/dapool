# -*- coding: utf-8 -*-


import time
import requests
import pandas
from params import *


def get_star_hot_list(section, hot_list, category, cookie):
    """
    星图热榜 抖音达人热榜
    :param section: 
    :param hot_list: 
    :param category: 
    :param cookie: 
    :return: 
    """
    headers["cookie"] = cookie
    params = "%s-%s-%s" % (section, hot_list, category)
    try:
        url = STAR_HOT_URL[params]
    except:
        return {"code": 401, "msg": "没有找到对应类型"}

    r = requests.get(url, headers=headers)

    publish_date = r.json()['data']['file_name'][-20:-1]
    data_all = r.json()['data']['stars']
    res_list = []
    new_rank = 1
    for data in data_all:
        res_dict = {
            "id": data['id'],
            "new_rank": new_rank,
            "nick_name": data['nick_name'],
            "avatar_uri": data['avatar_uri'],
            "province": data.setdefault('province'),
            "city": data['city'],
            "avg_play": data['avg_play'],
            "score": get_fields(data['fields'], "score"),
            "follower": get_fields(data['fields'], "follower"),
            "positive_vv": get_fields(data['fields'], "positive_vv"),
            "personal_interate_rate": get_fields(data['fields'], "personal_interate_rate"),
            "expected_cpm": get_fields(data['fields'], "expected_cpm"),
            "file_name": params,
            "publish_date": publish_date,
            "crawler_date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        res_list.append(res_dict)
        new_rank += 1
    data = pandas.DataFrame(res_list)
    return data


def get_star_market_list(section="抖音达人", market_list="抖音传播任务", category="全部", limit=30, page=1, cookie=None):
    """

    :param section:
    :param market_list:
    :param category:
    :param limit:
    :param page:
    :param cookie:
    :return:
    """
    cookie = cookie
    res_url = get_star_market_url(category, cookie)
    headers["cookie"] = cookie
    url = res_url % (limit, page)
    r = requests.get(url, headers=headers)
    try:
        res = r.json()['data']['authors']
    except:
        return {"msg": "cookie已经过期", "code": 401}
    return res


def get_star_market_url(category, cookie):
    """

    :param category:
    :param cookie:
    :return:
    """
    limit = 10
    res_url = ""
    if category == "全部":
        url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=1&platform_source=1&task_category=1&order_by=score&use_recommend=1" % limit
        res_url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=%s&platform_source=1&task_category=1&order_by=score&use_recommend=1"
    else:
        category_list = STAR_MARKET_DOUYIN_CATEGORY
        for cate in category_list:
            first_dict = cate['first']
            first_val = list(first_dict.values())[0]
            if category == first_val:
                tag = list(first_dict.keys())[0]
                url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=1&platform_source=1&task_category=1&tag=%s&order_by=score" % (
                    limit, tag)
                res_url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=%s&platform_source=1&task_category=1&tag=" + str(
                    tag) + "&order_by=score"
            else:
                second_list = cate['second']
                for second_dict in second_list:
                    second_val = list(second_dict.values())[0]
                    if category == second_val:
                        tag = list(first_dict.keys())[0]
                        tag_level_two = list(second_dict.keys())[0]
                        url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=1&platform_source=1&task_category=1&tag=%s&tag_level_two=%s&order_by=score" % (
                            limit, tag, tag_level_two)
                        res_url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=%s&platform_source=1&task_category=1&tag=" + str(
                            tag) + "&tag_level_two=" + str(tag_level_two) + "&order_by=score"

    # headers["cookie"] = cookie
    # r = requests.get(url, headers=headers)
    # total_count = r.json()['data']['pagination']['total_count']

    # return res_url, total_count
    return res_url
