import datetime,time,sys
h = [[1,2,3],[6,7,8,9,10,11,12,13,14,27,28,29],[],[2,3,4,5],[],[9,10,11,12],[],[],[15,16,17,18],[9,10,11],[],[]]
def judgeTime(year, mon, day):
    '''
    day = #time.strftime('%A')                
    date = #int(time.strftime('%d'))
    mon = #int(time.strftime('%m'))
    '''
    s = len(h[mon])
    if s !=0 :
        for i in range(0,s):
            if date == h[mon][s]:        
                return True
            else:   
                if day == 'Saturday' or day == 'Sunday' :
                    return True 
                else :  
                    return False
    else :
        if day == 'Saturday' or day == 'Sunday' :
            return True
        else :
            return False

def getTime(year, mon, day) :
    time=datetime.datetime(year, mon,day)
    return judgeTime(year, mon, time.strftime('%A'))
print getTime(int(sys.argv[1]), int(sys.argv[2]),int(sys.argv[3]))
 
