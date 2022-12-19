import math

def formatElapsedMsConsole(ms):
    s = math.floor(ms/1000)%60
    m = math.floor(ms/1000/60)%60
    h = math.floor(ms/1000/3600)
    ms %= 1000

    return '|{:02d}|{:02d}|{:02d}|{:03d}|'.format(h,m,s,ms)


def formatElapsedMsHuman(ms):
    s = math.floor(ms/1000)%60
    m = math.floor(ms/1000/60)%60
    h = math.floor(ms/1000/3600)
    ms %= 1000

    labels = []

    if h>0:
        labels.append('%dh'%h)
    
    if m>0:
        labels.append('%dm'%m)

    if s>=2:
        labels.append('%ds'%s)
    elif s>=0:
        ms+=s*1000

    labels.append('%dms'%ms)

    return "{:>18s}".format(','.join(labels))