#!/usr/bin/env python
import requests
import json
import os

class set_rule():

        def __init__(self): 
                my_ip = ""
                my_token = ""
                my_rule =""

        def set_data(self,rule):
                self.my_rule = rule
                with open('my_ip.txt','r') as f:
                        self.my_ip = f.read()

                with open('my_token.txt','r') as f:
                        self.my_token = f.read()

        def remove(self):
                rule_data = ''
                rule_flug = os.path.exists("./my_rule.txt")

                if rule_flug: 
                        with open('my_rule.txt', 'r') as f:
                                rule_data = f.read()
                        url='https://networking.tyo1.conoha.io/v2.0/security-group-rules/'+rule_data
                        header={'Accept':'application/json','X-Auth-Token':''}
                        header['X-Auth-Token']=self.my_token
                        r = requests.delete(url,headers=header)
                        print "delete_rule_data="+rule_data

                if rule_flug == False:
                        print "no_rule_data"

        def set_ip(self):
                url = "https://networking.tyo1.conoha.io/v2.0/security-group-rules"
                header = {'Accept':'application/json','X-Auth-Token':''}
                header['X-Auth-Token']=self.my_token
                data = {"security_group_rule":{"direction": "ingress","ethertype": "IPv4","security_group_id":"","protocol":"tcp" ,"remote_ip_prefix":""}}
                data["security_group_rule"]["security_group_id"]=self.my_rule
                data["security_group_rule"]["remote_ip_prefix"]=self.my_ip

                r = requests.post(url,data=json.dumps(data),headers=header)

                with open('rule_data.json','w') as f:
                        f.write(r.text)

                with open('rule_data.json','r') as f:
                        jsonData = json.loads(f.read())

                with open('my_rule.txt','w') as f:
                        f.write(jsonData["security_group_rule"]["id"])
                        print "set_rule="+jsonData["security_group_rule"]["id"]

def set_rule_main(group):
        groupid = group
        rule_setter = set_rule()
        rule_setter.set_data(groupid)
        rule_setter.remove()
        rule_setter.set_ip()


if __name__ == '__main__':
        set_rule_main("security_group_ID")
