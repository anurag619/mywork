import urllib2
import sys

def nasdaq(value):
	
	find = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1'%value)
	print "NASDAQ value of %s is %s " %(value.upper(), find.read()) 
	find.close()

def main():
	if len (sys.argv)!= 2:
	 print "enter the script and the NASDAQ sysmbol, like GOOG,FB,YHOO etc"
	else:
	 nasdaq(sys.argv[1])
	sys.exit(0)


if __name__ == '__main__':
	main() 
	
