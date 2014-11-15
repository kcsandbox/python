__author__ = 'kc'
inputFile = '../data/fb_friends_raw.txt'
file = open(inputFile, 'r')
for line in file:
    print line.strip()
