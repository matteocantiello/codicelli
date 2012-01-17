#!/usr/bin/python

import numpy

NUM_NAMES = 10000
startingSyllables = ['sel','ly','ky','swe','gre','']
middleSyllables = ['','le','be','re','el','or']
endingSyllables = ['ex', 'eo', 'ix', 'share', 'sh', 'io', 'exp', 'ect','eed','res','ect','ly','']

names = []
for i in startingSyllables:
    for j in middleSyllables:
        for k in endingSyllables:
            names.append(i+j+k)

names = string.join(names,'\n')

f = open('urls.txt','w')
f.write(names)
f.close()

#for i in range(NUM_NAMES):
#    startIndex = numpy.random.randint(0, len(startingSyllables))
#    middleIndex = numpy.random.randint(0, len(middleSyllables))
#    endIndex = numpy.random.randint(0, len(startingSyllables))
#    name = startingSyllables[startIndex] + middleSyllables[middleIndex] + endingSyllables[endIndex]
#    print name

# try:
#    input('press any key to quit')
# except:
#    None
