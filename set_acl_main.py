#!/usr/bin/env python


import ip
import get_token
import set_acl

get_ip_url = "address"
user = 'user_name'
key = 'password'
tenantId = 'tenant_ID'
security_group = "security_group_ID"

if __name__ == '__main__':
        ip.ip_get(get_ip_url)
        get_token.token_get_main(user,key,tenantId)
        set_acl.set_rule_main(security_group)
