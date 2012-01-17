#!/usr/bin/python

import numpy

NUM_NAMES = 10
startingSyllables = ['ju', 'jun']
middleSyllables = ['', 'cell']
endingSyllables = ['ex', 'eo']


for i in range(NUM_NAMES):
    startIndex = numpy.random.randint(0, len(startingSyllables))
    middleIndex = numpy.random.randint(0, len(middleSyllables))
    endIndex = numpy.random.randint(0, len(startingSyllables))
    name = startingSyllables[startIndex] + middleSyllables[middleIndex] + endingSyllables[endIndex]
    print name

try:
    input('press any key to quit')
except:
    None
