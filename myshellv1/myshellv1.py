#python script to get a shell with (Cmd) as prompt

from cmd2 import Cmd
import getpass
import requests
 
__version__ = '0.1'
 
class Application(Cmd):
    """
   The main Application class
 
   """
 
    def __init__(self): #inherits Cmd and  any method starting with do_ becomes a command
        Cmd.__init__(self)
 
    def do_hello(self, line):
        print "Hello:", line

    def do_sayit(self, line): 	#command sayit which will print "python rocks" 
	print "Python Rocks!"

    def do_greet(self,line):  #greet command 
	print "Hi, %s" %(getpass.getuser())

    def do_stock(self,line):  #stock command will print the latest NASDAQ value when given in a valid value
	url = requests.get('http://download.finance.yahoo.com/d/quotes.csv?s='+line+'&f=l1')
	stock_value = (url.text)
	print stock_value


 
if __name__ == '__main__':
    app = Application()
    app.cmdloop()

