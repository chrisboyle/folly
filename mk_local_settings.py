#!/usr/bin/env python

import random

def mksecret():
   return ("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))

secret = mksecret()
cachekey = mksecret()

with open('local_secret.py','w') as f:
	f.write( """
DEBUG = True
SECRET_KEY = \"%s\"
NEVERCACHE_KEY= \"%s\"
""" % (secret,cachekey))
