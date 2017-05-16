#This module implement some simple math operations:

import numpy as np

#-------MYCEIL_DIV2 -> take an integer number and return the ceiling of its division by 2

def ceil_div2(i):
    return i/2 + i % 2


#-------MYFLOOR_DIV2 -> take an integer number and return the floor of its division by 2

def floor_div2(i):
    return i/2 

#----- MYMOD_ABS -> take an integer number and return mod_2 of its anbsolute value

def mod_abs(i):
    return abs(i) % 2

#-----MYNORM -> take the norm of an array "x"

def norm(x):
    return np.max(np.abs(x))


#print np.abs([1,2])
