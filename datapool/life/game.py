# -*- coding: utf-8 -*-


import time
import pandas
import requests
from pyquery import PyQuery
from params import *

"""
http://rank.uuu9.com/club/ranking?game_id=6&type=0
http://rank.uuu9.com/player/ranking?game_id=6&type=0
"""


def get_club_rank(type) -> pandas.DataFrame:
    """
    中国电竞价值排行榜 俱乐部排行榜
    http://rank.uuu9.com/club/ranking?game_id=6&type=0
    :param type:
    DOTA2  1
    英雄联盟 2
    绝地求生 3
    王者荣耀 4
    穿越火线 5
    和平精英 6
    :return:
    :data:
    data.columns
    日期、类型、排名、俱乐部logo、俱乐部名称、人气指数、舆论指数、综合指数、排名变动
    """
    if type == "DOTA2":
        game_id = 1
    elif type == "英雄联盟":
        game_id = 2
    elif type == "绝地求生":
        game_id = 3
    elif type == "王者荣耀":
        game_id = 4
    elif type == "穿越火线":
        game_id = 5
    elif type == "和平精英":
        game_id = 6
    else:
        return pandas.DataFrame({"游戏名称输入错误": list()})

    try:
        url = "http://rank.uuu9.com/club/ranking?game_id=%s&type=0" % game_id
        r = requests.get(url=url, headers=headers)
        doc = PyQuery(r.text)
        trs = doc(".ec_table table tbody tr")
        res_list = []
        for tr in trs.items():
            bd_res = tr(".ec_change i").attr("class")
            bd_val = tr(".ec_change").text()
            if bd_res == "rise":
                bd = "上升 %s 位" % bd_val
            elif bd_res == "decline":
                bd = "下降 %s 位" % bd_val
            else:
                bd = "-"
            res_dict = {
                "日期": time.strftime("%Y-%m-%d"),
                "类型": type,
                "排名": tr.find(".ec_num").text(),
                "俱乐部logo": "http://rank.uuu9.com/%s" % tr("img").attr("src"),
                "俱乐部名称": tr("dd").text(),
                "人气指数": tr("td:nth-child(3)").text(),
                "舆论指数": tr("td:nth-child(4)").text(),
                "综合指数": tr("td:nth-child(5)").text(),
                "排名变动": bd
            }
            res_list.append(res_dict)
        data = pandas.DataFrame(res_list)
        return data
    except:
        return pandas.DataFrame({})


def get_player_rank(type) -> pandas.DataFrame:
    """
    中国电竞价值排行榜 选手排行榜
    http://rank.uuu9.com/player/ranking?game_id=6&type=0
    :param type:
    DOTA2  1
    英雄联盟 2
    绝地求生 3
    王者荣耀 4
    穿越火线 5
    和平精英 6
    :return:
    :data:
    data.columns
    日期、类型、排名、选手头像、选手名、所属战队、人气指数、舆论指数、战绩指数、综合指数、身价、排名变动
    """
    if type == "DOTA2":
        game_id = 1
    elif type == "英雄联盟":
        game_id = 2
    elif type == "绝地求生":
        game_id = 3
    elif type == "王者荣耀":
        game_id = 4
    elif type == "穿越火线":
        game_id = 5
    elif type == "和平精英":
        game_id = 6
    else:
        return pandas.DataFrame({"游戏名称输入错误": list()})

    try:
        url = "http://rank.uuu9.com/player/ranking?game_id=%s&type=0" % game_id
        r = requests.get(url=url, headers=headers)
        doc = PyQuery(r.text)
        trs = doc(".ec_table table tbody tr")
        res_list = []
        for tr in trs.items():
            bd_res = tr(".ec_change i").attr("class")
            bd_val = tr(".ec_change").text()
            if bd_res == "rise":
                bd = "上升 %s 位" % bd_val
            elif bd_res == "decline":
                bd = "下降 %s 位" % bd_val
            else:
                bd = "-"
            if type == "英雄联盟":
                res_dict = {
                    "日期": time.strftime("%Y-%m-%d"),
                    "类型": type,
                    "排名": tr.find(".ec_num").text(),
                    "选手头像": "http://rank.uuu9.com/%s" % tr("img").attr("src"),
                    "选手名": tr("dd").text(),
                    "所属战队": tr("td:nth-child(3)").text(),
                    "人气指数": tr("td:nth-child(4)").text(),
                    "舆论指数": tr("td:nth-child(5)").text(),
                    "战绩指数": tr("td:nth-child(6)").text(),
                    "综合指数": tr("td:nth-child(7)").text(),
                    "身价": tr("td:nth-child(8)").text(),
                    "排名变动": bd
                }
            else:
                res_dict = {
                    "日期": time.strftime("%Y-%m-%d"),
                    "类型": type,
                    "排名": tr.find(".ec_num").text(),
                    "选手头像": "http://rank.uuu9.com/%s" % tr("img").attr("src"),
                    "选手名": tr("dd").text(),
                    "所属战队": tr("td:nth-child(3)").text(),
                    "人气指数": tr("td:nth-child(4)").text(),
                    "舆论指数": tr("td:nth-child(5)").text(),
                    "综合指数": tr("td:nth-child(6)").text(),
                    "身价": tr("td:nth-child(7)").text(),
                    "排名变动": bd
                }

            res_list.append(res_dict)
        data = pandas.DataFrame(res_list)
        return data
    except:
        return pandas.DataFrame({})
