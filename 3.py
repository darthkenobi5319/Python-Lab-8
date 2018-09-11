# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 11:03:26 2017

@author: ZHENGHAN ZHANG
"""

#first load the file
#f=open('C:\Users\ZHENGHAN ZHANG\Desktop\Python\2017.10.5\board.txt','r')
f=open('board.txt','r')
ls1=[]
while True:
    c=f.readline().strip()
    if c == '':
        break
    ls2 = list(c)
    ls1.append(ls2)
f.close()

#put the matrix on a board
for i in range(len(ls1)-1):
    m=''
    for j in ls1[i]:
        m+=j
        m+='|'
    print(m[:-1])
    l='-+'*len(ls1[i])
    print(l[:-1])
m=''
for j in ls1[-1]:
    m+=j
    m+='|'
print(m[:-1])    


#user interaction
while True:
    x=input('Please enter two coordinates (row,col): (enter "stop" to end) ').split(',')
    if x[0]=='stop':
        break
    y=input('Please enter a letter: ')
    row=int(x[0])
    column=int(x[1])
    ls1[row][column]=y
m=''
for i in range(len(ls1)):
    for j in range(len(ls1[i])):
        m+=ls1[i][j]
    m+='\n'
f=open('board.txt','w')
f.write(m)
f.close()