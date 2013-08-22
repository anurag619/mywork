
import sys
import argparse
import json

data = []

def add_log(name,date,text):
 data = {'name': name, 'date': date, 'text': text}
 with open('log.json', 'w') as outfile:
  json.dump(data, outfile)


if __name__ == '__main__':
 print len(sys.argv)
 if len(sys.argv)== 4:
   add_log(sys.argv[1],sys.argv[2],sys.argv[3])
 


