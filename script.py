#!/usr/bin/python

#Atkin Julian, Zeng Haley
#SoftDev1 pd8
#HW01 -- Divine your Destiny
#2016-09-15

import random


def prep(importStr):
    data = importStr.strip().split("\r\n")
    data.pop(0) #remove headers
    data.pop(len(data) - 1) #remove total
    return data

def makeDict(data):
    d = {}
    for i in range(len(data)):
        #getting the data in a workable form
        array = data[i].split(",")
        if len(array) > 3:
            array = [ ",".join(array[0:len(array)-2]) , array[-2] , array[-1]]
            array[0] = array[0][1:len(array[0])-1] #remove " "
        data[i] = array
       
        job = array[0]
        percent = float(array[1])
        link = array[2]

        d[job] = [percent, link]
    return d




'''
how the weighting works:
- imagine a number line [0, 100)
- divide the number line proportionally to each of the percentages
- pick a random number
- starting at 0, find out which percentage bounds your random number
- the occupation matched w/ that % is the one that is printed
'''

def choose(d):
    choice = random.random() * 100
    summ = 0
    for key in d.keys():
        summ += d[key][0]
        if summ > choice:
            return key

def getDict():
    return d

f = open("occupations.csv","r")
fText = f.read()

d = makeDict(prep(fText))

if __name__ == "__main__":
    print choose(d)
