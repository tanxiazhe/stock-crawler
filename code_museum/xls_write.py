import urllib.request
import json
import stock_reader
import xlrd
import xlwt
from xlutils.copy import copy
import os
from xueqiu import get_data
from xueqiu import get_response
from xueqiu import getFieldColDict
from xueqiu import write_f10_xls
import pandas as pd
import datetime

"""
all code are not used anymore in this package
"""
# in xueqiu_income_statement.py
def writeXlsIncomeStatements(shOrSz,fromRow,incomeStatements):
    FILE_NAME='is.xls'
    oldwb = xlrd.open_workbook(FILE_NAME, 'rw')
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    if(shOrSz=='SZ'):
        sheet = newwb.get_sheet(1)
    row = fromRow
    for i in range(0,len(incomeStatements)):
        incomeStatement = incomeStatements[i]
        href = incomeStatement[0]
        jsonStr=incomeStatement[1]
        data=json.loads(jsonStr)
        if (('list' in data)& (data['list'] is not None)):
            iSGroup = data['list']
            for iS in iSGroup:
                if ('name' in data):
                    sheet.write(row, 0, data['name'])
                sheet.write(row, 1, href)
                if ('compcode' in iS):
                    sheet.write(row, 2, iS['compcode'])
                if ('publishdate' in iS):
                    sheet.write(row, 3, iS['publishdate'])
                if ('begindate' in iS):
                    sheet.write(row, 4, iS['begindate'])
                if ('enddate' in iS):
                    sheet.write(row, 5, iS['enddate'])
                if ('reporttype' in iS):
                    sheet.write(row, 6, iS['reporttype'])
                if ('adjustdate' in iS):
                    sheet.write(row, 7, iS['adjustdate'])
                if ('accstacode' in iS):
                    sheet.write(row, 8, iS['accstacode'])
                if ('accstaname' in iS):
                    sheet.write(row, 9, iS['accstaname'])
                if ('bizinco' in iS):
                    sheet.write(row, 10, iS['bizinco'])
                if ('netinteinco' in iS):
                    sheet.write(row, 11, iS['netinteinco'])
                if ('inteinco' in iS):
                    sheet.write(row, 12, iS['inteinco'])
                if ('inteexpe' in iS):
                    sheet.write(row, 13, iS['inteexpe'])
                if ('netpouninco' in iS):
                    sheet.write(row, 14, iS['netpouninco'])
                if ('pouninco' in iS):
                    sheet.write(row, 15, iS['pouninco'])
                if ('pounexpe' in iS):
                    sheet.write(row, 16, iS['pounexpe'])
                if ('netintebizinco' in iS):
                    sheet.write(row, 17, iS['netintebizinco'])
                if ('intebizinco' in iS):
                    sheet.write(row, 18, iS['intebizinco'])
                if ('intebizexpe' in iS):
                    sheet.write(row, 19, iS['intebizexpe'])
                if ('nettradeinco' in iS):
                    sheet.write(row, 20, iS['nettradeinco'])
                if ('netfinderiinco' in iS):
                    sheet.write(row, 21, iS['netfinderiinco'])
                if ('exchggain' in iS):
                    sheet.write(row, 22, iS['exchggain'])
                if ('leaseinco' in iS):
                    sheet.write(row, 23, iS['leaseinco'])
                if ('netinvinco' in iS):
                    sheet.write(row, 24, iS['netinvinco'])
                if ('assoinvegrain' in iS):
                    sheet.write(row, 25, iS['assoinvegrain'])
                if ('valuechgloss' in iS):
                    sheet.write(row, 26, iS['valuechgloss'])
                if ('otherbizinco' in iS):
                    sheet.write(row, 27, iS['otherbizinco'])
                if ('bizincoitse' in iS):
                    sheet.write(row, 28, iS['bizincoitse'])
                if ('totbizincoform' in iS):
                    sheet.write(row, 29, iS['totbizincoform'])
                if ('bizexpe' in iS):
                    sheet.write(row, 30, iS['bizexpe'])
                if ('biztax' in iS):
                    sheet.write(row, 31, iS['biztax'])
                if ('bizadminexpen' in iS):
                    sheet.write(row, 32, iS['bizadminexpen'])
                if ('asseimpaloss' in iS):
                    sheet.write(row, 33, iS['asseimpaloss'])
                if ('deprexpe' in iS):
                    sheet.write(row, 34, iS['deprexpe'])
                if ('doubdebtsprov' in iS):
                    sheet.write(row, 35, iS['doubdebtsprov'])
                if ('otherbizexpe' in iS):
                    sheet.write(row, 36, iS['otherbizexpe'])
                if ('totbizcostitse' in iS):
                    sheet.write(row, 37, iS['totbizcostitse'])
                if ('netbizcostform' in iS):
                    sheet.write(row, 38, iS['netbizcostform'])
                if ('bizprofitse' in iS):
                    sheet.write(row, 39, iS['bizprofitse'])
                if ('operprofform' in iS):
                    sheet.write(row, 40, iS['operprofform'])
                if ('operprofit' in iS):
                    sheet.write(row, 41, iS['operprofit'])
                if ('nonbusiinco' in iS):
                    sheet.write(row, 42, iS['nonbusiinco'])
                if ('nonoexpe' in iS):
                    sheet.write(row, 43, iS['nonoexpe'])
                if ('proftotitse' in iS):
                    sheet.write(row, 44, iS['proftotitse'])
                if ('proftotform' in iS):
                    sheet.write(row, 45, iS['proftotform'])
                if ('totprofit' in iS):
                    sheet.write(row, 46, iS['totprofit'])
                if ('incotax' in iS):
                    sheet.write(row, 47, iS['incotax'])
                if ('netpro1itse' in iS):
                    sheet.write(row, 48, iS['netpro1itse'])
                if ('netpro1form' in iS):
                    sheet.write(row, 49, iS['netpro1form'])
                if ('netprofit' in iS):
                    sheet.write(row, 50, iS['netprofit'])
                if ('minysharrigh' in iS):
                    sheet.write(row, 51, iS['minysharrigh'])
                if ('netparecompprof' in iS):
                    sheet.write(row, 52, iS['netparecompprof'])
                if ('netpro2itse' in iS):
                    sheet.write(row, 53, iS['netpro2itse'])
                if ('netpro2form' in iS):
                    sheet.write(row, 54, iS['netpro2form'])
                if ('earlyundiprof' in iS):
                    sheet.write(row, 55, iS['earlyundiprof'])
                if ('otherreasadju' in iS):
                    sheet.write(row, 56, iS['otherreasadju'])
                if ('netavaiitse' in iS):
                    sheet.write(row, 57, iS['netavaiitse'])
                if ('butprofform' in iS):
                    sheet.write(row, 58, iS['butprofform'])
                if ('avaidistprof' in iS):
                    sheet.write(row, 59, iS['avaidistprof'])
                if ('legalsurp' in iS):
                    sheet.write(row, 60, iS['legalsurp'])
                if ('statextrundi' in iS):
                    sheet.write(row, 61, iS['statextrundi'])
                if ('generiskrese' in iS):
                    sheet.write(row, 62, iS['generiskrese'])
                if ('trustloss' in iS):
                    sheet.write(row, 63, iS['trustloss'])
                if ('otherdistprof' in iS):
                    sheet.write(row, 64, iS['otherdistprof'])
                if ('sharprofitse' in iS):
                    sheet.write(row, 65, iS['sharprofitse'])
                if ('sharprofform' in iS):
                    sheet.write(row, 66, iS['sharprofform'])
                if ('avaidistshareprof' in iS):
                    sheet.write(row, 67, iS['avaidistshareprof'])
                if ('prefstockdivi' in iS):
                    sheet.write(row, 68, iS['prefstockdivi'])
                if ('extrarbirese' in iS):
                    sheet.write(row, 69, iS['extrarbirese'])
                if ('dealwithdivi' in iS):
                    sheet.write(row, 70, iS['dealwithdivi'])
                if ('turncapsdivi' in iS):
                    sheet.write(row, 71, iS['turncapsdivi'])
                if ('othersharedistprof' in iS):
                    sheet.write(row, 72, iS['othersharedistprof'])
                if ('undiprofitse' in iS):
                    sheet.write(row, 73, iS['undiprofitse'])
                if ('undiprofform' in iS):
                    sheet.write(row, 74, iS['undiprofform'])
                if ('undiprof' in iS):
                    sheet.write(row, 75, iS['undiprof'])
                if ('othercompinco' in iS):
                    sheet.write(row, 76, iS['othercompinco'])
                if ('parecompinco' in iS):
                    sheet.write(row, 77, iS['parecompinco'])
                if ('minysharinco' in iS):
                    sheet.write(row, 78, iS['minysharinco'])
                if ('compincoamt' in iS):
                    sheet.write(row, 79, iS['compincoamt'])
                if ('parecompamt' in iS):
                    sheet.write(row, 80, iS['parecompamt'])
                if ('minysharamt' in iS):
                    sheet.write(row, 81, iS['minysharamt'])
                if ('basiceps' in iS):
                    sheet.write(row, 82, iS['basiceps'])
                if ('dilutedeps' in iS):
                    sheet.write(row, 83, iS['dilutedeps'])
                row=row+1

    os.remove(FILE_NAME)
    newwb.save(FILE_NAME)
    print(row)
    return row


# in xueqiu_balance_sheet.py
import xlrd
import xlwt

import os
from xueqiu import get_data
# from xueqiu import getFieldColDict
# from xueqiu import write_f10_xls
# from xlutils.copy import copy
# import MySQLdb
def writeXls(shOrSz, fromRow, results):
    FILE_NAME='bs.xls'
    oldwb = xlrd.open_workbook(FILE_NAME, 'r')
    fieldColDict = getFieldColDict(oldwb)
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    if(shOrSz=='SZ'):
        sheet = newwb.get_sheet(1)
    row = fromRow
    for i in range(0, len(results)):
        result = results[i]
        href = result[0]
        jsonStr=result[1]
        data=json.loads(jsonStr)
        if (('list' in data)& (data['list'] is not None)):
            listJson = data['list']
            for item in listJson:
                sheet.write(row, 1, href)
                for key, value in item.items():
                    col=fieldColDict.get(key,-1)
                    if(col==-1):
                        col=max(fieldColDict.values())+1
                        sheet.write(0,col,key)
                        fieldColDict[key]=col
                        print('newly added col:'+key)
                    sheet.write(row, col, value)
                row=row+1
    os.remove(FILE_NAME)
    newwb.save(FILE_NAME)
    print(row)
    return row


def get_bs_for_range_stocks():
    # SH 0-287-1779
    # SZ 0-951
    # fromRow=1
    sh_sz = 'SZ'
    range_start = 2871
    range_end = 2908
    fromRow = 1
    stock_list = stock_reader.read_industry_stock_list2('化工行业')
    data = get_data(stock_list, '/stock/f10/balsheet.json?size=10000&page=1', '../data/bs_化工行业')
    write_f10_xls(fromRow, data, '../data/bs_化工行业')

# in xueqiu_cash_flow_statement.py
# import MySQLdb
import xlrd
import xlwt
# from xlutils.copy import copy
# from xueqiu import get_data
# from xueqiu import get_response
# from xueqiu import getFieldColDict
# from xueqiu import write_f10_xls
def get_cfs_for_range_stocks():
    #SH 0-287-1779
    #SZ 0-951
    range_start=2871
    range_end=2908
    fromRow=1
    stock_list = stock_reader.read_industry_stock_list2('家电行业')
    data = get_data( stock_list, '/stock/f10/cfstatement.json?size=10000&page=1', '../data/cfs_家电')
    write_f10_xls(fromRow, data, '../data/cfs_家电')


# in xueqiu_income_statement.py
# import MySQLdb
import xlrd
import xlwt
# from xueqiu import getHeaders
# from xueqiu import get_data
# from xueqiu import write_f10_xls
# if __name__=="__main__":
#     #SH 287-17
#     #SZ 0-951
#     shOrSz='SZ'
#     rangeStart=951
#     rangeEnd=952
#     fromRow=18276
#     writeXlsIncomeStatements(shOrSz,fromRow,getIncomeStatements(shOrSz,rangeStart,rangeEnd))



def get_is_for_range_stocks():
    #SH 0-287-1779
    #SZ 0-951
    #fromRow=1
    sh_sz='SZ'
    range_start=2871
    range_end=2908
    fromRow=1
    stock_list = stock_reader.read_industry_stock_list(range_start, range_end)
    data = xueqiu.get_data(stock_list, '/stock/f10/incstatement.json?size=10000&page=1','../data/is_家电')
    xueqiu.write_f10_xls(fromRow,data,'../data/is_家电')

# in xueqiu.py
def getFieldColDict( workbook):
    field_col_dict = dict()
    old_sheet = workbook.sheet_by_index(0)
    for col in range(old_sheet.ncols):
        field_col_dict[old_sheet.cell_value(0, col)] = col
    return field_col_dict


def write_f10_xls(fromRow, results,fileName):
    fileName1 = fileName+".xls"
    oldwb = xlrd.open_workbook(fileName1, 'r')
    fieldColDict = getFieldColDict(oldwb)
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    sheet.write(0, 0, 'code')
    sheet.write(0, 1, 'name')
    sheet.write(0, 2, 'url')
    row = fromRow
    for i in range(0, len(results)):
        result = results[i]
        stock=result[0]
        name = result[1]
        href = result[2]
        jsonStr=result[3]
        data=json.loads(jsonStr)
        if ('list' in data)& (data['list'] is not None):
            listJson = data['list']
            for item in listJson:
                sheet.write(row, 0, stock)
                sheet.write(row, 1, name)
                sheet.write(row, 2, href)
                for key, value in item.items():
                    col=fieldColDict.get(key,-1)
                    if(col==-1):
                        if(fieldColDict):
                            col=max(fieldColDict.values())+1
                        else:
                            col=3
                        sheet.write(0,col,key)
                        fieldColDict[key]=col
                        print('newly added col:'+key)
                    sheet.write(row, col, value)
                row=row+1
    os.remove(fileName1)
    newwb.save(fileName1)
    print(row)
    return row
