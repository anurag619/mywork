#python code for printing share values of nasdaq


import urllib2	 #imports module urllib2.
import sys	#imports module sys.


def nasdaq(value):	#creating a function nasdaq.

	
	find = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1'%value)	#urlopen function of urllib2 fetches the url along with the argument.

	print "NASDAQ value of %s is %s " %(value.upper(), find.read()) 	#prints the nasdaq value.

	find.close()

def main():	 #function main.
	
	if len (sys.argv)!= 2:	#checking the length of arguments(condition). 

	 print "enter the script and the NASDAQ sysmbol, like GOOG,FB,YHOO etc"	#print the condition statement.

	else:
	 nasdaq(sys.argv[1])	 #nasdaq function called.

	sys.exit(0)


if __name__ == '__main__':	#standard condition to call the main function.

	main() 
	
