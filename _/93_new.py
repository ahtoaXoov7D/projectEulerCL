#!/usr/bin/env python

from itertools import count

def genset():
    for a in xrange(10):
        for b in xrange(a+1,10):
            for c in xrange(b+1,10):
                for d in xrange(c+1,10):
                    yield [float(a),float(b),float(c),float(d)]

def orderings(arr):
    for a in arr:
        for b in arr:
            if b==a: continue
            for c in arr:
                if c==b or c==a: continue
                for d in arr:
                    if d==c or d==b or d==a: continue
                    yield [a,b,c,d]
funcarr = []

funcarr.append(lambda a,b,c,d: a + (b + (c + d)))
funcarr.append(lambda a,b,c,d: a + ((b + c) + d))
funcarr.append(lambda a,b,c,d: (a + b) + (c + d))
funcarr.append(lambda a,b,c,d: ((a + b) + c) + d)
funcarr.append(lambda a,b,c,d: a + (b + (c - d)))
funcarr.append(lambda a,b,c,d: a + ((b + c) - d))
funcarr.append(lambda a,b,c,d: (a + b) + (c - d))
funcarr.append(lambda a,b,c,d: ((a + b) + c) - d)
funcarr.append(lambda a,b,c,d: a + (b + (c * d)))
funcarr.append(lambda a,b,c,d: a + ((b + c) * d))
funcarr.append(lambda a,b,c,d: (a + b) + (c * d))
funcarr.append(lambda a,b,c,d: ((a + b) + c) * d)
funcarr.append(lambda a,b,c,d: a + (b + (c / d)))
funcarr.append(lambda a,b,c,d: a + ((b + c) / d))
funcarr.append(lambda a,b,c,d: (a + b) + (c / d))
funcarr.append(lambda a,b,c,d: ((a + b) + c) / d)
funcarr.append(lambda a,b,c,d: a + (b - (c + d)))
funcarr.append(lambda a,b,c,d: a + ((b - c) + d))
funcarr.append(lambda a,b,c,d: (a + b) - (c + d))
funcarr.append(lambda a,b,c,d: ((a + b) - c) + d)
funcarr.append(lambda a,b,c,d: a + (b - (c - d)))
funcarr.append(lambda a,b,c,d: a + ((b - c) - d))
funcarr.append(lambda a,b,c,d: (a + b) - (c - d))
funcarr.append(lambda a,b,c,d: ((a + b) - c) - d)
funcarr.append(lambda a,b,c,d: a + (b - (c * d)))
funcarr.append(lambda a,b,c,d: a + ((b - c) * d))
funcarr.append(lambda a,b,c,d: (a + b) - (c * d))
funcarr.append(lambda a,b,c,d: ((a + b) - c) * d)
funcarr.append(lambda a,b,c,d: a + (b - (c / d)))
funcarr.append(lambda a,b,c,d: a + ((b - c) / d))
funcarr.append(lambda a,b,c,d: (a + b) - (c / d))
funcarr.append(lambda a,b,c,d: ((a + b) - c) / d)
funcarr.append(lambda a,b,c,d: a + (b * (c + d)))
funcarr.append(lambda a,b,c,d: a + ((b * c) + d))
funcarr.append(lambda a,b,c,d: (a + b) * (c + d))
funcarr.append(lambda a,b,c,d: ((a + b) * c) + d)
funcarr.append(lambda a,b,c,d: a + (b * (c - d)))
funcarr.append(lambda a,b,c,d: a + ((b * c) - d))
funcarr.append(lambda a,b,c,d: (a + b) * (c - d))
funcarr.append(lambda a,b,c,d: ((a + b) * c) - d)
funcarr.append(lambda a,b,c,d: a + (b * (c * d)))
funcarr.append(lambda a,b,c,d: a + ((b * c) * d))
funcarr.append(lambda a,b,c,d: (a + b) * (c * d))
funcarr.append(lambda a,b,c,d: ((a + b) * c) * d)
funcarr.append(lambda a,b,c,d: a + (b * (c / d)))
funcarr.append(lambda a,b,c,d: a + ((b * c) / d))
funcarr.append(lambda a,b,c,d: (a + b) * (c / d))
funcarr.append(lambda a,b,c,d: ((a + b) * c) / d)
funcarr.append(lambda a,b,c,d: a + (b / (c + d)))
funcarr.append(lambda a,b,c,d: a + ((b / c) + d))
funcarr.append(lambda a,b,c,d: (a + b) / (c + d))
funcarr.append(lambda a,b,c,d: ((a + b) / c) + d)
funcarr.append(lambda a,b,c,d: a + (b / (c - d)))
funcarr.append(lambda a,b,c,d: a + ((b / c) - d))
funcarr.append(lambda a,b,c,d: (a + b) / (c - d))
funcarr.append(lambda a,b,c,d: ((a + b) / c) - d)
funcarr.append(lambda a,b,c,d: a + (b / (c * d)))
funcarr.append(lambda a,b,c,d: a + ((b / c) * d))
funcarr.append(lambda a,b,c,d: (a + b) / (c * d))
funcarr.append(lambda a,b,c,d: ((a + b) / c) * d)
funcarr.append(lambda a,b,c,d: a + (b / (c / d)))
funcarr.append(lambda a,b,c,d: a + ((b / c) / d))
funcarr.append(lambda a,b,c,d: (a + b) / (c / d))
funcarr.append(lambda a,b,c,d: ((a + b) / c) / d)
funcarr.append(lambda a,b,c,d: a - (b + (c + d)))
funcarr.append(lambda a,b,c,d: a - ((b + c) + d))
funcarr.append(lambda a,b,c,d: (a - b) + (c + d))
funcarr.append(lambda a,b,c,d: ((a - b) + c) + d)
funcarr.append(lambda a,b,c,d: a - (b + (c - d)))
funcarr.append(lambda a,b,c,d: a - ((b + c) - d))
funcarr.append(lambda a,b,c,d: (a - b) + (c - d))
funcarr.append(lambda a,b,c,d: ((a - b) + c) - d)
funcarr.append(lambda a,b,c,d: a - (b + (c * d)))
funcarr.append(lambda a,b,c,d: a - ((b + c) * d))
funcarr.append(lambda a,b,c,d: (a - b) + (c * d))
funcarr.append(lambda a,b,c,d: ((a - b) + c) * d)
funcarr.append(lambda a,b,c,d: a - (b + (c / d)))
funcarr.append(lambda a,b,c,d: a - ((b + c) / d))
funcarr.append(lambda a,b,c,d: (a - b) + (c / d))
funcarr.append(lambda a,b,c,d: ((a - b) + c) / d)
funcarr.append(lambda a,b,c,d: a - (b - (c + d)))
funcarr.append(lambda a,b,c,d: a - ((b - c) + d))
funcarr.append(lambda a,b,c,d: (a - b) - (c + d))
funcarr.append(lambda a,b,c,d: ((a - b) - c) + d)
funcarr.append(lambda a,b,c,d: a - (b - (c - d)))
funcarr.append(lambda a,b,c,d: a - ((b - c) - d))
funcarr.append(lambda a,b,c,d: (a - b) - (c - d))
funcarr.append(lambda a,b,c,d: ((a - b) - c) - d)
funcarr.append(lambda a,b,c,d: a - (b - (c * d)))
funcarr.append(lambda a,b,c,d: a - ((b - c) * d))
funcarr.append(lambda a,b,c,d: (a - b) - (c * d))
funcarr.append(lambda a,b,c,d: ((a - b) - c) * d)
funcarr.append(lambda a,b,c,d: a - (b - (c / d)))
funcarr.append(lambda a,b,c,d: a - ((b - c) / d))
funcarr.append(lambda a,b,c,d: (a - b) - (c / d))
funcarr.append(lambda a,b,c,d: ((a - b) - c) / d)
funcarr.append(lambda a,b,c,d: a - (b * (c + d)))
funcarr.append(lambda a,b,c,d: a - ((b * c) + d))
funcarr.append(lambda a,b,c,d: (a - b) * (c + d))
funcarr.append(lambda a,b,c,d: ((a - b) * c) + d)
funcarr.append(lambda a,b,c,d: a - (b * (c - d)))
funcarr.append(lambda a,b,c,d: a - ((b * c) - d))
funcarr.append(lambda a,b,c,d: (a - b) * (c - d))
funcarr.append(lambda a,b,c,d: ((a - b) * c) - d)
funcarr.append(lambda a,b,c,d: a - (b * (c * d)))
funcarr.append(lambda a,b,c,d: a - ((b * c) * d))
funcarr.append(lambda a,b,c,d: (a - b) * (c * d))
funcarr.append(lambda a,b,c,d: ((a - b) * c) * d)
funcarr.append(lambda a,b,c,d: a - (b * (c / d)))
funcarr.append(lambda a,b,c,d: a - ((b * c) / d))
funcarr.append(lambda a,b,c,d: (a - b) * (c / d))
funcarr.append(lambda a,b,c,d: ((a - b) * c) / d)
funcarr.append(lambda a,b,c,d: a - (b / (c + d)))
funcarr.append(lambda a,b,c,d: a - ((b / c) + d))
funcarr.append(lambda a,b,c,d: (a - b) / (c + d))
funcarr.append(lambda a,b,c,d: ((a - b) / c) + d)
funcarr.append(lambda a,b,c,d: a - (b / (c - d)))
funcarr.append(lambda a,b,c,d: a - ((b / c) - d))
funcarr.append(lambda a,b,c,d: (a - b) / (c - d))
funcarr.append(lambda a,b,c,d: ((a - b) / c) - d)
funcarr.append(lambda a,b,c,d: a - (b / (c * d)))
funcarr.append(lambda a,b,c,d: a - ((b / c) * d))
funcarr.append(lambda a,b,c,d: (a - b) / (c * d))
funcarr.append(lambda a,b,c,d: ((a - b) / c) * d)
funcarr.append(lambda a,b,c,d: a - (b / (c / d)))
funcarr.append(lambda a,b,c,d: a - ((b / c) / d))
funcarr.append(lambda a,b,c,d: (a - b) / (c / d))
funcarr.append(lambda a,b,c,d: ((a - b) / c) / d)
funcarr.append(lambda a,b,c,d: a * (b + (c + d)))
funcarr.append(lambda a,b,c,d: a * ((b + c) + d))
funcarr.append(lambda a,b,c,d: (a * b) + (c + d))
funcarr.append(lambda a,b,c,d: ((a * b) + c) + d)
funcarr.append(lambda a,b,c,d: a * (b + (c - d)))
funcarr.append(lambda a,b,c,d: a * ((b + c) - d))
funcarr.append(lambda a,b,c,d: (a * b) + (c - d))
funcarr.append(lambda a,b,c,d: ((a * b) + c) - d)
funcarr.append(lambda a,b,c,d: a * (b + (c * d)))
funcarr.append(lambda a,b,c,d: a * ((b + c) * d))
funcarr.append(lambda a,b,c,d: (a * b) + (c * d))
funcarr.append(lambda a,b,c,d: ((a * b) + c) * d)
funcarr.append(lambda a,b,c,d: a * (b + (c / d)))
funcarr.append(lambda a,b,c,d: a * ((b + c) / d))
funcarr.append(lambda a,b,c,d: (a * b) + (c / d))
funcarr.append(lambda a,b,c,d: ((a * b) + c) / d)
funcarr.append(lambda a,b,c,d: a * (b - (c + d)))
funcarr.append(lambda a,b,c,d: a * ((b - c) + d))
funcarr.append(lambda a,b,c,d: (a * b) - (c + d))
funcarr.append(lambda a,b,c,d: ((a * b) - c) + d)
funcarr.append(lambda a,b,c,d: a * (b - (c - d)))
funcarr.append(lambda a,b,c,d: a * ((b - c) - d))
funcarr.append(lambda a,b,c,d: (a * b) - (c - d))
funcarr.append(lambda a,b,c,d: ((a * b) - c) - d)
funcarr.append(lambda a,b,c,d: a * (b - (c * d)))
funcarr.append(lambda a,b,c,d: a * ((b - c) * d))
funcarr.append(lambda a,b,c,d: (a * b) - (c * d))
funcarr.append(lambda a,b,c,d: ((a * b) - c) * d)
funcarr.append(lambda a,b,c,d: a * (b - (c / d)))
funcarr.append(lambda a,b,c,d: a * ((b - c) / d))
funcarr.append(lambda a,b,c,d: (a * b) - (c / d))
funcarr.append(lambda a,b,c,d: ((a * b) - c) / d)
funcarr.append(lambda a,b,c,d: a * (b * (c + d)))
funcarr.append(lambda a,b,c,d: a * ((b * c) + d))
funcarr.append(lambda a,b,c,d: (a * b) * (c + d))
funcarr.append(lambda a,b,c,d: ((a * b) * c) + d)
funcarr.append(lambda a,b,c,d: a * (b * (c - d)))
funcarr.append(lambda a,b,c,d: a * ((b * c) - d))
funcarr.append(lambda a,b,c,d: (a * b) * (c - d))
funcarr.append(lambda a,b,c,d: ((a * b) * c) - d)
funcarr.append(lambda a,b,c,d: a * (b * (c * d)))
funcarr.append(lambda a,b,c,d: a * ((b * c) * d))
funcarr.append(lambda a,b,c,d: (a * b) * (c * d))
funcarr.append(lambda a,b,c,d: ((a * b) * c) * d)
funcarr.append(lambda a,b,c,d: a * (b * (c / d)))
funcarr.append(lambda a,b,c,d: a * ((b * c) / d))
funcarr.append(lambda a,b,c,d: (a * b) * (c / d))
funcarr.append(lambda a,b,c,d: ((a * b) * c) / d)
funcarr.append(lambda a,b,c,d: a * (b / (c + d)))
funcarr.append(lambda a,b,c,d: a * ((b / c) + d))
funcarr.append(lambda a,b,c,d: (a * b) / (c + d))
funcarr.append(lambda a,b,c,d: ((a * b) / c) + d)
funcarr.append(lambda a,b,c,d: a * (b / (c - d)))
funcarr.append(lambda a,b,c,d: a * ((b / c) - d))
funcarr.append(lambda a,b,c,d: (a * b) / (c - d))
funcarr.append(lambda a,b,c,d: ((a * b) / c) - d)
funcarr.append(lambda a,b,c,d: a * (b / (c * d)))
funcarr.append(lambda a,b,c,d: a * ((b / c) * d))
funcarr.append(lambda a,b,c,d: (a * b) / (c * d))
funcarr.append(lambda a,b,c,d: ((a * b) / c) * d)
funcarr.append(lambda a,b,c,d: a * (b / (c / d)))
funcarr.append(lambda a,b,c,d: a * ((b / c) / d))
funcarr.append(lambda a,b,c,d: (a * b) / (c / d))
funcarr.append(lambda a,b,c,d: ((a * b) / c) / d)
funcarr.append(lambda a,b,c,d: a / (b + (c + d)))
funcarr.append(lambda a,b,c,d: a / ((b + c) + d))
funcarr.append(lambda a,b,c,d: (a / b) + (c + d))
funcarr.append(lambda a,b,c,d: ((a / b) + c) + d)
funcarr.append(lambda a,b,c,d: a / (b + (c - d)))
funcarr.append(lambda a,b,c,d: a / ((b + c) - d))
funcarr.append(lambda a,b,c,d: (a / b) + (c - d))
funcarr.append(lambda a,b,c,d: ((a / b) + c) - d)
funcarr.append(lambda a,b,c,d: a / (b + (c * d)))
funcarr.append(lambda a,b,c,d: a / ((b + c) * d))
funcarr.append(lambda a,b,c,d: (a / b) + (c * d))
funcarr.append(lambda a,b,c,d: ((a / b) + c) * d)
funcarr.append(lambda a,b,c,d: a / (b + (c / d)))
funcarr.append(lambda a,b,c,d: a / ((b + c) / d))
funcarr.append(lambda a,b,c,d: (a / b) + (c / d))
funcarr.append(lambda a,b,c,d: ((a / b) + c) / d)
funcarr.append(lambda a,b,c,d: a / (b - (c + d)))
funcarr.append(lambda a,b,c,d: a / ((b - c) + d))
funcarr.append(lambda a,b,c,d: (a / b) - (c + d))
funcarr.append(lambda a,b,c,d: ((a / b) - c) + d)
funcarr.append(lambda a,b,c,d: a / (b - (c - d)))
funcarr.append(lambda a,b,c,d: a / ((b - c) - d))
funcarr.append(lambda a,b,c,d: (a / b) - (c - d))
funcarr.append(lambda a,b,c,d: ((a / b) - c) - d)
funcarr.append(lambda a,b,c,d: a / (b - (c * d)))
funcarr.append(lambda a,b,c,d: a / ((b - c) * d))
funcarr.append(lambda a,b,c,d: (a / b) - (c * d))
funcarr.append(lambda a,b,c,d: ((a / b) - c) * d)
funcarr.append(lambda a,b,c,d: a / (b - (c / d)))
funcarr.append(lambda a,b,c,d: a / ((b - c) / d))
funcarr.append(lambda a,b,c,d: (a / b) - (c / d))
funcarr.append(lambda a,b,c,d: ((a / b) - c) / d)
funcarr.append(lambda a,b,c,d: a / (b * (c + d)))
funcarr.append(lambda a,b,c,d: a / ((b * c) + d))
funcarr.append(lambda a,b,c,d: (a / b) * (c + d))
funcarr.append(lambda a,b,c,d: ((a / b) * c) + d)
funcarr.append(lambda a,b,c,d: a / (b * (c - d)))
funcarr.append(lambda a,b,c,d: a / ((b * c) - d))
funcarr.append(lambda a,b,c,d: (a / b) * (c - d))
funcarr.append(lambda a,b,c,d: ((a / b) * c) - d)
funcarr.append(lambda a,b,c,d: a / (b * (c * d)))
funcarr.append(lambda a,b,c,d: a / ((b * c) * d))
funcarr.append(lambda a,b,c,d: (a / b) * (c * d))
funcarr.append(lambda a,b,c,d: ((a / b) * c) * d)
funcarr.append(lambda a,b,c,d: a / (b * (c / d)))
funcarr.append(lambda a,b,c,d: a / ((b * c) / d))
funcarr.append(lambda a,b,c,d: (a / b) * (c / d))
funcarr.append(lambda a,b,c,d: ((a / b) * c) / d)
funcarr.append(lambda a,b,c,d: a / (b / (c + d)))
funcarr.append(lambda a,b,c,d: a / ((b / c) + d))
funcarr.append(lambda a,b,c,d: (a / b) / (c + d))
funcarr.append(lambda a,b,c,d: ((a / b) / c) + d)
funcarr.append(lambda a,b,c,d: a / (b / (c - d)))
funcarr.append(lambda a,b,c,d: a / ((b / c) - d))
funcarr.append(lambda a,b,c,d: (a / b) / (c - d))
funcarr.append(lambda a,b,c,d: ((a / b) / c) - d)
funcarr.append(lambda a,b,c,d: a / (b / (c * d)))
funcarr.append(lambda a,b,c,d: a / ((b / c) * d))
funcarr.append(lambda a,b,c,d: (a / b) / (c * d))
funcarr.append(lambda a,b,c,d: ((a / b) / c) * d)
funcarr.append(lambda a,b,c,d: a / (b / (c / d)))
funcarr.append(lambda a,b,c,d: a / ((b / c) / d))
funcarr.append(lambda a,b,c,d: (a / b) / (c / d))
funcarr.append(lambda a,b,c,d: ((a / b) / c) / d)

best = 0
bestvals = [-1,-1,-1,-1]
for subset in genset():
    poss = set([])
    for order in orderings(subset):
        for func in funcarr:
            try: val = func(*order)
            except ZeroDivisionError: continue
            ival = int(round(val))
            if val > 0 and abs(val-ival) < .01: poss.add(ival)
    for n in count(0):
        if not n+1 in poss: break
    if n > best:
        best = n
        bestvals = [str(int(val)) for val in subset]
print reduce(lambda x,y: x+y, bestvals)
