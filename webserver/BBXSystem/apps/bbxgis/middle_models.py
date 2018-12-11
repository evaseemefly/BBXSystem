
class GPSData:
    def __init__(self,geometry,properties):
        # self.coordinates=coordinates
        # self.times=times
        self.type="Feature"
        self.geometry=geometry
        self.properties=properties

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
