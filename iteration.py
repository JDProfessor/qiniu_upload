#!/usr/bin/python
#
'''
	iterate files
	get the last ctime 
	compare the last ctime with the ctime of to be upload file
'''
import os,re,baseinfo

def iterate (filepath = baseinfo.backupdir):
	file_path = []
	for root,dirs,files in os.walk(filepath):
		for filepath in files:
			namepath = os.path.join(root,filepath)
			file_path.append(namepath)
	return file_path
file_path = iterate()	

director = os.getcwd()
logpath = director +'/log.txt'

def getctime ():
	f = open(logpath)
	lines = f.readlines()
	try:
		line = str(lines[-1])
		pattern = r'\d{10}'
		last_time = re.compile(pattern)
		last_time = last_time.findall(line)
	except IndexError:
		last_time = [0]
	finally:
		f.close
		return last_time

last_time = getctime()
#print last_time

def compare (file_path):
	upload_file = []
	for filename in file_path :
		ctime = int(os.path.getctime(filename))
		if ctime > int(last_time[0]) :
			upload_file.append(filename)
	return upload_file

upload_file =  compare(file_path)		

if __name__ == '__main__':
	print upload_file				
