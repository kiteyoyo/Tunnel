#!/bin/bash 
url='http://tisvcloud.freeway.gov.tw/history/vd/'

url=${url}$1
if [ $2 -lt 10 ]; then
	url=${url}0$2
else
	url=${url}$2
fi

if [ $3 -lt 10 ]; then
	url=${url}0$3
else
	url=${url}$3
fi

for i in $(seq 0 23)
do
	for j in $(seq 0 59)
	do
		if [$i -lt 10 ]; then
			number=0$i
		else
			number=$i
		fi
		if [ $j -lt 10 ]; then
			number=${number}0$j
		else
			number=${number}$j
		fi
		wget -P ./buffer/ ${url}/vd_value_${number}.xml.gz
	done
done
