#!/usr/bin/env python

from encode import multipart_encode
from streaminghttp import register_openers
import urllib2,tkproductor,iteration,log


register_openers()

product_token = tkproductor.present_token
upload_dic = {}
upload_file = iteration.upload_file
for upload_name in upload_file :
	upload_dic["key"] = upload_name
	upload_dic["token"] = product_token
	upload_dic["file"] = open(upload_name,"rb")
	log.writedown (upload_name)
	datagen, headers = multipart_encode(upload_dic)
	request = urllib2.Request("http://upload.qiniu.com/", datagen, headers)
	print urllib2.urlopen(request).read()
		

