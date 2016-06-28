#!/bin/bash
if [ "${1}" = "download" ] || [ "${1}" = "moveerror" ]; then
	python /usr/src/app/trips/api.py ${1} > /usr/src/app/out 2> /usr/src/app/error
fi
