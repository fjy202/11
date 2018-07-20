#-*- coding:utf-8 -*-
import os
from os import path
import urllib.request
import time
def mk_link(url):
    try:
        urllib.request.urlopen (url).read ()
    except:
        print("错误：无法访问。url需带协议。")
        exit()
    f=open(r'C:\Users\Administrator\Desktop\\'+input("名称:")+'.url','w')
    f.write('[{000214A0-0000-0000-C000-000000000046}]')
    f.write('\n')
    f.write('Prop3=19,4')
    f.write ('\n')
    f.write('[InternetShortcut]')
    f.write ('\n')
    f.write("URL="+url)
    f.write ('\n')
    f.write('IDList=')
mk_link(input("url:"))
