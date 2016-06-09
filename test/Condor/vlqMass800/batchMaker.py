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

toMake = ['ttbar', 'dy_ht100-200', 'dy_ht200-400', 'dy_ht400-600', 'dy_ht600-Inf', 'bprime', 'tprime', 'muons', 'electrons']
for n in toMake:
    inputFile = open('batchDummy.py')
    outputFile = open(str(n)+'.jdl', 'w')
    if n == 'ttbar':
        QUEUE = '4653'
        EXE = 'run_'+n+'.sh'
    if n == 'dy_ht100-200':
        QUEUE = '66'
        EXE = 'run_'+n+'.sh'
    if n == 'dy_ht200-400':
        QUEUE = '23'
        EXE = 'run_'+n+'.sh'
    if n == 'dy_ht400-600':
        QUEUE = '26'
        EXE = 'run_'+n+'.sh'
    if n == 'dy_ht600-Inf':
        QUEUE = '23'
        EXE = 'run_'+n+'.sh'
    if n == 'tprime':
        QUEUE = '17'
        EXE = 'run_'+n+'.sh'
    if n == 'bprime':
        QUEUE = '18'
        EXE = 'run_'+n+'.sh'
    if n == 'muons':
        QUEUE = '6641'
        EXE = 'run_'+n+'.sh'
    if n == 'electrons':
        QUEUE = '6639'
        EXE = 'run_'+n+'.sh'

    for line in inputFile:
        line = line.replace('queue', QUEUE)
        line = line.replace('path', PATH)
        line = line.replace('exe', EXE)
        outputFile.writelines(line)
    inputFile.close()
    outputFile.close()

