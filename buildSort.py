import sys
import argparse
import os
import re


parser = argparse.ArgumentParser()
parser.add_argument('-path', help= 'please use args: -path PATH_TO_DMG_FILES')
args = parser.parse_args()



#if args.providername is None:
#    print ("Please supply a path to the build files as the first arg to the program")

buildPath = sys.argv[2]


fileList = os.listdir(buildPath)

pureVersionNumbers = []

#Remove upper and lowercase letters. Remove the "-"
for myfile in fileList:
    versionNumber = re.sub('[A-Za-z-]', '', myfile)
    if versionNumber.endswith('.'):
        versionNumber = versionNumber[:-1]
    pureVersionNumbers.append(versionNumber)
    
    
print "In Build File Directory: \n", buildPath, "\n\n"

print "Of these build files found:\n\n"
for myFile in fileList:
    print myFile
    
print "\n\n"
print "-------------------------------------"
    
#print fileList
#print pureVersionNumbers

# Audit version numbers
# 
validFile = []
validVersion = []
filePosition = -1
for version in pureVersionNumbers:
    skipFile =  False
    filePosition = filePosition + 1
    digit = version.split(".")
    digits = len(digit)
    #print digit
    skipFile =  False
    for i in range(0, digits):
        #print digit[i]
        if i == 0:
            if int(digit[i]) > 999:
                print "Error! Buildfile: ",fileList[filePosition]," is not a valid buildfile. Version number X.n.n exceeds alloowable 999 skipping..."
                skipFile = True
        if i == 1:
                if int(digit[i]) > 99:
                        print "Error! Buildfile: ", fileList[filePosition]," is not a valid buildfile. Version number n.X.n exceeds alloowable 99 skipping..."
                        skipFile = True
        if i == 2:
                if int(digit[i]) > 99:
                        print "Error! Buildfile: ", fileList[filePosition]," is not a valid buildfile. Version number n.n.X exceeds alloowable 99 skipping..."
                        skipFile = True
                        
    if skipFile == False:
        validFile.append(fileList[filePosition])
        validVersion.append(version)
        
#print "---------------------------------------------"
        
#print validFile
#print validVersion

# Build a list of integers representing value of build versioning.
#create a list
# example:
#Version 2.3.4 will be
#integer = 10**2 * 2 + 10**1 * 3 + 10**0 + 4


intList = []

for version in validVersion:
    digit = version.split(".")
    upper = len(digit)
    exp = 2
    num = 0
    for n in range(0, upper):
        num = num + 10**exp * int(digit[n])
        exp = exp - 1
    intList.append(num)
    
def bubblesort( A, BuildFiles ):
    for i in range( len( A ) ):
        for k in range( len( A ) - 1, i, -1 ):
            if ( A[k] < A[k - 1] ):
                swap( A, k, k - 1 )
                swap( BuildFiles, k, k - 1 )
 
def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
    
# The bubble sort will take the list of integers correspoinding to the calculated version integers and sort them.
# the list of valid file names is also sorted along with the integers. The integers are the "key" for sorting.
# The last element of the list is the highest number of the versioned file.
    
bubblesort( intList, validFile)

#print "++++++++++++++++++++++++++"
#print intList
#print validFile

print "\nThe highest VALID version build file is: ", validFile[-1]
    
        

        

