# -*- coding: utf-8 -*-


import os
import json
import pandas
import requests
import execjs
from params import *
from setting.date_kit import get_today, day_last_date


def get_js():
    """

    :param js_url:
    :return:
    """
    r = requests.get(url=interface_dict["get_js"], headers=headers)
    return r.text


def get_realtime_boxOffice() -> pandas.DataFrame:
    """
    获取实时电影票房数据
    数据来源: EBOT艺恩票房智库 https://www.endata.com.cn/BoxOffice
    :return:
    :data:
    data.columns
    BoxOffice     实时票房(万)
    Irank         排名
    MovieName     影片名
    boxPer        票房占比(%)
    movieDay      上映天数
    sumBoxOffice  累计票房(万)
    default_url   影片海报
    """
    try:
        data = {
            "tdate": get_today(),
            "MethodName": "BoxOffice_GetHourBoxOffice"
        }
        r = requests.post(
            url=interface_dict["get_realtime_boxOffice"], data=data, headers=headers
        )
        js = get_js()

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table1']
            res_pandas = pandas.DataFrame(tmp)
            res_pandas = res_pandas.drop(columns=['moblie_url', 'larger_url', 'mId', 'MovieImg'])
            return res_pandas
        else:
            return pandas.DataFrame({})
    except Exception as e:
        return pandas.DataFrame({})


def get_day_boxOffice(date=None) -> pandas.DataFrame:
    """
    获取单日电影票房数据
    数据来源: EBOT艺恩票房智库 https://www.endata.com.cn/BoxOffice
    :param date:
    :return:
    :data:
    data.columns
    Irank         排名
    MovieName     影片名
    BoxOffice     单日票房(万)
    BoxOffice_Up  环比变化
    SumBoxOffice  累计票房(万)
    default_url   影片海报
    AvgPrice      平均票价
    AvpPeoPle     场均人次
    RapIndex      口碑指数
    MovieDay      上映天数
    """
    try:
        if date == None:
            edate = get_today()
        else:
            edate = date
        sdate = day_last_date(edate, days=1)
        data = {
            "sdate": sdate,
            "edate": edate,
            "MethodName": "BoxOffice_GetDayBoxOffice"
        }
        r = requests.post(
            url=interface_dict["get_day_boxOffice"], data=data, headers=headers
        )
        js = get_js()

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pandas = pandas.DataFrame(tmp)
            res_pandas = res_pandas.drop(
                columns=[
                    'MovieImg', 'moblie_url', 'larger_url', 'MovieID', 'Director', 'BoxOffice1',
                    'IRank_pro', 'RapIndex'
                ]
            )
            return res_pandas
        else:
            pandas.DataFrame({})
    except Exception as e:
        return pandas.DataFrame({})


def get_day_cinema(date=None) -> pandas.DataFrame:
    """
    获取单日影院票房
    :param date:
    :return:
    :data:
    data.columns
    RowNum         排名
    CinemaName     影院名称
    TodayBox       单日票房(元)
    TodayShowCount 单日场次
    AvgPeople      场均人次
    price          场均票价(元)
    Attendance     上座率
    """
    try:
        data = {
            "date": date,
            "rowNum1": 1,
            "rowNum2": 100,
            "MethodName": "BoxOffice_GetCinemaDayBoxOffice"
        }
        r = requests.post(
            url=interface_dict["get_day_cinema"], data=data, headers=headers
        )
        js = get_js()

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pandas = pandas.DataFrame(tmp)
            res_pandas = res_pandas.drop(
                columns=['CinemaID', 'TodayAudienceCount', 'TodayOfferSeat'])
            return res_pandas
        else:
            return pandas.DataFrame({})
    except Exception as e:
        return pandas.DataFrame({})


def get_realtime_tv() -> pandas.DataFrame:
    """
    获取实时电视剧播映指数
    数据来源: EBOT 艺恩票房智库 https://www.endata.com.cn/BoxOffice/Video/index.html
    :return:
    :data:
    data.columns
    TvName        名称
    Irank         排名
    Genres        类型
    PlayIndex     播映指数
    MediaHot      媒体热度
    UserHot       用户热度
    AnswerHot     好评度
    PlayHot       观看度
    date          日期
    """
    try:
        data = {
            "tvType": 2,
            "MethodName": "BoxOffice_GetTvData_PlayIndexRank"
        }
        r = requests.post(
            url=interface_dict["get_realtime_tv"], data=data, headers=headers
        )
        js = get_js()

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pandas = pandas.DataFrame(tmp)
            res_pandas['date'] = res_dict['Data']['Table1'][0]['MaxDate']
            return res_pandas
        else:
            return pandas.DataFrame({})
    except Exception as e:
        return pandas.DataFrame({})


def get_realtime_show() -> pandas.DataFrame:
    """
    获取实时综艺播映指数
    数据来源: EBOT艺恩票房智库 https://www.endata.com.cn/BoxOffice/Video/index.html
    :return:
    :data:
    data.columns
    TvName        名称
    Irank         排名
    Genres        类型
    PlayIndex     播映指数
    MediaHot      媒体热度
    UserHot       用户热度
    AnswerHot     好评度
    PlayHot       观看度
    date          日期
    """
    try:
        data = {
            "tvType": 8,
            "MethodName": "BoxOffice_GetTvData_PlayIndexRank"
        }
        r = requests.post(
            url=interface_dict["get_realtime_show"], data=data, headers=headers
        )
        js = get_js()

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pandas = pandas.DataFrame(tmp)
            res_pandas['date'] = res_dict['Data']['Table1'][0]['MaxDate']
            return res_pandas
        else:
            return pandas.DataFrame({})
    except Exception as e:
        return pandas.DataFrame({})


def get_realtime_artist() -> pandas.DataFrame:
    """
    获取艺人商业价值
    数据来源: EBOT艺恩票房智库 https://www.endata.com.cn/BoxOffice/Marketing/Artist/business.html
    :return:
    :data:
    data.columns
    StarBaseName  艺人
    Irank         排名
    BusinessValueIndex_L1  商业价值
    MajorHotIndex_L2       专业热度
    FocusHotIndex_L2       关注热度
    PredictHotIndex_L2     预测热度
    ReputationIndex_L3     美誉度
    """
    try:
        data = {
            "Order": "BusinessValueIndex_L1",
            "OrderType": "DESC",
            "PageIndex": 1,
            "PageSize": 100,
            "MethodName": "Data_GetList_Star"
        }
        r = requests.post(
            url=interface_dict["get_realtime_artist"], data=data, headers=headers
        )
        js = get_js()

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pandas = pandas.DataFrame(tmp)
            res_pandas = res_pandas.drop(columns=['StarBaseID'])
            return res_pandas
        else:
            return pandas.DataFrame({})
    except Exception as e:
        return pandas.DataFrame({})


def get_realtime_artist_flow() -> pandas.DataFrame:
    """
    获取艺人流量价值
    数据来源: EBOT艺恩票房智库 https://www.endata.com.cn/BoxOffice/Marketing/Artist/business.html
    :return:
    :data:
    data.columns
    StarBaseName  艺人
    Irank         排名
    FlowValueIndex_L1      流量价值
    MajorHotIndex_L2       专业热度
    FocusHotIndex_L2       关注热度
    PredictHotIndex_L2     预测热度
    TakeGoodsIndex_L2      带货力
    """
    try:
        data = {
            "Order": "FlowValueIndex_L1",
            "OrderType": "DESC",
            "PageIndex": 1,
            "PageSize": 100,
            "MethodName": "Data_GetList_Star"
        }
        r = requests.post(
            url=interface_dict["get_realtime_artist_flow"], data=data, headers=headers
        )
        js = get_js()

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pandas = pandas.DataFrame(tmp)
            res_pandas = res_pandas.drop(
                columns=['StarBaseID', 'ReputationIndex_L3', 'BusinessValueIndex_L1']
            )
            return res_pandas
        else:
            return pandas.DataFrame({})
    except Exception as e:
        return pandas.DataFrame({})


def _get_js_path(name, module_file):
    """
    获取 JS 文件的路径(从模块所在目录查找)
    :param name: 文件名
    :param module_file: filename
    :return:
    """
    module_folder = os.path.abspath(os.path.dirname(os.path.dirname(module_file)))
    module_json_path = os.path.join(module_folder, "movie", name)
    return module_json_path
