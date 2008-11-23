#!/usr/bin/python

from datetime import *

delta = timedelta(hours=1-2) # one hour
expire_time = datetime.now() + delta
print expire_time.strftime("%a, %d %b %Y %H:%M:%S") + " GMT"
