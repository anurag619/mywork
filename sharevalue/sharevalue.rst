sharevalue
-----------
here i am python script which will show us the latest nasdaq value. we will be using urllib2 module to fetch the url.

`sharevalue.py`_ code link.

.. _sharevalue.py: http://github.com
 

::

        import urllib2    #imports module urllib2
        import sys      #imports module sys

        def nasdaq(value):      #creating a function nasdaq
        
                find = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1'%value)        #
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
        


*to run the code*

$python sharevalue.py FB


