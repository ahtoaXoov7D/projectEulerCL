#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 44
# found online at projecteuler.net/problem=44
# Solution by Timothy Reasa
#
###############################################################################

limit = 10000	# arbitrary limit

description = \
'Pentagonal numbers are generated by the formula, Pn=n(3n1)/2. The first\n' + \
'ten pentagonal numbers are:\n\n' + \
'\t1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...\n\n' + \
'It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their\n' + \
'difference, 70 - 22 = 48, is not pentagonal.\n\n' + \
'Find the pair of pentagonal numbers, Pj and Pk, for which their sum and\n' + \
'difference is pentagonal and D = |Pk - Pj| is minimised; what is the\n' + \
'value of D?\n'

def display(self):
    return description

def solve(self):
    pentList = [0] * limit
    pentSet = set()
    p = 0

    for i in range(1, limit):
	p = i*(3*i-1)/2
	pentList[i] = p
 	pentSet.add(p)

    minD = pentList[limit-1]
    s = 0
    d = 0
    for i in range(1, limit):
	for j in range(1, i):
	    s = pentList[i] + pentList[j]
	    d = abs(pentList[i] - pentList[j])
	    if s in pentSet and d in pentSet and d < minD:
		minD = d	

###############################################################################
#
# Returning the first found candidate is much quicker, but there is no
# reason to believe the minimum candidate is the first found.
#
# In fact, I don't think there is a reason to believe the the minimum
# candidate only uses the for 10000 pentagonal numbers either
#
###############################################################################
    
    return minD


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)