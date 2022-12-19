import sys, os, math
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils, arrayUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *
 
EXPECTED_RESULT = 1886043

TARGET_THRESHOLD = 100000

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' ')
    
    df = pd.DataFrame([tuple[1:] if tuple[0]=='$' else tuple for tuple in raw[2:]], columns=["comm", "arg"])

    processed=df[df["comm"]!="ls"]

    return processed

def createNewFolder(name, root):
    return {"name":name, "root":root, "folders":{}, "files":{}}

def crawlAndGather(fs, basket):
    totalSize = sum([fs["files"][file] for file in fs["files"]])
    # log(fs["name"], totalSize)

    for folder in fs["folders"]:
        totalSize += crawlAndGather(fs["folders"][folder], basket)
    
    if totalSize <= TARGET_THRESHOLD:
        basket.append((fs["name"], totalSize))

    return totalSize

def solution(inputFile):
    cliLines = getInputData(inputFile)

    fs = createNewFolder("/", None)

    # build the filesystem
    for index, line in cliLines.iterrows():
        comm = line['comm']
        arg = line['arg']
        
        if comm == "dir" and not arg in fs["folders"]:
            fs["folders"][arg] = createNewFolder(arg, fs)
        elif comm.isnumeric() and not arg in fs["files"]:
            fs["files"][arg]=int(comm)
        elif comm == 'cd':
            if arg=="..":
                fs = fs["root"]
            else:
                fs = fs["folders"][arg]
        else:
            log(red('UNKNOWN COMMAND', comm, arg))

    # navigate to root folder
    while fs["root"] is not None:
        fs = fs["root"]

    # crawl fs and gather folder smaller than 100000
    basket = []
    crawlAndGather(fs, basket)

    # for entry in basket:
    #     log(entry)

    result=sum([entry[1] for entry in basket])

    return (result,EXPECTED_RESULT)