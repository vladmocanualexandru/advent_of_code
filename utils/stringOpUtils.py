import hashlib

def getMD5Hash(string, number):
    return hashlib.md5(bytes('%s%s' % (string, number),'UTF-8')).hexdigest()