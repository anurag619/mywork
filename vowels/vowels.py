
import sys

def check(val):
 i = 0
 alph = ['a','e','i','o','u']
 file = open(val, "r+")
 lines = file.read()
 words = lines.split()
 for word in words:
   for j in range(len(alph)):
    if word[0][0]==alph[j]:
     i=i+1
 print "there are %d words which starts with a vowel in the text file" %i


if __name__=='__main__':
 check(sys.argv[1])
 
