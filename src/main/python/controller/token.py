import os


def get_token(fileName):
    pathFile = ""
    file = open(os.path.join(pathFile, 'docs', fileName), 'r')
    token = file.readline()
    file.close()
    return token
