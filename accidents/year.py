__author__ = 'kc'
print 'Hello World'

fileName = './testinput.txt'

file = open(fileName, 'r')

newfile = open("newFile.txt", "w") # A new file is created with name newfile.txt
newfile.write("hello World\n")


for line in file:
    year = line.split("/") # Split the value of year only.
   # print year[2].strip()
    if (int(year[2].strip()) > 2009): # converting a string to integer.
        print line.strip() # Removing any additional spaces.
        newfile.write(line) # Writes the above result to the newFile.txt
newfile.close()








