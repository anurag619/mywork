mount
------

here I will be displaying the output of mount command. the file to be read is located in /proc/mounts

source file:'mount.py <https://github.com/anurag619/mywork/blob/master/mount/mount.py>'_

::
        #python file for mount operation

        m= open("/proc/mounts") #opening of the file mounts
        for lines in m:    #reading every line in m
          print lines 
        m.close()       #file closed after operation

*to execute the file* 

$python mount.py




