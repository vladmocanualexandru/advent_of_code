def decrypt(numberTuples, key, mixCount, refValue, index0,  index1,  index2):
    numberTuples = [(t[0]*key,t[1]) for t in numberTuples]

    refTuple = None
    initialOrderNumbers = numberTuples + []
    
    for mcIndex in range(mixCount):
        for tuple in initialOrderNumbers:
            number = tuple[0]
            currentPos = numberTuples.index(tuple)
            del numberTuples[currentPos]

            oldLeft = (currentPos-1)%len(numberTuples)
            oldRight = currentPos

            newLeft = (oldLeft+number)%len(numberTuples)
            newRight = (oldRight+number)%len(numberTuples)

            if newRight>newLeft:
                numberTuples = numberTuples[:newLeft+1]+[tuple]+numberTuples[newRight:]
            else:
                numberTuples = numberTuples + [tuple]

            if refTuple == None and number == refValue:
                refTuple = tuple

    indexRef = numberTuples.index(refTuple)

    gpsValue0 = numberTuples[(indexRef+index0)%len(numberTuples)][0]
    gpsValue1 = numberTuples[(indexRef+index1)%len(numberTuples)][0]
    gpsValue2 = numberTuples[(indexRef+index2)%len(numberTuples)][0]

    return gpsValue0+gpsValue1+gpsValue2