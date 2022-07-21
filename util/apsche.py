#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2022/7/14 22:38'
import platform
from apscheduler.schedulers.blocking import BlockingScheduler

if platform.system().lower() == 'windows':
    from util.get_stock_info import getStockDateLineAll, getStockNameInfo
    from util.get_stock_rose import getRose
elif platform.system().lower() == 'linux':
    from get_stock_info import getStockDateLineAll, getStockNameInfo
    from get_stock_rose import getRose


scheduler = BlockingScheduler()


scheduler.add_job(getStockNameInfo, 'cron', day_of_week='*', hour=19, minute='00', second='00')
scheduler.add_job(getStockDateLineAll, 'cron', day_of_week='*', hour=19, minute='10', second='10')
scheduler.add_job(getRose, 'cron', day_of_week='*', hour=20, minute='00', second='00')
scheduler.start()
