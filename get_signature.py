#!/usr/bin/env python
import base64,hashlib,hmac,time,urllib
def getSignaureUrl():
		#add AWSAccessKeyId,Service,Timestamp,Version to params
		accessKey = 'accessKeyValue'
		secretKey = 'secretKeyVale'
		params={}
		params['AWSAccessKeyId'] = accessKey
		params['Service'] = 'AWSCommerceService'
		params['Timestamp'] = time.strftime("%Y-%m-%dT%H:%M:%S.000Z",time.gmtime())
		params['Version'] = '2009-01-06'
		#sort params
		paramList = params.items()
		paramList.sort()
		#debug
		#print paramList
		
		canonicalizedQueryString = '&'.join(['%s=%s' % (k,urllib.quote(str(v))) for (k,v) in paramList if v])
		#debug
		#print canonicalizedQueryString
		#Create string to sign
		host = 'ecs.amazon.com'
		requestUri = '/onca/xml'
		stringToSign = 'GET\=n'
		stringToSign+= host +'\n'
		stringToSign+= requestUri +'\n'
		stringToSign+= canonicalizedQueryString.encode('utf-8')
	
		#Create HMAC
		digest = hmac.new(secretKey,msg=stringToSign,digestmod=hashlib.sha256).digest()
		
		#base64
		sig = base64.b64encode(digest)
		
		#append the sig to query
		url  = 'http://' + host + requestUri + '?'
		url += canonicalizedQueryString + "&Signature=" + urllib.quote(sig)
		print url
		return url
getSignaureUrl()
