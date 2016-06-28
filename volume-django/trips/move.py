#!/usr/bin/env python
import os
from api import Api
if __name__=='__main__' :
	path=os.path.dirname(os.path.realpath(__file__))+'/data/buffer/'
	print path
	li=os.listdir(path)
	a=Api()
	for l in li :
		a.saveData(path=path+l)
