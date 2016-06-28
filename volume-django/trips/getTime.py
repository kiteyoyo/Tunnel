# -*- coding: utf8 -*-
# coding=Big5
import time,pprint,logging,json,sys
from datetime import datetime
from search import search
#logging.basicConfig(level=logging.DEBUG)
class basic(object):
    x = [30.1,29.843,28.42,27.779,27.468,27.056,26.705,26.3,26.007,25.652,25.31,24.952,24.677,24.264,23.911,23.568,23.209,22.859,22.51,22.158,21.808,21.444,21.055,20.752,20.412,20.062,19.689,19.361,19.012,18.662,18.313,17.998,17.608,17.268,16.9,16.57,16.196,15.855,15.488,14.8,14.683,14.583,14.55,13.763,13.348,12.922,12.579,12.238,11.896,11.555,11.178,10.866,10.506,10.147,9.84,9.373,9.013,8.703,8.043,7.636,7.113,6.413,5.883,5.523,4.46,4.455,4.4,4.058,4.044,3.198,2.849,2.455,2.068,1.788,1.435,1.068,0.706,0.178,0]
    y = [0,1.072,1.424,1.766,2.05,2.433,2.835,3.178,3.506,3.806,4.016,4.178,4.395,4.749,5.523,6.498,7.113,7.553,7.923,8.669,9.063,9.326,9.84,10.145,10.495,10.845,11.158,11.545,11.895,12.245,12.595,12.945,13.343,14.356,14.483,14.54,14.691,15.139,15.478,15.856,16.201,16.551,16.902,17.253,17.608,17.99,18.312,18.663,19.013,19.363,19.677,20.063,20.413,20.763,21.063,21.46,21.807,22.159,22.506,22.859,23.207,23.56,23.91,24.264,24.678,24.962,25.312,25.664,26.013,26.299,26.706,27.054,27.442,27.748,28.236,29.716,30.14,30.249,30.266]
    @staticmethod
    def change(n) :
        if n=='南港' :
            return '南港'
        elif n=='石碇' :
            return '石碇'
        elif n=='坪林' :
            return '坪林'
        elif n=='頭城' :
            return '頭城'

    @staticmethod
    def get_road(s,e) :
        s=getTime.change(s)
        e=getTime.change(e)
        tree={ '南港': {
                    '石碇' : [0, 9, False],
                    '坪林' : [12, 35, False],
                    '頭城' : [0, 76, False]
                },
                '石碇' : {
                    '南港' :[70, 78, True],
                    '坪林' :[12, 35, False],
                    '頭城' :[12, 76, False],
                },
                '坪林' : {
                    '南港' :[12, 76, True],
                    '石碇' :[42, 67, True],
                    '頭城' :[37 ,76, False],
                },
                '頭城' : {
                    '南港' :[0, 76, True],
                    '石碇' :[0, 35, True],
                    '坪林' :[0, 41, True],
                }
            }
        return tree.get(s).get(e)
'''
        if s == '南港' and e == '石碇':
            start = 0  
            end = 9
            isN = False
        elif s == '石碇' and e == '坪林':
            start = 12 
            end = 35
            isN = False
        elif s == '坪林' and e == '頭城':
            start = 37
            end = 76
            isN = False
        elif s == '南港' and e == '坪林':
            start = 0
            end = 35
            isN = False
        elif s == '石碇' and e == '頭城':
            start = 12
            end = 76
            isN = False
        elif s == '南港' and e == '頭城':
            start = 0
            end = 76
            isN = False
        elif s == '頭城' and e == '坪林': 
            start = 0
            end = 41
            isN = True
        elif s == '坪林' and e == '石碇':
            start = 42 
            end = 67
            isN = True
        elif s == '石碇' and e == '南港': 
            start = 70
            end = 79
            isN = True
        elif s == '頭城' and e == '石碇':
            start = 0
            end = 35
            isN = True
        elif s == '坪林' and e == '南港': 
            start = 12
            end = 76
            isN = True
        elif s == '頭城' and e == '南港':
            start = 0
            end = 76
            isN = True  
        return [start, end, isN]
'''
class getTime(basic) :
    @staticmethod
    def inputTime(minute): #輸入小時，分 判斷要用哪一個時間點的速度
        m = minute
        i = int(m/5)
        return i 
    
    @staticmethod #get file function 
    def getFile(isN) :
        path='/usr/src/app/trips/data/prediction/'
        if isN :
            path=path+'FinalNorthVel.json'
        else :
            path=path+'FinalSouthVel.json'
        try :
            f=open(path)
            j=json.load(f)
            return j
        except :
            logging.error("Can't read file "+path)                                                                                    
    @staticmethod
    def compute(s,e,time):
        road = getTime.get_road(s,e)
        isN=road[2]
        vl = []
        j = getTime.getFile(isN) 

        start_time = time
        if isN :
            d1 = getTime.x
            for i in range(1,40):
                tmp = j[i]
                j[i] = j[79-i] 
                j[79-i] = tmp
        else :
            d1 = getTime.y
        j = j[1:]
        logging.debug('s: %d, e: %d',road[0], road[1])
        logging.debug(j)
        for i in range(road[0],road[1]):
            n = getTime.inputTime(time)
            d = abs(d1[i] - d1[i+1]) 
            logging.debug('n: %d', n)
            v = j[i][n] 
            time = time + d/v*60
            vl.append(v)
        return  [time - start_time ,vl]

    @staticmethod
    def getPreduction(s, e, time=0) :
        time=int(time)
        ti=datetime.now()
        hour=int(ti.strftime('%H'))
        mine=int(ti.strftime('%M'))
        t=hour*24+mine
        if t!=0 :
            t=t+time
        t=t%1440
        return getTime.compute(s, e, t)

    @staticmethod
    def getPreductionAll(isN, time=0) :
        if isN :
            return getTime.getPreduction('頭城', '南港', time)
        else :
            return getTime.getPreduction('南港', '頭城', time)

    @staticmethod
    def getPreductionMore(s,e,t) :
        o=[]
        for i in t :
            o.append(getTime.getPreduction(s,e,i)[0])
        return  o

class immedite(basic):
    @staticmethod
    def handleSpeed(isN):
        if isN :
            k=0
        else :
            k=1
        n=[]
        m = search.getLastJson()
        if m==None :
            return None
        for i in range(0,78):
            amount = 0 
            speed = 0 
            a=m[k][i]
            for j in range(0,len(a)) :
                amount = amount + a[j][1]
                speed = speed +  a[j][0]*a[j][1]
            if amount==0 :
                n.append(0)
            else :
                n.append( speed/amount ) 
        return n

    @staticmethod
    def swap_x():
        for i in range(0,39):        
            tmp = basic.x[i]            
            basic.x[i] = basic.x[78-i]                    
            basic.x[78-i] = tmp    
        return basic.x

    @staticmethod
    def nowTime(s,e): 
        vl = []
        t = 0 
        road = basic.get_road(s,e)
        isN=road[2]
        speed = immedite.handleSpeed(isN)
        if speed==None :
            return getTime.getPreduction(s,e)
        if isN:
            s = immedite.swap_x()
        else:
            s = basic.y
        logging.debug('%r',speed)
        logging.debug('road: %d, %d', road[0],road[1])
        for i in range(road[0],road[1]):
            d = abs( s[i]-s[i+1])
            v= immedite.handle(speed,i, isN)
            print v
            t = t + d/v*60
            vl.append(v)
        return [t, vl] 
    @staticmethod
    def handle(speed, i, isN):
        if isN :
            check=[9, 12, 36, 37, 76]
        else :
            check=[8, 10, 33, 35, 74, 76]
        if speed[i]==0 :
            if i==0 :
                return speed[1]
            else :
                return immedite.handle(speed, i-1, isN)
        elif i in check :
            return speed[i-1]
        return speed[i]

if __name__ == '__main__':

    argv=sys.argv
    ''' 
    h = int( time.strftime('%H'))
    m = int( time.strftime('%M'))
    minute = h*60+m
    print getTime.compute(argv[1],argv[2],minute)
    '''
    r=['南港', '石碇', '坪林', '頭城']
    for s in r :
        for e in r :
            if s!=e :
                a=getTime.getPreduction(s,e)[0]
                print s, '=>', e, 't:', a

   # print immedite.nowTime(argv[1], argv[2])
