# -*- coding: utf-8 -*-


import os
from client import *


def set_token(token):
    """

    :param token:
    :return:
    """
    df = pandas.DataFrame([token], columns=['token'])
    user_home = os.path.expanduser('~')
    fp = os.path.join(user_home, 'gp.csv')
    df.to_csv(fp, index=False)


def get_token():
    """

    :return:
    """
    user_home = os.path.expanduser('~')
    fp = os.path.join(user_home, 'gp.csv')
    if os.path.exists(fp):
        df = pandas.read_csv(fp)
        return str(df.loc[0]['token'])
    else:
        print('请设置 gopup 的 token 凭证码，如果没有请访问 http://www.gopup.cn 注册申请')
        return None


def pro_api(token='', timeout=30):
    """
    初始化 pro API
    第一次可以通过 gp.set_token('your token') 来记录自己的 token 凭证
    临时 token 可以通过本参数传入
    """
    if token == '' or token is None:
        token = get_token()
    if token is not None and token != '':
        pro = DataApi(token=token, timeout=timeout)
        return pro
    else:
        raise Exception('api init error.')
