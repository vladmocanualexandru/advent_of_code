import sys, os

sys.path.append(os.path.abspath(os.path.join('../..')))

from utils import matrixUtils
from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
 

def getInputData(inputFile):
    raw = getText(inputFile)

    conversions = ['0000',
        '0001',
        '0010',
        '0011',
        '0100',
        '0101',
        '0110',
        '0111',
        '1000',
        '1001',
        '1010',
        '1011',
        '1100',
        '1101',
        '1110',
        '1111']

    rawBin = []

    for d in raw:
        rawBin.append(conversions[int(d, 16)])

    return ''.join(rawBin)

def extractPackets(type, argument, payload):
    result = []

    if type == 1:
        for i in range(argument):
            p = Packet(payload)
            result.append(p)
            payload = payload[p.length:]
    else:
        while argument>0:
            p = Packet(payload)
            result.append(p)
            argument-= p.length
            payload=payload[p.length:]

    return result


class Packet:
    version=None
    type=None
    payload=None
    value=None
    lengthTypeId=None
    packetsLength=None
    pachetsCount=None
    innerPackets=[]
    length=6

    def __init__(self, bits):
        self.version=int(bits[:3],2)
        self.type=int(bits[3:6],2)

        if self.type == 4:
            parseIndex=6
            foundLast=False
            payloadParts = []

            while(not foundLast):
                if bits[parseIndex]=='0':
                    foundLast = True
                
                payloadParts.append(bits[parseIndex+1:parseIndex+5])
                parseIndex+=5

                self.length+=5

            self.payload = ''.join(payloadParts)
            self.value = int(self.payload, 2)
        else:
            self.lengthTypeId = int(bits[6])

            if self.lengthTypeId == 0:
                self.packetsLength = int(bits[7:22],2)
                self.payload = bits[22:]
                self.length+=16
                self.innerPackets = extractPackets(self.lengthTypeId, self.packetsLength, self.payload)
            else:
                self.pachetsCount = int(bits[7:18],2)
                self.payload = bits[18:]
                self.length+=12
                self.innerPackets = extractPackets(self.lengthTypeId, self.pachetsCount, self.payload)

            sum = 0
            prod = 1
            min = 999999
            max = -1
            for p in self.innerPackets:
                self.length+=p.length
                sum+=p.value
                prod*=p.value
                if p.value<min:
                    min = p.value
                if p.value>max:
                    max = p.value

            if self.type==0:
                self.value = sum
            elif self.type==1:
                self.value = prod
            elif self.type==2:
                self.value = min
            elif self.type==3:
                self.value = max
            elif self.type==5:
                self.value = 1 if self.innerPackets[0].value>self.innerPackets[1].value else 0
            elif self.type==6:
                self.value = 1 if self.innerPackets[1].value>self.innerPackets[0].value else 0
            elif self.type==7:
                self.value = 1 if self.innerPackets[1].value==self.innerPackets[0].value else 0



    def __str__(self):
        return 'v=%s, t=%s, p=%s, val=%s, ltid=%s, plen=%s, pcnt=%s, packets=[%s], len=%s' % (
            self.version, self.type, self.payload, self.value, self.lengthTypeId,
            self.packetsLength, self.pachetsCount, len(self.innerPackets), self.length)


def solution(inputFile):
    def calculateVersionSum(packet):
        result = packet.version

        for p in packet.innerPackets:
            result += calculateVersionSum(p)

        return result

    inputData = getInputData(inputFile)
    # log(len(inputData))
    
    rootPacket = Packet(inputData)

    # log('root',rootPacket)

    return (rootPacket.value,246225449979)