# -*- coding: utf-8 -*-


from fake_headers import Headers

"""headers"""
header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)
headers = header.generate()

BOX = 'boxOffice'

MOVIE_BOX = 'http://www.cbooo.cn/%s/GetHourBoxOffice?d=%s'

"""interface_dict"""
interface_dict = {
    "get_realtime_boxOffice": "https://www.endata.com.cn/API/GetData.ashx",
    "get_js": "http://www.gopup.cn/static/lib/webDES.js",
    "get_day_boxOffice": "https://www.endata.com.cn/API/GetData.ashx",
    "get_day_cinema": "https://www.endata.com.cn/API/GetData.ashx",
    "get_realtime_tv": "https://www.endata.com.cn/API/GetData.ashx",
    "get_realtime_show": "https://www.endata.com.cn/API/GetData.ashx",
    "get_realtime_artist": "https://www.endata.com.cn/API/GetData.ashx",
    "get_realtime_artist_flow": "https://www.endata.com.cn/API/GetData.ashx",
}
