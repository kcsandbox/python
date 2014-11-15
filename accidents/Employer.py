__author__ = 'kc'

fileName = './Employeedetails.csv'

file = open(fileName, 'r')

newfile = open("newEmpFile.txt", "w") # A new file is created with name newfile.txt
newfile.write("Name, DOB and profession details of employee as below.\n")


for line in file:
    stripline=line.strip() # to remove the newline character at the end of the lines and storing it into a variable.
    fields = stripline.split(',') #
    #if(len(fields) == 5):

    #print fields[0],fields[1],fields[2],fields[4]
    #DMY = fields[2].split("/") # Split the value of year only.
    #print DMY[2].strip()
    newfile.write(fields[0] + ',' + fields[1] +','+ fields[2]+','+ fields[4]+'\n')
    #print (fields[0] + ',' + fields[1] +','+ fields[2]+','+ fields[4])
   # print[1:2]
    #if (int(year[2].strip()) > 2009): # converting a string to integer.
        #print line.strip() # Removing any additional spaces.
        #newfile.write(line) # Writes the above result to the newFile.txt
newfile.close()
