#!/usr/bin/env python
import json, logging, pprint
from datetime import datetime
#from time import gmtime, strftime
#logging.basicConfig(level=logging.INFO)
class search(object) :
    path='./data/json/'
    vdid=[[
    ['nfbVD-5N-0.178',25.034765,121.624969],
    ['nfbVD-5N-0.706',25.033037,121.629848],
    ['nfbVD-5N-SDT-1.068',25.031313,121.632890],
    ['nfbVD-5N-SDT-1.435',25.029135,121.635628],
    ['nfbVD-5N-SDT-1.788',25.026701,121.637856],
    ['nfbVD-5N-SDT-2.068',25.024556,121.639312],
    ['nfbVD-5N-SDT-2.455',25.021365,121.640838],
    ['nfbVD-5N-SDT-2.849',25.017962,121.641938],
    ['nfbVD-5N-SDT-3.198',25.014950,121.642900],
    ['nfbVD-5N-SDIC-I-4.044',25.008579,121.647313],
    ['nfbVD-5N-4.058',25.008483,121.647401],
    ['nfbVD-5N-4.400',25.006083,121.649516],
    ['nfbVD-5N-SDIC-O-4.455',25.005648,121.649774],
    ['nfbVD-5N-4.460',25.005609,121.649798],
    ['nfbVD-5N-5.523',24.996261,121.651843],
    ['nfbVD-5N-5.883',24.993189,121.652870],
    ['nfbVD-5N-6.413',24.990042,121.656705],
    ['nfbVD-5N-7.113',24.984858,121.660383],
    ['nfbVD-5N-7.636',24.981998,121.664122],
    ['nfbVD-5N-8.043',24.982214,121.668142],
    ['nfbVD-5N-8.703',24.980075,121.674098],
    ['nfbVD-5N-9.013',24.978000,121.676137],
    ['nfbVD-5N-PST-9.373',24.975027,121.677519],
    ['nfbVD-5N-PST-9.840',24.971599,121.680118],
    ['nfbVD-5N-PST-10.147',24.969717,121.682356],
    ['nfbVD-5N-PST-10.506',24.967115,121.684432],
    ['nfbVD-5N-PST-P-10.866',24.964082,121.685648],
    ['nfbVD-5N-PST-11.178',24.961319,121.686176],
    ['nfbVD-5N-PST-11.555',24.958107,121.687341],
    ['nfbVD-5N-PST-P-11.896',24.955492,121.689083],
    ['nfbVD-5N-PST-12.238',24.953256,121.691405],
    ['nfbVD-5N-PST-12.579',24.951525,121.694185],
    ['nfbVD-5N-PST-12.922',24.950362,121.697327],
    ['nfbVD-5N-13.348',24.949439,121.701427],
    ['nfbVD-5N-13.763',24.947618,121.704993],
    ['nfbVD-5N-14.550',24.943688,121.711261],
    ['nfbVD-5N-PLIC-I-14.583',24.943434,121.711429],
    ['nfbVD-5N-PLIC-O-14.683',24.942656,121.711939],
    ['nfbVD-5N-14.800',24.941915,121.712416],
    ['nfbVD-5N-SST-15.488',24.936679,121.716143],
    ['nfbVD-5N-SST-15.855',24.934274,121.718817],
    ['nfbVD-5N-SST-16.196',24.931885,121.720898],
    ['nfbVD-5N-SST-16.570',24.929051,121.722746],
    ['nfbVD-5N-SST-P-16.900',24.926308,121.724511],
    ['nfbVD-5N-SST-17.268',24.923683,121.726324],
    ['nfbVD-5N-SST-17.608',24.921138,121.728347],
    ['nfbVD-5N-SST-17.998',24.918539,121.730764],
    ['nfbVD-5N-SST-P-18.313',24.916468,121.732975],
    ['nfbVD-5N-SST-18.662',24.914383,121.735521],
    ['nfbVD-5N-SST-19.012',24.912333,121.738156],
    ['nfbVD-5N-SST-19.361',24.910308,121.740811],
    ['nfbVD-5N-SST-P-19.689',24.908256,121.743479],
    ['nfbVD-5N-SST-20.062',24.906243,121.746111],
    ['nfbVD-5N-SST-20.412',24.904203,121.748756],
    ['nfbVD-5N-SST-20.752',24.902122,121.751368],
    ['nfbVD-5N-SST-P-21.055',24.900195,121.753505],
    ['nfbVD-5N-SST-21.444',24.897490,121.756101],
    ['nfbVD-5N-SST-21.808',24.894968,121.758209],
    ['nfbVD-5N-SST-22.158',24.892320,121.760102],
    ['nfbVD-5N-SST-P-22.510',24.889627,121.761968],
    ['nfbVD-5N-SST-22.859',24.890018,121.761695],
    ['nfbVD-5N-SST-23.209',24.884310,121.765632],
    ['nfbVD-5N-SST-23.568',24.882921,121.766586],
    ['nfbVD-5N-SST-P-23.911',24.879155,121.769600],
    ['nfbVD-5N-SST-24.264',24.876805,121.771824],
    ['nfbVD-5N-SST-24.677',24.874088,121.774682],
    ['nfbVD-5N-SST-24.952',24.872265,121.776635],
    ['nfbVD-5N-SST-P-25.310',24.869990,121.779070],
    ['nfbVD-5N-SST-25.652',24.867745,121.781460],
    ['nfbVD-5N-SST-26.007',24.865470,121.783859,],
    ['nfbVD-5N-SST-26.300',24.863514,121.785788,],
    ['nfbVD-5N-SST-P-26.705',24.860466,121.788180,],
    ['nfbVD-5N-SST-27.056',24.857648,121.789748,],
    ['nfbVD-5N-SST-27.468',24.854268,121.790975,],
    ['nfbVD-5N-SST-27.779',24.851519,121.791495,],
    ['nfbVD-5N-28.420',24.846058,121.790591,],
    ['nfbVD-5N-TCIC-I-29.843',24.833456,121.790577,],
    ['nfbVD-5N-30.100',24.829461,121.790256]],[
    ['nfbVD-5S-SDT-1.072',25.031001,121.632782],
    ['nfbVD-5S-SDT-1.424',25.028917,121.635409],
    ['nfbVD-5S-SDT-1.766',25.026551,121.637569],
    ['nfbVD-5S-SDT-2.050',25.024378,121.639051],
    ['nfbVD-5S-SDT-2.433',25.021212,121.640538],
    ['nfbVD-5S-SDT-2.835',25.017742,121.641654],
    ['nfbVD-5S-SDT-3.178',25.014782,121.642614],
    ['nfbVD-5S-3.506',25.012078,121.643860],
    ['nfbVD-5S-SDIC-O-3.806',25.009963,121.645706],
    ['nfbVD-5S-4.016',25.008546,121.647092],
    ['nfbVD-5S-SDIC-I-4.178',25.007460,121.648161],
    ['nfbVD-5S-4.395',25.005930,121.649487],
    ['nfbVD-5S-4.749',25.002917,121.650544],
    ['nfbVD-5S-5.523',24.996041,121.651755],
    ['nfbVD-5S-6.498',24.989473,121.657439],
    ['nfbVD-5S-7.113',24.984658,121.660352],
    ['nfbVD-5S-7.553',24.981894,121.663244],
    ['nfbVD-5S-7.923',24.981824,121.666871],
    ['nfbVD-5S-8.669',24.979970,121.673758],
    ['nfbVD-5S-9.063',24.977273,121.676223],
    ['nfbVD-5S-PST-9.326',24.975075,121.677170],
    ['nfbVD-5S-PST-9.840',24.971273,121.679972],
    ['nfbVD-5S-PST-10.145',24.969381,121.682158],
    ['nfbVD-5S-PST-10.495',24.966802,121.684122],
    ['nfbVD-5S-PST-P-10.845',24.963827,121.685221],
    ['nfbVD-5S-PST-11.158',24.961053,121.685762],
    ['nfbVD-5S-PST-11.545',24.957768,121.686969],
    ['nfbVD-5S-PST-P-11.895',24.955080,121.688767],
    ['nfbVD-5S-PST-12.245',24.952836,121.691192],
    ['nfbVD-5S-PST-12.595',24.951094,121.694073],
    ['nfbVD-5S-PST-12.945',24.949984,121.697318],
    ['nfbVD-5S-13.343',24.949217,121.701170],
    ['nfbVD-5S-14.356',24.944926,121.709949],
    ['nfbVD-5S-PLIC-O-14.483',24.944039,121.710739],
    ['nfbVD-5S-14.540',24.942770,121.711547],
    ['nfbVD-5S-PLIC-I-14.691',24.942414,121.711763],
    ['nfbVD-5S-15.139',24.938899,121.713917],
    ['nfbVD-5S-SST-15.478',24.936405,121.715845],
    ['nfbVD-5S-SST-15.856',24.933963,121.718451],
    ['nfbVD-5S-SST-16.201',24.931562,121.720377],
    ['nfbVD-5S-SST-16.551',24.928745,121.722226],
    ['nfbVD-5S-SST-P-16.902',24.926051,121.723991],
    ['nfbVD-5S-SST-17.253',24.923365,121.725858],
    ['nfbVD-5S-SST-17.608',24.920805,121.727900],
    ['nfbVD-5S-SST-17.990',24.918177,121.730334],
    ['nfbVD-5S-SST-P-18.312',24.916115,121.732539],
    ['nfbVD-5S-SST-18.663',24.913981,121.735134],
    ['nfbVD-5S-SST-19.013',24.912058,121.737623],
    ['nfbVD-5S-SST-19.363',24.909911,121.740424],
    ['nfbVD-5S-SST-P-19.677',24.907883,121.743059],
    ['nfbVD-5S-SST-20.063',24.905845,121.745729],
    ['nfbVD-5S-SST-20.413',24.903811,121.748374],
    ['nfbVD-5S-SST-20.763',24.901739,121.750969],
    ['nfbVD-5S-SST-P-21.063',24.899855,121.753056],
    ['nfbVD-5S-SST-21.460',24.897148,121.755667],
    ['nfbVD-5S-SST-21.807',24.894641,121.757733],
    ['nfbVD-5S-SST-22.159',24.892018,121.759632],
    ['nfbVD-5S-SST-P-22.506',24.889363,121.761456],
    ['nfbVD-5S-SST-22.859',24.886678,121.763306],
    ['nfbVD-5S-SST-23.207',24.883955,121.765184],
    ['nfbVD-5S-SST-23.560',24.881371,121.767043],
    ['nfbVD-5S-SST-P-23.910',24.878842,121.769115],
    ['nfbVD-5S-SST-24.264',24.876437,121.771408],
    ['nfbVD-5S-SST-24.678',24.873758,121.774249],
    ['nfbVD-5S-SST-24.962',24.871892,121.776219],
    ['nfbVD-5S-SST-P-25.312',24.869650,121.778621],
    ['nfbVD-5S-SST-25.664',24.867362,121.781039],
    ['nfbVD-5S-SST-26.013',24.865087,121.783434],
    ['nfbVD-5S-SST-26.299',24.863174,121.785337],
    ['nfbVD-5S-SST-P-26.706',24.860211,121.787661],
    ['nfbVD-5S-SST-27.054',24.857413,121.789209],
    ['nfbVD-5S-SST-27.442',24.854091,121.790431],
    ['nfbVD-5S-SST-27.748',24.851413,121.790962],
    ['nfbVD-5S-SST-28.236',24.846997,121.790618],
    ['nfbVD-5S-TCIC-O-29.716',24.834020,121.790258],
    ['nfbVD-5S-30.140',24.830951,121.790402],
    ['nfbVD-5S-30.266',24.829347,121.790108],
    ['nfbVD-5S-TCIC-I-30.249',24.829199,121.790068]]]

    @staticmethod
    def getSpeed(model='json') :
        m=search.getLastJson()
        out=[]
        for i in range(0,2) :
            for j in range(0,78) :
                a=m[i][j]
                s=0
                n=0
                for k in range(0,len(a)) :
                    s=s+a[k][0]*a[k][1]
                    n=n+a[k][1]
                if n==0 :
                    if model=='handle' and j!=0 :
                        speed=out[j-1]
                    else :
                        speed=-1
                else :
                    speed=s/n
                if model=='json' :
                    b=search.vdid[i][j]
                    out.append({'name' : b[0], 'addr' : [str(b[1]),str(b[2])], 'speed' : speed})
                else :
                    out.append(speed)
        return out

    @staticmethod
    def getLastJson() :
        [y,m,d,h,i]=search.getNow()
        logging.info('Now: %s-%s-%s %s:%s', y, m, d, h, i)
        return search.getPreviousJson(y,m,d,h,i)

    @staticmethod
    def getPreviousJson(year, mon, day, hour, mine) :
        success=True
        while success :
            js=search.getJson(year, mon, day, hour, mine)
            if js==None :
                [year, mon, day, hour, mine]=search.getPreviousTime(year, mon, day, hour, mine)
            else :
                logging.info('Get: %s-%s-%s %s:%s', year, mon, day, hour, mine)
                return js
        return None

    @staticmethod
    def getPreviousTime(year, mon, day, hour, mine) :
        mine=mine-1
        return search.getStandardTime(year, mon, day, hour, mine)

    @staticmethod
    def getStandardTime(year, mon, day, hour, mine) :
        if mine<0 :
            return search.getStandardTime(year, mon, day, hour-1, 59)
        if hour<0 :
            return search.getStandardTime(year, mon, day-1, 23, mine)
        if day<1 :
            m=[31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if search.isLeaP(year) :
                m[2]=29
            return search.getStandardTime(year, mon-1, m[mon-1], hour, mine)
        if mon<1 :
            return search.getStandardTime(year-1, 12, day, hour, mine)
        return [year, mon, day, hour, mine]

    @staticmethod
    def isLeaP(year) :
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    @staticmethod
    def getNow() :
        '''
        year=int(strftime('%Y', gmtime()))
        mon=int(strftime('%m', gmtime()))
        day=int(strftime('%d', gmtime()))
        hour=int(strftime('%H', gmtime()))
        mine=int(strftime('%M', gmtime()))
        print strftime("%Y-%m-%d %H:%M:%S", gmtime())
        '''
        t=datetime.now()
        year=int(t.strftime('%Y'))
        mon=int(t.strftime('%m'))
        day=int(t.strftime('%d'))
        hour=int(t.strftime('%H'))
        mine=int(t.strftime('%M'))
        return [year, mon, day, hour, mine]

    @staticmethod
    def checkJson(read) :
        l=[[2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],[2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 3, 2, 3, 3, 2, 3, 3, 3, 2, 2, 2, 2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2]]
        if len(read)!=2 :
            return False
        for i in range(2) :
            if len(read[i])!=len(l[i]) :
                return False
            for j in range(len(l[i])) :
                if len(read[i][j])!=l[i][j] :
                    return False
                for k in range(l[i][j]) :
                    if len(read[i][j][k])!=2 :
                        return False
        if len(read[0])!=78 :
            return False
        if len(read[1])!=78 :
            return False
        return True

    @staticmethod
    def getJson(year, mon, day, hour, mine) :
        path=search.getPath(year, mon, day, hour, mine)
        try :
            f=open(path)
            js=json.load(f)
            if search.checkJson(js) :
                return js
        except :
            logging.info('Not Exist: %s', path)
        return None
    @staticmethod
    def getPath(year, mon, day, hour, mine) :
        m=str(year)+'_'+search.padded(mon)
        d=m+'_'+search.padded(day)
        f=d+'-'+search.padded(hour)+'_'+search.padded(mine)+'_00.json'
        return search.path+m+'/'+d+'/'+f

    @staticmethod
    def padded(n) :
        n=int(n)
        if n<10 :
            return '0'+str(n)
        return str(n)

if __name__=='__main__' :
    pp = pprint.PrettyPrinter(indent=4);
    read=search.getLastJson()
    pp.pprint(read)
    logging.debug('OVER')
    #print search.getPreviousTime(2012, 3, 1, 0, 0)
    #print read
