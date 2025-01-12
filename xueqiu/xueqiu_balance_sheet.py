# -*- coding: utf-8 -*-
import urllib.request
import json
# import stock_reader
import xueqiu.xueqiu_base as xueqiu_base
import pandas as pd
import datetime


def get_bs_for_1_stock(str_stock_code):
    # stock_list=readStockList.read_industry_stock_list_by_code(stock_code)
    # data = get_data(stock_list, '/stock/f10/balsheet.json?size=10000&page=1', '../data/bs_'+stock_id)
    str_response = xueqiu_base.get_response(
        'https://stock.xueqiu.com/v5/stock/finance/cn/balance.json?symbol=' + str_stock_code + '&type=all&is_detail=true&count=10000')
    # write_f10_xls(1, data, '../data/bs_'+stock_id)
    json_data = json.loads(str_response)
    json_data = json_data['data']
    if (('list' in json_data) & (json_data['list'] is not None)):
        json_list = json_data['list']

        res_list = []

        for item in json_list:
            res = {}
            for key in dict(item).keys():
                if isinstance(item[key], list):
                    res[key.replace('_', '')] = item[key][0]
                else:
                    res[key.replace('_', '')] = item[key]
            res_list.append(res)

        str_list = json.dumps(res_list)
        df = pd.read_json(str_list, orient='records')
        df.to_excel(xueqiu_base.get_file_name('../data/bs/', 'bs_', str_stock_code))


def parseString(keys):
    return [map(lambda key: key.replace('_', ''), keys.keys())]
