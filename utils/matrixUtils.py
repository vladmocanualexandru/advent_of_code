from numpy import mat

def log(matrix, logFunc, separator='', highlightElem=(lambda e: str(e))):
    for line in matrix:
        logFunc(separator.join([highlightElem(e) for e in line]))

def find(matrix, transformLogic=None, returnCondition=lambda e : True):
    returnCoords = []

    for li in range(len(matrix)):
        for ci in range(len(matrix[li])):
            if transformLogic is not None:
                matrix[li][ci] = transformLogic(matrix[li][ci])

            if returnCondition(matrix[li][ci]):
                returnCoords.append((li,ci))

    return returnCoords

def apply(matrix, applyLogic):
    appliedMatrix = generate(len(matrix), len(matrix[0]))

    for li in range(len(matrix)):
        for ci in range(len(matrix[li])):
            appliedMatrix[li][ci] = applyLogic(matrix[li][ci])
            
    return appliedMatrix

def wrap(matrix, wrapMaterial, times=1):
    result = []

    result.append([(wrapMaterial() if callable(wrapMaterial) else wrapMaterial) for i in range(len(matrix[0])+2)])

    for line in matrix:
        newLine  = [(wrapMaterial() if callable(wrapMaterial) else wrapMaterial)] + line + [(wrapMaterial() if callable(wrapMaterial) else wrapMaterial)]
        result.append(newLine)

    result.append([(wrapMaterial() if callable(wrapMaterial) else wrapMaterial) for i in range(len(matrix[0])+2)])

    if times>1:
        result = wrap(result, lambda : wrapMaterial() if callable(wrapMaterial) else wrapMaterial, times-1)

    return result

def trim(matrix, times=1):
    result = []

    for line in matrix[times:len(matrix)-times]:
        result.append(line[times:len(line)-times])

    return result

def addAll(matrix, eIsRelevant=lambda e : True, map=lambda e: e):
    return sum( sum(map(e) for e in line if eIsRelevant(e)) for line in matrix)  

def generate(lines, cols, value=0):
    return [[(value() if callable(value) else value) for i in range(cols)] for j in range(lines)]

def setAreaToValue(matrix, startLine, startCol, endLine, endCol, value):
    for lineI in range(startLine, endLine):
        for colI in range(startCol, endCol):
            matrix[lineI][colI] = value


def getNeighbors4(matrix, y, x, includeRef=False, radius=1, includeNeighborCoords=False):
    result = []

    yValues = range(max(y-radius, 0),min(y+radius+1,len(matrix)))

    for neighY in yValues:

        xValues = [x]
        if neighY == y:
            xValues = range(max(x-radius, 0),min(x+radius+1,len(matrix[0])))
            
        for neighX in xValues:
            if includeRef or (not neighY == y or not neighX == x):
                neighbor = matrix[neighY][neighX]

                if includeNeighborCoords:
                    neighbor = (neighbor, (neighY, neighX))

                result.append(neighbor)

    return result

def getNeighbors8(matrix, y, x, includeRef=False, radius=1, includeNeighborCoords=False):
    result = []

    neighYRange = range(max(y-radius, 0),min(y+radius+1,len(matrix)))
    neighXRange = range(max(x-radius, 0),min(x+radius+1,len(matrix[0])))

    for neighY in neighYRange:
        for neighX in neighXRange:
            if includeRef or (not neighY == y or not neighX == x):
                neighbor = matrix[neighY][neighX]

                if includeNeighborCoords:
                    neighbor = (neighbor, (neighY, neighX))

                result.append(neighbor)

    return result

def flipMainDiagonal(matrix):
    flippedMatrix = generate(len(matrix[0]), len(matrix), None)

    for lineIndex in range(len(matrix)):
        for colIndex in range(len(matrix[0])):
            flippedMatrix[colIndex][lineIndex] = matrix[lineIndex][colIndex]

    return flippedMatrix

def flipHorizontal(matrix):
    flippedMatrix = []
    
    for line in matrix:
        flippedMatrix.append(line[::-1])

    return flippedMatrix

def flipVertical(matrix):
    flippedMatrix = []
    
    for line in matrix[::-1]:
        flippedMatrix.append(line)

    return flippedMatrix

def rotate(matrix, times=1, cw=True):
    times = times % 4

    for timeIndex in range(times):
        rotatedMatrix = []
        if cw:
            for colIndex in range(len(matrix[0])):
                newRow = []
                for lineIndex in range(len(matrix)-1,-1,-1):
                    newRow.append(matrix[lineIndex][colIndex])

                rotatedMatrix.append(newRow)
        else:
            for colIndex in range(len(matrix[0])-1, -1, -1):
                newRow = []
                for lineIndex in range(len(matrix)):
                    newRow.append(matrix[lineIndex][colIndex])

                rotatedMatrix.append(newRow)

        matrix=rotatedMatrix

    return matrix

def agg(matrix, f):
    return f([f(row) for row in matrix])
