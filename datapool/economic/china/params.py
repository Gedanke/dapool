# -*- coding: utf-8 -*-


"""
该文件存放当前目录下所有文件内的接口地址，dataFrame 的表头，参数等等
"""

"""interface_dict"""
interface_dict = {
    "get_marco_cmlrd": "http://114.115.232.154:8080/handler/download.ashx",
    "get_gdp_quarter": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
    "get_cpi": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
    "get_ppi": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
    "get_pmi": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
    "get_rrr": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
    "get_money_supply": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
    "get_gold_and_foreign_reserves": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
    "get_industrial_growth": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
    "get_fiscal_revenue": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
    "get_consumer_total": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
    "get_credit_data": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx",
    "get_fdi_data": "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
}

"""get_marco_cmlrd"""
marco_cmlrd_table = [
    "年份", "居民部门", "非金融企业部门", "中央政府", "地方政府", "政府部门", "实体经济部门", "金融部门资产方", "金融部门负债方"
]

"""params"""
params_dict = {
    "get_gdp_quarter": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "20"
    },
    "get_cpi": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "19"
    },
    "get_ppi": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "22"
    },
    "get_pmi": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "21"
    },
    "get_rrr": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "23"
    },
    "get_money_supply": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "11"
    },
    "get_gold_and_foreign_reserves": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "16"
    },
    "get_industrial_growth": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "0"
    },
    "get_fiscal_revenue": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "14"
    },
    "get_consumer_total": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "5"
    },
    "get_credit_data": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "7"
    },
    "get_fdi_data": {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "15"
    }
}

"""table"""
table_dict = {
    "get_gdp_quarter": [
        "季度", "国内生产总值 绝对值(亿元)", "国内生产总值 同比增长", "第一产业 绝对值(亿元)", "第一产业 同比增长", "第二产业 绝对值(亿元)", "第二产业 同比增长", "第三产业 绝对值(亿元)",
        "第三产业 同比增长"
    ],
    "get_cpi": [
        "月份", "全国当月", "全国同比增长", "全国环比增长", "全国累计", "城市当月", "城市同比增长", "城市环比增长", "城市累计", "农村当月", "农村同比增长",
        "农村环比增长", "农村累计"
    ],
    "get_ppi": [
        "月份", "当月", "当月同比增长", "累计"
    ],
    "get_pmi": [
        "月份", "制造业指数", "制造业同比增长", "非制造业指数", "非制造业同比增长"
    ],
    "get_rrr": [
        "公布时间", "生效时间", "大型金融机构 调整前", "大型金融机构 调整后", "大型金融机构 调整幅度", "中小型金融机构 调整前", "中小型金融机构 调整后", "中小型金融机构 调整幅度",
        "备注", "消息公布次日指数涨跌 上证", "消息公布次日指数涨跌 深证"
    ],
    "get_money_supply": [
        "月份", "货币和准货币(M2) 数量(亿元)", "货币和准货币(M2) 同比增长", "货币和准货币(M2) 环比增长", "货币(M1) 数量(亿元)",
        "货币(M1) 同比增长	", "货币(M1) 环比增长", "流通中的现金(M0) 数量(亿元)", "流通中的现金(M0) 同比增长", "流通中的现金(M0) 环比增长"
    ],
    "get_gold_and_foreign_reserves": [
        "月份", "国家外汇储备(亿美元) 数值", "国家外汇储备(亿美元) 同比", "国家外汇储备(亿美元) 环比", "黄金储备(万盎司) 数值", "黄金储备(万盎司) 同比", "黄金储备(万盎司) 环比"
    ],
    "get_industrial_growth": [
        "月份", "同比增长%", "累计增长%"
    ],
    "get_fiscal_revenue": [
        "月份", "当月(亿元)", "同比增长", "环比增长", "累计(亿元)", "同比增长"
    ],
    "get_consumer_total": [
        "月份", "当月(亿元)", "同比增长", "环比增长", "累计(亿元)", "同比增长"
    ],
    "get_credit_data": [
        "月份", "当月(亿元)", "同比增长", "环比增长", "累计(亿元)", "同比增长"
    ],
    "get_fdi_data": [
        "月份", "当月(十万元)", "同比增长", "环比增长", "累计(十万元)", "同比增长"
    ]
}
