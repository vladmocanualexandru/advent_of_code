import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    
    result = {}
    for tuple in getTuples_text(inputFile,  ' -> '):
        result[tuple[0]]=tuple[1]

    return result


def solution(inputFile):

    template = list('COPBCNPOBKCCFFBSVHKO')
    rules = getInputData(inputFile)
    
    # log(template, rules)

    steps = 10
    while steps>0:

        i=0
        while i< len(template)-1:
            ruleCandidate = '%s%s' % (template[i], template[i+1])
            if ruleCandidate in rules:
                template.insert(i+1,rules[ruleCandidate])
                i+=2
            else:
                i+=1

        steps-=1

    occurences = {}
    for c in template:
        if not c in occurences:
            occurences[c]=0
        
        occurences[c]+=1

    # log(occurences)
    
    occurencesArray = [(e, occurences[e]) for e in occurences]
    occurencesArray.sort(key = lambda e: (e[1]))

    # log(occurencesArray[0], occurencesArray[-1])

    return (occurencesArray[-1][1] - occurencesArray[0][1], 2602)