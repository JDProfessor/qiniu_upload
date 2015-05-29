#!/usr/bin/python
'''
 Product token
'''
import baseinfo,base64,hmac,hashlib,time,re

putpolicy = baseinfo.dic
sk = baseinfo.sk
ak = baseinfo.ak

def base_64(putpolicy):
	encoded = base64.b64encode(putpolicy)
	encoded = encoded.replace('+','-')
	encoded = encoded.replace('/','_')
	if re.match(r'.*=$',encoded) :
		encoded_policy = encoded
	else :
		encoded_policy = encoded + '='
	return encoded_policy
#print base_64(putpolicy)

encoded_policy = base_64(putpolicy)
#print sk,encoded_policy
binhmac =  hmac.new(sk, encoded_policy, digestmod=hashlib.sha1).digest()
#print binhmac
sign = base_64(binhmac)
#print sign
present_token = ak+':'+sign+':'+encoded_policy

if __name__ == '__main__':
	print present_token
