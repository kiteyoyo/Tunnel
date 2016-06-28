# -*- coding: utf8 -*-
# coding=Big5
import datetime,time,pprint,logging,json,sys
from search import search

class preTime(object) :
    x = [30.1,29.843,28.42,27.779,27.468,27.056,26.705,26.3,26.007,25.652,25.31,24.952,24.677,24.264,23.911,23.568,23.209,22.859,22.51,22.158,21.808,21.444,21.055,20.752,20.412,20.062,19.689,19.361,19.012,18.662,18.313,17.998,17.608,17.268,16.9,16.57,16.196,15.855,15.488,14.8,14.683,14.583,14.55,13.763,13.348,12.922,12.579,12.238,11.896,11.555,11.178,10.866,10.506,10.147,9.84,9.373,9.013,8.703,8.043,7.636,7.113,6.413,5.883,5.523,4.46,4.455,4.4,4.058,4.044,3.198,2.849,2.455,2.068,1.788,1.435,1.068,0.706,0.178]
   
    y = [1.072,1.424,1.766,2.05,2.433,2.835,3.178,3.506,3.806,4.016,4.178,4.395,4.749,5.523,6.498,7.113,7.553,7.923,8.669,9.063,9.326,9.84,10.145,10.495,10.845,11.158,11.545,11.895,12.245,12.595,12.945,13.343,14.356,14.483,14.54,14.691,15.139,15.478,15.856,16.201,16.551,16.902,17.253,17.608,17.99,18.312,18.663,19.013,19.363,19.677,20.063,20.413,20.763,21.063,21.46,21.807,22.159,22.506,22.859,23.207,23.56,23.91,24.264,24.678,24.962,25.312,25.664,26.013,26.299,26.706,27.054,27.442,27.748,28.236,29.716,30.14,30.249,30.266]
 

    @staticmethod    
    def judgeRoad(s,e,jam):
        if s == '頭城' and e == '坪林' :#north 
            a = preTime.preTime1(0,0,jam)
            tmp = preTime.nowTime1(0,0)
            speed = preTime.handleSpeed1()
            return [a[0],tmp[0],speed]
        elif s == '坪林' and e == '石碇' :
            a = preTime.preTime1(1,0,jam)   
            tmp = preTime.nowTime1(1,0)
            speed = preTime.handleSpeed1()
            return [a[0],tmp[0],speed]
        elif s == '石碇' and e == '南港':
            a = preTime.preTime1(2,0,jam)
            tmp = preTime.nowTime1(2,0)
            speed = preTime.handleSpeed1()
            return [a[0],tmp[0],speed]
        elif s == '頭城' and e == '石碇':
            a = preTime.preTime1(0,0,jam)   
            a[0] = a[0] + (preTime.x[41]-preTime.x[42])/a[1]
            a1 = preTime.preTime1(1,a[0],jam,a[2])
            a[2].extend(a1[2])

            tmp = preTime.nowTime1(0,0)   
            tmp[0] = tmp[0] + (preTime.x[41]-preTime.x[42])/tmp[1]
            tmp = preTime.nowTime1(1,tmp[0])
            speed = preTime.handleSpeed1()
            return [a1[0],tmp[0],speed]
        elif s == '坪林' and e == '南港':
            a = preTime.preTime1(1,0,jam)
            a[0] = a[0] + (preTime.x[66]-preTime.x[67])/a[1]
            a1 = preTime.preTime1(2,a[0],jam,a[2])
            a[2].extend(a1[2])

            tmp = preTime.nowTime1(1,0)
            tmp[0] = tmp[0] + (preTime.x[66]-preTime.x[67])/tmp[1]
            tmp = preTime.nowTime1(2,tmp[0])
            speed = preTime.handleSpeed1()
            return [a1[0],tmp[0],speed]
        elif s == '頭城' and e == '南港':
            a = preTime.preTime1(0,0,jam)
            a[0] = a[0] + (preTime.x[41]-preTime.x[42])/a[1]
            a1 = preTime.preTime1(1,a[0],jam,a[2])
            a1[0] = a1[0] + (preTime.x[66]-preTime.x[67])/a1[1]
            a2 = preTime.preTime1(2,a1[0],jam,a1[2])
            a[2].extend(a1[2])
            a[2].extend(a2[2])

            tmp = preTime.nowTime1(0,0)
            tmp[0] = tmp[0] + (preTime.x[41]-preTime.x[42])/tmp[1]
            tmp = preTime.nowTime1(1,tmp[0])
            tmp[0] = tmp[0] + (preTime.x[66]-preTime.x[67])/tmp[1]
            tmp = preTime.nowTime1(2,tmp[0])
            speed = preTime.handleSpeed1()
            return [a2[0],tmp[0],speed]
        elif s == '南港' and e == '石碇' :#south
            a = preTime.preTime2(0,0,jam) 
            tmp = preTime.nowTime2(0,0) 
            speed = preTime.handleSpeed2()
            return [a[0],tmp[0],speed]
        elif s == '石碇' and e == '坪林' :
            a = preTime.preTime2(1,0,jam)   
            tmp = preTime.nowTime2(1,0) 
            speed = preTime.handleSpeed2()
            return [a[0],tmp[0],speed]
        elif s == '坪林' and e == '頭城':
            a = preTime.preTime2(2,0,jam)
            tmp = preTime.nowTime2(2,0) 
            speed = preTime.handleSpeed2()
            return [a[0],tmp[0],speed]
        elif s == '南港' and e == '坪林':
            a = preTime.preTime2(0,0,jam)
            a[0] = a[0] + (preTime.y[11]-preTime.y[8])/a[1]
            a1 = preTime.preTime1(1,a[0],jam,a[2])
            a[2].extend(a1[2])

            tmp = preTime.nowTime2(0,0)
            tmp[0] = tmp[0] + (preTime.y[11]-preTime.y[8])/tmp[1]
            tmp = preTime.nowTime1(1,tmp[0])
            speed = preTime.handleSpeed2()
            return [a1[0],tmp[0],speed]
        elif s == '石碇' and e == '頭城':
            a = preTime.preTime2(1,0,jam)
            a[0] = a[0] + (preTime.y[36]-preTime.y[34])/a[1]
            a1 = preTime.preTime2(2,a[0],jam,a[2])
            a[2].extend(a1[2])

            tmp = preTime.nowTime2(1,0)
            tmp[0] = tmp[0] + (preTime.y[36]-preTime.y[34])/tmp[1]
            tmp = preTime.nowTime2(2,tmp[0])
            speed = preTime.handleSpeed2()
            return [a1[0],tmp[0],speed]
        elif s == '南港' and e == '頭城':
            a = preTime.preTime2(0,0,jam)
            a[0] = a[0] + (preTime.y[11]-preTime.y[8])/a[1]
            a1 = preTime.preTime1(1,a[0],jam,a[2])
            a1[0] = a1[0] + (preTime.y[36]-preTime.y[34])/a1[1]
            a2 = preTime.preTime2(2,a1[0],jam,a1[2])
            a[2].extend(a1[2])
            a[2].extend(a2[2])

            tmp = preTime.nowTime2(0,0)
            tmp[0] = tmp[0] + (preTime.y[11]-preTime.y[8])/tmp[1]
            tmp = preTime.nowTime1(1,tmp[0])
            tmp[0] = tmp[0] + (preTime.y[36]-preTime.y[34])/tmp[1]
            tmp = preTime.nowTime2(2,tmp[0])
            speed = preTime.handleSpeed2()
            return [a2[0],tmp[0],speed]
        else:
            print 'Error !'
        
    @staticmethod 
    def preTime1(j,t,jam,vl=[]): #jam == 0 is trafficjam
        a = [[-1.4227,-1.0201,-7.4135],[0.077,-0.4037,-7.0387]]
        b = [[0.0061,0.0071,0.0189],[-0.0162,-0.0041,-0.0068]]
        c = [[90.8322,89.5241,82.5084],[87.7284,93.0937,96.9126]]
        s = [1,42,67]
        e = [42,67,77]
        for i in range(s[j],e[j]) :
            s =  preTime.x[i] - preTime.x[i+1]
            mid_x = ( preTime.x[i] + preTime.x[i+1] )/2
            v = a[jam][j]*mid_x + b[jam][j]*t + c[jam][j]
            t = t + s/v*60
            vl.append(v)
        return [t , v, vl]

    @staticmethod
    def preTime2(j,t,jam,vl=[]):   #jam == 0 is traffic jam
        a = [[0.2297,-0.5071,0.0408],[-0.0652,-0.8535,-1.219]]
        b = [[0.0004,0.004,-0.004],[0.0045,0.0033,0.0145]]
        c = [[66.6885,76.9128,69.9834],[83.493,87.9012,80.1414]]
        s = [0,11,36]
        e = [8,34,75]
                
        for i in range(s[j],e[j]) :
            s =  preTime.y[i+1] - preTime.y[i] 
            mid_x = ( preTime.y[i] + preTime.y[i+1] )/2  
            v = a[jam][j]*mid_x + b[jam][j]*t + c[jam][j]  
            t = t + s/v*60      
        return [t , v , vl ] 
    
    @staticmethod
    def handleSpeed1():#north
        n=[]
        m = search.getLastJson()
        for i in range(0,78):
            amount = 0 
            speed = 0
            for j in range(0,len(m[0][i])):
                amount = amount + m[0][i][j][1]
                speed = speed +  m[0][i][j][0]*m[0][i][j][1]
            if amount==0 :
                n.append(0)
            else :
                n.append( speed/amount ) 
        return n 

    @staticmethod
    def handleSpeed2(): #south
        n=[]
        m = search.getLastJson()
        for i in range(0,78):
            amount = 0 
            speed = 0
            for j in range(0,len(m[1][i])):
                amount = amount + m[1][i][j][1]
                speed = speed +  m[1][i][j][0]*m[1][i][j][1]
            if amount==0 :
                n.append(0)
            else :
                n.append( speed/amount )
        return n


    @staticmethod 
    def nowTime1(j,t): #to compute time by using immediate speed  
        speed = preTime.handleSpeed1()
        s = [1,42,67]
        e = [42,67,77]
        for i in range(s[j],e[j]) :
            s =  preTime.x[i] - preTime.x[i+1]
            mid_x = ( preTime.x[i] + preTime.x[i+1] )/2
            if speed[i] == 0 :
                t = t + s/80*60
            else:
                t = t + s/speed[i]*60
       
        if  speed[e[j]] == 0 :      
            return [ t , 80 ]
        else :
            return [t ,speed[e[j]]]


    @staticmethod
    def nowTime2(j,t):
        speed = preTime.handleSpeed2()
        s = [0,11,36]
        e = [8,34,75]
        for i in range(s[j],e[j]) :
            s =  preTime.y[i+1] - preTime.y[i] 
            mid_x = ( preTime.y[i] + preTime.y[i+1] )/2  
            if speed[i] == 0 :
                t = t + s/80*60
            else:
                t = t + s/speed[i]*60      
        if  speed[e[j]] == 0 :      
            return [ t , 80 ]
        else :
            return [t ,speed[e[j]]]
if __name__ == '__main__':
    #s = raw_input("Start: ")
    #e = raw_input("End: ")
    jam = 0 #Is it traffic jam ? 0 is true , 1 is false
    argv = sys.argv  
    h = preTime.judgeRoad(argv[1],argv[2],jam)
    print '[迴歸線的時間,即時速度的時間,即時速度]'
    
    print h 
