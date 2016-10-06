import sys, math, os, re
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')
options.register('pyInput', '',
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "path to read config"
)
options.register('output', '', 
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "path to output"
)
options.register('test', '', 
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "path to test directory"
)
options.parseArguments()

pyInput = options.pyInput
output = options.output
test = options.test

toMake = ['ttbar', 'dy_ht100-200', 'dy_ht200-400', 'dy_ht400-600', 'dy_ht600-Inf', 'bprime', 'tprime', 'muons', 'electrons','WW', 'WZto2', 'WZto3', 'ZZto2', 'ZZto4']

for n in toMake:
    inputFile = open('runDummy.py')
    outputFile = open('run_'+str(n)+'.sh', 'w')
    for line in inputFile:
        line = line.replace('SAMPLE', n)
        line = line.replace('PYTHON', pyInput)
        line = line.replace('OUTPUT', output)
        line = line.replace('TEST', test)
        outputFile.writelines(line)
    inputFile.close()
    outputFile.close()
