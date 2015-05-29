#!/usr/bin/python
#
'''
	write down upload message in log.txt
'''
import time,iteration


def writedown (upload_name):
	upload_time = int(time.time())
	with open(iteration.logpath,'a+') as f:
		f.write(upload_name + ':' + str(upload_time) +'\n')
		f.flush()



