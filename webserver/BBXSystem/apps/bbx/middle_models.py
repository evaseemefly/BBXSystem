
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

class StateDetailMidInfo:
    '''
        不同状态以及接收到的个数
    '''
    def __init__(self,state,count):
        self.state=state
        self.count=count

