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
    "get_fund_etf_category_sina":"http://vip.stock.finance.sina.com.cn/quotes_service/api/jsonp.php/IO.XSRV2.CallbackList['da_yPT46_Ll7K6WD']/Market_Center.getHQNodeDataSimple"

}