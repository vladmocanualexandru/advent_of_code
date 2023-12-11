from random import randrange

C_BLOCK = '█'
C_HORIZ_LINE = '─'
C_VERT_LINE = '│'
C_DOT_TRANSPARENT = '◌'
C_DOT_EMPTY = '○'
C_DOT_FULL = '●'
C_SE_CORNER = '┌'
C_SW_CORNER = '┐'
C_NE_CORNER = '└'
C_NW_CORNER = '┘'
C_NE_CORNER_DOUBLE = '╚'
C_NW_CORNER_DOUBLE = '╝'
C_SE_CORNER_DOUBLE = '╔'
C_SW_CORNER_DOUBLE = '╗'
C_HORIZ_LINE_DOUBLE = '═'
C_VERT_LINE_DOUBLE = '║'



def formatOutput(formatCode, *output):
    # return '\u001b[%dm%s\u001b[0m' % (formatCode, ' '.join([str(e) for e in output]))
    return '\u001b[%dm%s\u001b[0m' % (formatCode, ' '.join(str(e) for e in output))

def underline(*output):
    return formatOutput(4, *output)

def strikethrough(*output):
    return formatOutput(9, *output)

availableColorCodes = [1,31,32,33,34,35,36,90]
def color(*output):
    return formatOutput(availableColorCodes[randrange(len(availableColorCodes))], *output)

def light(*output):
    return formatOutput(1, *output)

def red(*output):
    return formatOutput(31, *output)

def green(*output):
    return formatOutput(32, *output)

def yellow(*output):
    return formatOutput(33, *output)

def blue(*output):
    return formatOutput(34, *output)

def purple(*output):
    return formatOutput(35, *output)

def cyan(*output):
    return formatOutput(36, *output)

def dark(*output):
    return formatOutput(90, *output)

def reverseColor(*output):
    return formatOutput(7, *output)

def redBG(*output):
    return formatOutput(41, *output)

def greenBG(*output):
    return formatOutput(42, *output)

def yellowBG(*output):
    return formatOutput(43, *output)

def blueBG(*output):
    return formatOutput(44, *output)

def purpleBG(*output):
    return formatOutput(45, *output)

def cyanBG(*output):
    return formatOutput(46, *output)