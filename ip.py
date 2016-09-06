#!/usr/bin/env python

import requests
from HTMLParser import HTMLParser
import codecs

class MYHTMLParser(HTMLParser): 
        def __init__(self):
                HTMLParser.__init__(self)
                self.mytag = ''

        def handle_starttag(self,tag, attrs): 
                if tag == 'p': 
                        if (dict(attrs).get('name')=="ip"):
                                self.mytag = 'ip'

        def handle_data(self,data): 
                if self.mytag == 'ip': 
                        self.mytag = ''
                        print 'IP='+data
                        with codecs.open('my_ip.txt','w','utf-8') as f:
                                f.write(data)


def ip_get(myurl): 
        r = requests.get(myurl)
        r.encoding = r.apparent_encoding 

        with codecs.open('my_ip.html','w','utf-8') as f:
                f.write(r.text)
                f.flush() 

        with codecs.open('my_ip.html','r','utf-8') as f:
                parser = MYHTMLParser()
                parser.feed(f.read())
                parser.close()


if __name__ == '__main__':
        ip_get("address")
