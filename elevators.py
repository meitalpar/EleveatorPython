class elevator:
    Time = 0
    flag = 0 ;
    #UP = 1
    #DOWN = -1

    def __init__(self, d: dict):
        self.id = d.get("_id")
        self.speed= d.get("_speed")
        self.minfloor=d.get("_minFloor")
        self.maxfloor=d.get("_maxFloor")
        self.closetime=d.get("_closeTime")
        self.opentime= d.get("_openTime")
        self.starttime=d.get("_startTime")
        self.stoptime=d.get("_stopTime")



    def time(self,src,des):
        df=des-src
       # print(df)
        return (self.closetime + self.starttime + df/self.speed + self.stoptime + self.opentime)
