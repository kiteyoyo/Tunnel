#!/usr/bin/env python
import os, gzip, re, json, time, sys, traceback
from xml.dom import minidom
class Api(object) :
    nvdid=['nfbVD-5N-0.178',
            'nfbVD-5N-0.706',
            'nfbVD-5N-SDT-1.068',
            'nfbVD-5N-SDT-1.435',
            'nfbVD-5N-SDT-1.788',
            'nfbVD-5N-SDT-2.068',
            'nfbVD-5N-SDT-2.455',
            'nfbVD-5N-SDT-2.849',
            'nfbVD-5N-SDT-3.198',
            'nfbVD-5N-SDIC-I-4.044',
            'nfbVD-5N-4.058',
            'nfbVD-5N-4.400',
            'nfbVD-5N-SDIC-O-4.455',
            'nfbVD-5N-4.460',
            'nfbVD-5N-5.523',
            'nfbVD-5N-5.883',
            'nfbVD-5N-6.413',
            'nfbVD-5N-7.113',
            'nfbVD-5N-7.636',
            'nfbVD-5N-8.043',
            'nfbVD-5N-8.703',
            'nfbVD-5N-9.013',
            'nfbVD-5N-PST-9.373',
            'nfbVD-5N-PST-9.840',
            'nfbVD-5N-PST-10.147',
            'nfbVD-5N-PST-10.506',
            'nfbVD-5N-PST-P-10.866',
            'nfbVD-5N-PST-11.178',
            'nfbVD-5N-PST-11.555',
            'nfbVD-5N-PST-P-11.896',
            'nfbVD-5N-PST-12.238',
            'nfbVD-5N-PST-12.579',
            'nfbVD-5N-PST-12.922',
            'nfbVD-5N-13.348',
            'nfbVD-5N-13.763',
            'nfbVD-5N-14.550',
            'nfbVD-5N-PLIC-I-14.583',
            'nfbVD-5N-PLIC-O-14.683',
            'nfbVD-5N-14.800',
            'nfbVD-5N-SST-15.488',
            'nfbVD-5N-SST-15.855',
            'nfbVD-5N-SST-16.196',
            'nfbVD-5N-SST-16.570',
            'nfbVD-5N-SST-P-16.900',
            'nfbVD-5N-SST-17.268',
            'nfbVD-5N-SST-17.608',
            'nfbVD-5N-SST-17.998',
            'nfbVD-5N-SST-P-18.313',
            'nfbVD-5N-SST-18.662',
            'nfbVD-5N-SST-19.012',
            'nfbVD-5N-SST-19.361',
            'nfbVD-5N-SST-P-19.689',
            'nfbVD-5N-SST-20.062',
            'nfbVD-5N-SST-20.412',
            'nfbVD-5N-SST-20.752',
            'nfbVD-5N-SST-P-21.055',
            'nfbVD-5N-SST-21.444',
            'nfbVD-5N-SST-21.808',
            'nfbVD-5N-SST-22.158',
            'nfbVD-5N-SST-P-22.510',
            'nfbVD-5N-SST-22.859',
            'nfbVD-5N-SST-23.209',
            'nfbVD-5N-SST-23.568',
            'nfbVD-5N-SST-P-23.911',
            'nfbVD-5N-SST-24.264',
            'nfbVD-5N-SST-24.677',
            'nfbVD-5N-SST-24.952',
            'nfbVD-5N-SST-P-25.310',
            'nfbVD-5N-SST-25.652',
            'nfbVD-5N-SST-26.007',
            'nfbVD-5N-SST-26.300',
            'nfbVD-5N-SST-P-26.705',
            'nfbVD-5N-SST-27.056',
            'nfbVD-5N-SST-27.468',
            'nfbVD-5N-SST-27.779',
            'nfbVD-5N-28.420',
            'nfbVD-5N-TCIC-I-29.843',
            'nfbVD-5N-30.100']
    svdid=['nfbVD-5S-SDT-1.072',
            'nfbVD-5S-SDT-1.424',
            'nfbVD-5S-SDT-1.766',
            'nfbVD-5S-SDT-2.050',
            'nfbVD-5S-SDT-2.433',
            'nfbVD-5S-SDT-2.835',
            'nfbVD-5S-SDT-3.178',
            'nfbVD-5S-3.506',
            'nfbVD-5S-SDIC-O-3.806',
            'nfbVD-5S-4.016',
            'nfbVD-5S-SDIC-I-4.178',
            'nfbVD-5S-4.395',
            'nfbVD-5S-4.749',
            'nfbVD-5S-5.523',
            'nfbVD-5S-6.498',
            'nfbVD-5S-7.113',
            'nfbVD-5S-7.553',
            'nfbVD-5S-7.923',
            'nfbVD-5S-8.669',
            'nfbVD-5S-9.063',
            'nfbVD-5S-PST-9.326',
            'nfbVD-5S-PST-9.840',
            'nfbVD-5S-PST-10.145',
            'nfbVD-5S-PST-10.495',
            'nfbVD-5S-PST-P-10.845',
            'nfbVD-5S-PST-11.158',
            'nfbVD-5S-PST-11.545',
            'nfbVD-5S-PST-P-11.895',
            'nfbVD-5S-PST-12.245',
            'nfbVD-5S-PST-12.595',
            'nfbVD-5S-PST-12.945',
            'nfbVD-5S-13.343',
            'nfbVD-5S-14.356',
            'nfbVD-5S-PLIC-O-14.483',
            'nfbVD-5S-14.540',
            'nfbVD-5S-PLIC-I-14.691',
            'nfbVD-5S-15.139',
            'nfbVD-5S-SST-15.478',
            'nfbVD-5S-SST-15.856',
            'nfbVD-5S-SST-16.201',
            'nfbVD-5S-SST-16.551',
            'nfbVD-5S-SST-P-16.902',
            'nfbVD-5S-SST-17.253',
            'nfbVD-5S-SST-17.608',
            'nfbVD-5S-SST-17.990',
            'nfbVD-5S-SST-P-18.312',
            'nfbVD-5S-SST-18.663',
            'nfbVD-5S-SST-19.013',
            'nfbVD-5S-SST-19.363',
            'nfbVD-5S-SST-P-19.677',
            'nfbVD-5S-SST-20.063',
            'nfbVD-5S-SST-20.413',
            'nfbVD-5S-SST-20.763',
            'nfbVD-5S-SST-P-21.063',
            'nfbVD-5S-SST-21.460',
            'nfbVD-5S-SST-21.807',
            'nfbVD-5S-SST-22.159',
            'nfbVD-5S-SST-P-22.506',
            'nfbVD-5S-SST-22.859',
            'nfbVD-5S-SST-23.207',
            'nfbVD-5S-SST-23.560',
            'nfbVD-5S-SST-P-23.910',
            'nfbVD-5S-SST-24.264',
            'nfbVD-5S-SST-24.678',
            'nfbVD-5S-SST-24.962',
            'nfbVD-5S-SST-P-25.312',
            'nfbVD-5S-SST-25.664',
            'nfbVD-5S-SST-26.013',
            'nfbVD-5S-SST-26.299',
            'nfbVD-5S-SST-P-26.706',
            'nfbVD-5S-SST-27.054',
            'nfbVD-5S-SST-27.442',
            'nfbVD-5S-SST-27.748',
            'nfbVD-5S-SST-28.236',
            'nfbVD-5S-TCIC-O-29.716',
            'nfbVD-5S-30.140',
            'nfbVD-5S-TCIC-I-30.249',
            'nfbVD-5S-30.266']
    path='/home/engineer/docker/tunnel/django-volume/trips/'
    purposePath='/home/engineer/docker/tunnel/django-volume/trips/data/error/'

    def moveError(self, p) :
        path=re.search('^.*/', p).group()
        fi=re.search('vd_value.xml.gz(\.\d+)?',p).group()
        if re.search('vd_value.xml.gz(\.\d+)?',fi) :
            li=os.listdir(Api.purposePath)
            Nlist=[]
            for l in li :
                Nlist.append(re.search('vd_value.xml.gz(\.\d+)?',l).group())
            success=True
            n=0
            while (success) :
                name='vd_value.xml.gz.'+str(n)
                if n==0 :
                    if not ('vd_value.xml.gz' in Nlist) :
                        purposrName='vd_value.xml.gz'
                        success=False
                elif not name in Nlist :
                    purposrName=name
                    success=False
                n=n+1
            print 'mv '+path+fi+' '+Api.purposePath+purposrName
            os.system('mv '+path+fi+' '+Api.purposePath+purposrName)

    def loadMon(self, year, mon) :
        m=[31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mon=int(mon)
        for i in range(2,m[mon-1]+1) :
            self.loadDay(year, mon, i)

    def loadDay(self, year, mon, day) :
        d=self.padded(year)+self.padded(mon,2)+self.padded(day,2)
        #for i in range(0, 2356) :
            #si=self.padded(i)
            #url='http://tisvcloud.freeway.gov.tw/history/vd/'+d+'/vd_value_'+si+'.xml.gz'
            #result=os.popen('wget -P '+Api.path+'data/vd/ '+url+' >/dev/null 2>/dev/null &')
        for i in range(0,2356) :
            si=self.padded(i)
            url='http://tisvcloud.freeway.gov.tw/history/vd/'+d+'/vd_value_'+si+'.xml.gz'
            path='data/vd/vd_value_'+si+'.xml.gz'
            self.saveData(path, url)
            print d, i

    def padded(self, number,p=4) :
        number=int(number)
        if p==2 :
            if number<10 :
                return '0'+str(number)
            else :
                return str(number)
        if number>999 :
            return str(number)
        if number>99 :
            return '0'+str(number)
        if number>9 :
            return '00'+str(number)
        if number>-1 :
            return '000'+str(number)
        raise Exception('input error')

    def getdata(self, path, url) :
        if url=='http://tisvcloud.freeway.gov.tw/vd_value.xml.gz' :
            result=os.popen('wget -P '+Api.path+'data/vd/ http://tisvcloud.freeway.gov.tw/vd_value.xml.gz ')
        elif url!=None :
            result=os.popen('wget -P '+Api.path+'data/vd/ '+url+' >/dev/null 2>/dev/null').read()
        with gzip.open(path) as f :
            m=f.read()
            if m!=None :
		a=minidom.parseString(m)
                return a
            else :
                print 'wget Error'
                raise Exception('wget ERROR')

    def getData(self, path, url, model='default') :
        xml=self.getdata(path, url).getElementsByTagName('Info')
        ln=[]
        ls=[]
        for x in xml :
            if x.attributes['vdid'].value in Api.nvdid :
                data=self.getInfo(x)
                if model=='average' :
                    data=self.getVM(data)
                ln.append(data)
            if x.attributes['vdid'].value in Api.svdid :
                data=self.getInfo(x)
                if model=='average' :
                    data=self.getVM(data)
                ls.append(data)
        time=xml[0].attributes['datacollecttime'].value
        return [time ,[ln, ls]]

    def saveData(self, path='data/vd/vd_value.xml.gz', url=None) :
        if path=='data/vd/vd_value.xml.gz' :
            path=Api.path+path
        try :
            [time, li]=self.getData(path, url)
            pathX=self.getFilePath(time,'xml')
            pathJ=self.getFilePath(time,'json')
            result=os.popen('mv '+path+' '+pathX)
            print 'out XML: ', pathX
            with open(pathJ,'w') as f :
                f.write(json.dumps(li))
                print 'out JSON:', pathJ
        except :
            error=sys.exc_info()
            print '########################################################'
            traceback.print_exception(error[0], error[1], error[2],limit=2, file=sys.stdout)
            self.moveError(path)

    def getFilePath(self, t, forma ) :
        d=re.search('\d\d\d\d/\d\d/\d\d', t).group()
        t=re.search('\d\d:\d\d:\d\d',t).group()
        time=t[0:2]+'_'+t[3:5]+'_'+t[6:8]
        
        dir_mon=d[0:4]+'_'+d[5:7]
        dir_date=dir_mon+'_'+d[8:10]
        path=Api.path+'data/'+forma+'/'+dir_mon+'/'+dir_date+'/'
        if not os.path.exists(path) :
            os.makedirs(path)
        path=path+dir_date+'-'+time
        if forma=='xml' :
            path=path+'.xml.gz'
        elif forma=='json' :
            path=path+'.json'

        return path

    def getInfo(self, info) :
        li=[]
        for lane in info.childNodes :
            if lane.childNodes!=() :
                speed=int(lane.attributes['speed'].value)
                number_sum=0;
                for cars in lane.childNodes :
                    if cars.childNodes!=() :
                        number_sum=number_sum+int(cars.attributes['volume'].value)
                li.append([speed, number_sum])
        return li

    def getVN(self, li) :
        speed_sum=0;
        number_sum=0;
        for l in li :
            speed_sum=speed_sum+li[0]*li[1]
            number_sum=number_sum+li[1]
        if number_sum==0 :
            return [0, 0]
        return [speed_sum/number_sum ,number_sum]



if __name__=='__main__' :
    a=Api()
    arg=sys.argv[1]
    if arg=='download' :
        a.saveData(url='http://tisvcloud.freeway.gov.tw/vd_value.xml.gz')
    elif arg=='moveerror' or arg=='movevd' :
        errorPath=os.path.dirname(os.path.realpath(__file__))+'/data/error'
        vdPath=os.path.dirname(os.path.realpath(__file__))+'/data/vd'
        path=os.path.dirname(os.path.realpath(__file__))+'/data/buffer/'
        if arg=='moveerror' :
             os.system('mv '+errorPath+'/vd_value.xml.gz.* '+path)
        elif arg=='movevd' :
             os.system('mv '+vdPath+'/vd_value.xml.gz.* '+path)
        li=os.listdir(path)
        for l in li :
            a.saveData(path=path+l)

