#python script to extract author and titles from a web blog
#module beautifulsoup should be installed before running the scrip



from bs4 import BeautifulSoup #import beautifulsoup
import urllib2 #import urllib2 for generating the web address

def main():  #the main function
 
	url = "http://planet.fedoraproject.org/"  #the url used to extract the authors and titles
	content = urllib2.urlopen(url)  
	soup = BeautifulSoup(content)  #beautifulsoup parses the website content 
	print_title_and_name(soup)   #function call to print the authors and titles

def print_title_and_name(soup):
	data_titles = soup.find_all('div', class_="blog-entry-title")  #find_all method to rip apart the desired html code
	total_entries = len(data_titles) #total number of titles
	data_authors = soup.find_all('div', class_="blog-entry")
	total_authors = len(data_authors) #total number of authors
	for i in range(total_entries):  #loop to print titles and authors
		titles = " %s " % data_titles[i].find('a').string 
		
		print "auhor of %s is %s " % (titles,data_authors[i].find('a').string)

if __name__== '__main__':  #standard condition to call the main() 
	main()

