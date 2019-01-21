
class BBXDetailMidInfo:
    '''
        指定海区以及船舶集合
    '''
    def __init__(self,area,bbxlist):
        self.area=area
        self.bbxlist=bbxlist

class BBXStateDetailMidInfo:
    '''
        船舶状态详细中间mid
    '''
    def __init__(self,area,bid,code,stateDetailList):
        self.bid=bid
        self.code=code
        self.area=area
        self.stateDetailList=stateDetailList
        # self.state=state
        # self.count=count

class BBXMaxDateMidInfo:
    '''
        船舶最近时间model
    '''
    def __init__(self,dict):
        self.bid=dict['bid_id']
        self.code=dict['code']
        self.area=dict['bid__area']
        self.lastDateTime=dict['nowdate__max']

class StateDetailMidInfo:
    '''
        不同状态以及接收到的个数
    '''
    def __init__(self,state,count):
        self.state=state
        self.count=count



class AreaStatisticMidInfo:
    def __init__(self,area,static):
        self.area=area
        self.static=static

class StatisticMidInfo:
    def __init__(self,state,count,list):
        self.state=state
        self.count=count
        self.list=list

class BBXTrackMidInfo:
    def __init__(self,code,bid,latlngs):
        self.code=code
        self.bid=bid
        self.latlngs=latlngs

class RealtimeMidInfo:
    def __init__(self,timestamp,val):
        self.timestamp=timestamp
        self.val=val