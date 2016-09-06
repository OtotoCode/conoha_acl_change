#!/usr/bin/env python

import requests
import json
import datetime
import os

class get_token:
        def __init__(self):
                self.values = {"auth":{"passwordCredentials":{"username":"","password":""},"tenantId":""}}

        def set(self,user,passwd,tnid):
                self.user = user
                self.passwd = passwd
                self.tnid = tnid

        def getter(self):
                get_flag = True
                if os.path.exists("./my_token_expire.txt"):
                        with open('my_token_expire.txt','r') as f:
                                tk_ex = f.read()
                                tk_ex = tk_ex.replace("T"," ")
                                tk_ex = tk_ex.replace("Z","")
                                tk_ex_time =  datetime.datetime.strptime(tk_ex, '%Y-%m-%d %H:%M:%S')
                                today =  datetime.datetime.utcnow()

                                if today < tk_ex_time:
                                        get_flag = False
                                        print 'active token'
                                else:
                                        print 'expired token'

                else:
                        print 'token file not found'


                if get_flag:
                        url = 'https://identity.tyo1.conoha.io/v2.0/tokens'
                        self.values["auth"]["passwordCredentials"]["username"]=self.user
                        self.values["auth"]["passwordCredentials"]["password"]=self.passwd
                        self.values["auth"]["tenantId"]=self.tnid
                        head = {'Accept':'application/json'}
                        r = requests.post(url,data=json.dumps(self.values),headers=head)
                        with open('my_token.json','w') as f:
                                f.write(r.text)
                                f.flush()

                        with open('my_token.json','r') as f:
                                jsonData = json.loads(f.read())

                        with open('my_token.txt','w') as f:
                                f.write(jsonData["access"]["token"]["id"])
                                f.flush()
                                print 'write token'

                        with open('my_token_expire.txt','w') as f:
                                f.write(jsonData["access"]["token"]["expires"])
                                f.flush()
                                print 'expires='+jsonData["access"]["token"]["expires"]


def token_get_main(user,passwd,tenantId):
        token_get = get_token()
        token_get.set(user,passwd,tenantId)
        token_get.getter()

if __name__ == '__main__':
        user = 'user'
        ps = 'pass'
        tenantId = 'tenantID'
        token_get_main(user,ps,tenantId)
