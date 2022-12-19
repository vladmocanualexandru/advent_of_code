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
 
EXPECTED_RESULT = 3842121

TOTAL_CAPACITY = 70000000
UPDATE_SIZE = 30000000

def getInputData(inputFile):
    raw = getTuples_text(inputFile, ' ')
    
    df = pd.DataFrame([tuple[1:] if tuple[0]=='$' else tuple for tuple in raw[2:]], columns=["comm", "arg"])

    processed=df[df["comm"]!="ls"]

    return processed

def createNewFolder(name, root):
    return {"name":name, "root":root, "folders":{}, "files":{}}

def crawlAndGather(fs, basket):
    totalSize = sum([fs["files"][file] for file in fs["files"]])

    for folder in fs["folders"]:
        totalSize += crawlAndGather(fs["folders"][folder], basket)

    basket.append([fs["name"], totalSize])
    
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

    sizeDf = pd.DataFrame(basket, columns=["folder","size"]).set_index(["folder"]).sort_values(by="size")

    availableSpace = TOTAL_CAPACITY - sizeDf.loc["/"]["size"]
    requiredSpace = UPDATE_SIZE - availableSpace

    result = sizeDf[sizeDf["size"]>requiredSpace].head(1)["size"][0]

    return (result,EXPECTED_RESULT)