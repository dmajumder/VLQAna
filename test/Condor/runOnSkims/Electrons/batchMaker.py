import sys, math, os, re
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')
options.register('Path', '',
                VarParsing.multiplicity.singleton,
                VarParsing.varType.string,
                "path to store"
)
options.parseArguments()

PATH = options.Path
print PATH

toMake = ['ttbar', 'dy_ht100-200', 'dy_ht200-400', 'dy_ht400-600', 'dy_ht600-Inf', 'bprime800','bprime1000', 'bprime1200', 'tprime800', 'tprime1000', 'tprime1200', 'muons', 'electrons', 'WW', 'WZto2', 'WZto3', 'ZZto2', 'ZZto4']
for n in toMake:
    inputFile = open('batchDummy.py')
    outputFile = open('batch_'+str(n)+'.jdl', 'w')
    if n == 'ttbar':
        QUEUE = '4653'
    if n == 'dy_ht100-200':
        QUEUE = '66'
    if n == 'dy_ht200-400':
        QUEUE = '23'
    if n == 'dy_ht400-600':
        QUEUE = '26'
    if n == 'dy_ht600-Inf':
        QUEUE = '23'
    if n == 'tprime800':
        QUEUE = '17'
    if n == 'tprime1000':
        QUEUE = '18'
    if n == 'tprime1200':
        QUEUE = '19'
    if n == 'bprime800':
        QUEUE = '18'
    if n == 'bprime1000':
        QUEUE = '18'
    if n == 'bprime1200':
        QUEUE = '19'
    if n == 'muons':
        QUEUE = '6641'
    if n == 'electrons':
        QUEUE = '6639'
    if n == 'WW':
        QUEUE='51'
    if n == 'ZZto4':
        QUEUE='264'
    if n == 'ZZto2':
        QUEUE='226'
    if n == 'WZto2':
        QUEUE='700'
    if n == 'WZto3':
        QUEUE='46'

    EXE = 'run_'+n+'.sh'

    for line in inputFile:
        line = line.replace('queue', QUEUE)
        line = line.replace('path', PATH+'/'+n)
        line = line.replace('exe', EXE)
        outputFile.writelines(line)
    inputFile.close()
    outputFile.close()

