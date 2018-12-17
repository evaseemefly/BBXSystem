
class GPSData:
    def __init__(self,geometry,properties,bbox):
        # self.coordinates=coordinates
        # self.times=times
        self.type="Feature"
        self.geometry=geometry
        self.properties=properties
        self.bbox=bbox

class Geometry:
    def __init__(self,coordinates):
        '''

        :param coordinates:
        array of [lng,lat] coordinates
        '''
        self.type="MultiPoint"

        self.coordinates=coordinates

class Property:
    def __init__(self,times):
        self.time=times

class BBXTrack:
    '''
        船舶行驶轨迹
    '''
    def __init__(self,bsid,code,starttime,endtime,latlngs,speeds):
        '''
            船舶轨迹model
        :param bsid: 船舶id
        :param code: 船舶呼号
        :param starttime: 起始时间
        :param endtime: 终止时间
        :param latlngs: 经纬度数组
        :param seepds: 速度数组
        '''
        self.bsid=bsid
        self.code=code
        self.starttime=starttime
        self.endtime=endtime
        self.latlngs=latlngs
        self.speeds=speeds
