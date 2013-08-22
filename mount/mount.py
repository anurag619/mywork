# python file for displaying mount operation

m= open("/proc/mounts") #opening of the file mounts
for lines in m:  #reading every line in m
 print lines
m.close()        #file closed after operation

