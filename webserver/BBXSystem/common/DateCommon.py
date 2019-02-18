from datetime import datetime,date,timedelta
import calendar


def getMonthDateRang(target_date):
    '''
        获取指定日期的该月的全部日期
    :param target_date:
    :return:
    '''
    # 获取指定月份的全部日期
    start_date=target_date.replace(day=1)
    _,days_in_month=calendar.monthrange(target_date.year,target_date.month)
    end_date=start_date+timedelta(days=days_in_month)

    return (start_date,end_date)

def getDataRang(target_date:datetime,hours:int):
    '''
        将当前时间向后推days天
    :param target_date:
    :param hours:
    :return:
    '''
    end_date=target_date
    start_date = end_date + timedelta(hours=-hours)
    if hours<0:
        end_date=start_date
    # if hours>0:
    #     start_date=end_date+timedelta(hours=-hours)
    # else:
    #     start_date=end_date
    return start_date,end_date

def getMonthDateList(target_date):
    '''
        根据传入的日期获取该月份的全部时间列表
    :param target_date:
    :return:
    '''
    date_list=[]
    first_day,last_day= getMonthDateRang(target_date)
    a_day=timedelta(days=1)
    while first_day<last_day:
        date_list.append(first_day)
        first_day+=a_day

    return date_list

# def local2Utc(target_date,kind='history'):
#     '''
#         将本地时间改为世界时
#     :param target_date:
#     :return:
#     '''
#     # 传入的可能是str也可能是date类型
#     if isinstance(target_date,str):
#         # 转成date
#         if
#         target_date=datetime.strptime(target_date, '%Y-%m-%d')
#     # 本地时间-8为世界时
#     target_date=target_date + timedelta(hours=-8)
#     return target_date.strftime('%Y-%m-%d')

def local2Utc(target_date):
    '''
        将本地时间改为世界时
    :param target_date:
    :return:
    '''

    # 本地时间-8为世界时
    target_date=target_date + timedelta(hours=-8)
    return target_date
