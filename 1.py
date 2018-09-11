# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:14:28 2017

@author: ZHENGHAN ZHANG
"""

#generate 10 random numbers
'''
import random
file1=open('file1','w')
for i in range(10):
    x = str(random.randrange(0,51))
    file1.write(x)
file1.close()

file1=open('file1','r')

while True:
    c=file1.read(1)
    if c == '':
        break
    print(c)
    
'''
#That's one way to do it, or we just write the lines
import random
file1=open('file1','w')
for i in range(10):
    x = str(random.randrange(0,51))+'\n'
    file1.write(x)
file1.close()

file1=open('file1','r')
m=0
while True:
    c=file1.readline()
    if c == '':
        break
    m += int(c)
print(m)
file1.close()