import os
import re
import sys
import numpy

def checkKeyword(words):
    keywords = ['include','void','int','float','struct','break','if','else','for','long','typedef','do','while','return','char','union','else','continue']
    counter = 0
    flag = False
    for keyword in keywords:
        if keyword == words:
            counter = counter + 1
            flag = True
    return counter,flag

def checkSymbols(line):
    symbols = [';',':','#','!','@','$','^','(',')','{','}',',']
    counter = 0
    flag = False
    for symbol in symbols:
        if symbol == words:
            counter = counter + 1
            flag = True
    return (counter),flag

def checkOperators(line):
    operators = ['+','-','*','/','%','==','!=','<=','>=','&&','=','++','--','<','>']
    counter = 0
    flag = False
    for operator in operators:
        if operator == words:
            counter = counter + 1
            flag = True
    return (counter),flag

files = os.listdir('.')

for names in files:
    if names[-2:] == '.c':
        keywords = 0
        symbols = 0
        operators = 0
        countMain = 0
        with open(names,'r') as f:
            contents = f.read().splitlines()
        print ("Code to be analyzed from "+names +" is ")
        for lines in contents:
            if lines[0:2] != '//' and lines[0:4] != 'prin' and lines[0:4] != 'scan':
                #print (lines)
                for words in lines.split(' '):
                    count,flagK = checkKeyword(words)
                    keywords = keywords + count
                    count1,flagS = checkSymbols(words)
                    symbols = symbols + count1
                    count2,flagO = checkOperators(words)
                    operators = operators + count2
                    if not flagK and not flagO and not flagS and words != 'main()' and words[0:1] != '<':
                        #print ("Word is identifier "+words)
                        countMain = countMain + 1 
        print ("Keywords = ",keywords)        
        print ("Symbols = ",symbols)
        print ("Operators = ",operators)
        print ("Identifiers = ",countMain)


#checkKeyword('float int int float')