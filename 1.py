#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:01:05 2019

@author: m
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 21:05:17 2019
@author: OFOK
"""

import datetime


'''
 Mr. Muhesn thanks for your sloution 
 we need to tell the user when they will turn 
 100 years ould 
 
 currAge = current age 
 x = represent how many more years the user need to 
 turn 100 years old 
 Nturn100 = when they turn 100 years 
 
 currentAge + x =100 
 so x = 100-currentAge 
 then  Nturn100 = currentYear + x  
 '''
 
 
 
Name = raw_input('Enter your name:' )
currAge= raw_input('Enter your age:' )
curdate = datetime.datetime.now()
currentYear = curdate.year
x = 100- int(currAge)
Nturn100 = x + currentYear


print("You will turn 100 years old on " + str(Nturn100)  + "!")
