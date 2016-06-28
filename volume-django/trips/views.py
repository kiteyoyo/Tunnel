# -*- coding: utf8 -*-
# coding=Big5
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from search import search
from getTime import getTime, immedite
import sys, json
reload(sys)
sys.setdefaultencoding('utf8') 
# Create your views here.
def suggestion(request, direction) :
    if direction=='北上' :
        s='頭城'
        d='南港'
    else :
        s='南港'
        d='頭城'
    u=[15, 30, 60, 120]
    p=getTime.getPreductionMore(s, d, u)
    n=immedite.nowTime(s, d)[0]
    t=[]
    for i in p :
        t.append(n-i)
    a=-1
    for i in range(0,4) :
        if t[i]>1 and ( a==-1 or t[a]<t[i] ) :
            a=i
    v=60*30/n
    if a==-1 :
        if v>80 :
            suggest='目前車道順暢，建議現在就上路'
        elif v>60 :
            suggest='目前車道普通，建議現在先上路'
        else :
            suggest='目前車道壅塞，建議下次提早上路'
    else :
        if v>80 :
            suggest='目前車道順暢，建議現在就上路'
        else :
            suggest=str(u[a])+'分後上路，可以省下你'+str(int(t[a]))+'分的時間'
    print 'n:', n
    print 'p:', p
    print 't:', t
    struct={
            'from' : s,
            'to' : d,
            'suggestion' :suggest
            }
    return JsonResponse(struct)

def prediction(request, time, start, destination) :
    s=start
    d=destination
    t=getTime.getPreduction(s, d, time)[0]
    struct={
            'from' : s,
            'to' : d,
            'time' : immedite.nowTime(s, d)[0],
            'forecast' : getTime.getPreduction(s, d,time)[0]
            }
    return JsonResponse(struct)

def predictionAll(request) :
    struct={
            'fifteen' : {
                'north' : 60*30.266/getTime.getPreductionAll(True, 15)[0],
                'south' : 60*30.266/getTime.getPreductionAll(False, 15)[0]
                },
            'thirty' : {
                'north' : 60*30.266/getTime.getPreductionAll(True, 30)[0],
                'south' : 60*30.266/getTime.getPreductionAll(False, 30)[0]
                },
            'sixty' :{
                'north' : 60*30.266/getTime.getPreductionAll(True, 60)[0],
                'south' : 60*30.266/getTime.getPreductionAll(False, 60)[0]
                },
            'twohour' : {
                'north' : 60*30.266/getTime.getPreductionAll(True, 120)[0],
                'south' : 60*30.266/getTime.getPreductionAll(False, 120)[0]
                }
            }
    return JsonResponse(struct)

def getNow(request, start, destination) :
    s=start
    d=destination
    p=immedite.nowTime(s, d)
    return JsonResponse({'from' : s, 'to' : d, 'time' : p[0]})

def getSpeed(request) :
    return JsonResponse(search.getSpeed(),safe=False)

def getCurrent(request) :
    m=search.getSpeed(model='handle')
    n=[sum(m[:9]),sum(m[13:36]),sum(m[38:76])]
    s=[sum(m[78:86]),sum(m[89:111]),sum(m[114:152])]
    nt=n[2]/38
    st=s[2]/37
    na=sum(n)/70
    sa=sum(s)/67
    return JsonResponse({'overall' : {'north' : na, 'south' : sa}, 'tunnel' : {'north' : nt, 'south' : st}})

def home(request) :
    return HttpResponse('home')

