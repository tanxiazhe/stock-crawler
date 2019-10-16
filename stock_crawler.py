
import xueqiu.xueqiu
import xueqiu.xueqiu_base as xueqiu_base

if __name__ == "__main__":
    # SH 0-287-1779
    # SZ 0-951
    # fromRow=1
    shOrSz = 'SZ'
    rangeStart = 800
    rangeEnd = 951
    fromRow = 7737
    xueqiu.writeXls(shOrSz, fromRow, xueqiu_base.getData(shOrSz, rangeStart, rangeEnd, '/stock/f10/bonus.json'))