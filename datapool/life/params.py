# -*- coding: utf-8 -*-


from fake_headers import Headers

"""headers"""
header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)
headers = header.generate()

"""interface_dict"""
interface_dict = {
    "get_university": "http://img.kekepu.com/gaoxiao.json",
    "get_station_name": "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js",
    "get_train_list": "https://kyfw.12306.cn/otn/resources/js/query/train_list.js",
    "get_energy_oil_hist": "http://datacenter.eastmoney.com/api/data/get",
    "get_energy_oil_detail": "http://datacenter.eastmoney.com/api/data/get",
    "get_charity_organization": "https://cszg.mca.gov.cn/biz/ma/csmh/a/csmhaindex.html",
    "get_page_num_charity_organization": "https://cszg.mca.gov.cn/biz/ma/csmh/a/csmhaindex.html"
}
params_dict = {
    "get_energy_oil_hist": {
        "type": "RPTA_WEB_YJ_BD",
        "sty": "ALL",
        "source": "WEB",
        "p": "1",
        "ps": "5000",
        "st": "dim_date",
        "sr": "-1",
        "var": "OxGINxug",
        "rt": "52861006",
    },
    "get_energy_oil_detail": {
        "type": "RPTA_WEB_YJ_JH",
        "sty": "ALL",
        "source": "WEB",
        "p": "1",
        "ps": "5000",
        "st": "cityname",
        "sr": "1",
        "filter": "",
        "var": "todayPriceData",
    },
    "get_page_num_charity_organization": {
        "aaee0102_03": "",
        "field": "aaex0131",
        "sort": "desc",
        "flag": "0",
    },
    "get_charity_organization": {
        "field": "aaex0131",
        "sort": "desc",
        "flag": "0",
    }
}
