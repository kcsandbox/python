__author__ = 'kc'


def getfriends(inputFile):
    i = 0
    file = open(inputFile, 'r')
    for line in file:
        #if len(line) >1 :
        #if line.strip():
         #   if 'friend' not in line.strip().lower():
        if ((line.strip()) and ('friend' not in line.strip().lower()) and ('message' not in line.strip().lower())):
            i= i+1
            print line.strip()

    print 'Number of friends you have',i


#=========== main  ===========

rawinput = '../data/fb_friends_raw.txt'

getfriends(rawinput)