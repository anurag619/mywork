
import os
import time
import sys
import json

x = 0
while x<5:
 load = os.getloadavg()
 time.sleep(2)
 with open('timeavg.json', 'a+') as outfile:
  json.dump(load, outfile)
 x = x+1



