def getRawText(filename):
    fileData = open(filename, 'r')

    return fileData.read()

def getText(filename):
    return getRawText(filename).strip()

def getRawLines(filename):
    fileData = open(filename, 'r')

    return fileData.readlines()


def getStrings(filename):
    rawLines = getRawLines(filename)
    result = []

    for line in rawLines:
        result.append(line.strip())
    
    return result

def getNumbers_dec(filename):
    rawLines = getRawLines(filename)
    result = []

    for line in rawLines:
        result.append(int(line))
    
    return result

def getTuples_text(filename, *separators):
    if len(separators)==0:
        separators = [' ']

    result = []
    
    for text in getStrings(filename):
        if separators[0] == '':
            result.append(list(text))
        else:
            result.append(text.split(separators[0]))

    for separator in separators[1:]:
        newResult = []
        for entry in result:
            newEntry = []

            for text in entry:
                newEntry += text.split(separator)

            newResult.append(newEntry)

        result = newResult
    
    return result

def getTuples_numbers(filename, *separators):

    stringTuples = getTuples_text(filename, *separators)
    result = []

    for tuple in stringTuples:
        entry = []
        for element in tuple:
            try:
                entry.append(int(element))
            except:
                try:
                    entry.append(float(element))
                except:
                    entry.append(None)

        result.append(entry)
        
    return result


