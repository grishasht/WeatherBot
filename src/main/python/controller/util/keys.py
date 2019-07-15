def get_key(filePath):
    file = open(filePath, 'r')
    key = file.readline()
    file.close()
    return key
