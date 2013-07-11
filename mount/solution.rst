mount
======

here I will be displaying the output of mount command. the file to be read is located in /proc/mounts

source file: https://github.com/anurag619/mywork/blob/master/mount/mount.py



#!/usr/bin/env python
m= open("/proc/mounts") #opening of the file mounts
for lines in m:
 print lines


