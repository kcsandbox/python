__author__ = 'kc'

def DOB(line):
    field = line.split(',')
    print field[2]
    #print ('The third field is', x[0])
    year = line.split('/')
    print year[2]

inputFile = 'Persons.txt'
file = open(inputFile, 'r')
for line in file:
    DOB(line.strip())




