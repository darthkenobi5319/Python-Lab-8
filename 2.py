# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:41:37 2017

@author: ZHENGHAN ZHANG
"""

#first ask the user for input
while True:
    x=input('Do you want to create a new File?(Y/N) ')
    if x == 'Y' or x =='y':    
        phonebook=open('phonebook','w')
        while True:
            name=input('Please enter the name: ')
            if name == '':
                break
            number=input('Please enter the number: ')
            entry=name + ',' + number
            phonebook.write(entry + '\n')
        phonebook.close()
        break    
    elif x == 'N' or x =='n':
        break
    else:
        print('Invalid input')
    
# read the file 
'''    
phonebook=open('phonebook','r')
print(phonebook.read().strip())
phonebook.close()
'''

phonebook=open('phonebook','r')
dictPhonebook={}
while True:
    c=phonebook.readline().strip()
    if c == '':
        break
    list1=c.split(',')
    dictPhonebook[list1[0]]=list1[1]
print(dictPhonebook)    
phonebook.close()


#continuously ask for a name
while True:
    name=input('Please enter the name you wish to seek: ')
    if name == '':
        break
    if name in dictPhonebook:
        print(name, dictPhonebook[name],sep=',')
    else:
        print('Name does not exist')