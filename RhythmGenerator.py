#A program used to find every possible matching rhythm
#Written by Cameron Yeomans for Linear Algebra at the University of Utah 2019

import re
regex = "^[\+|\-]+$"

print("Rhythm builder")
print("use + to enter an eigth note")
print("use - to enter an eigth rest")
print("input must be 8 chars or less and contain only the chars + and -")

error = True

while(error):
    searchRhythm = raw_input("Enter a valid rhythm: ")
    valid = re.search(regex, searchRhythm)
    if(len(searchRhythm) < 9 and valid):
        error = False
    if(searchRhythm == ""):
        break


rhythmsInBinary = []

binaryVal =""
for x in range(256):
    binaryVal = str(bin(x)[2:])
    while(len(binaryVal)!= 8):
        binaryVal = "0" + binaryVal
        
    match = True
    for y in range(len(searchRhythm)):
        if((searchRhythm[y] == "+" and binaryVal[y] == "0") or (searchRhythm[y] == "-" and binaryVal[y] == "1")):
            match = False
    if(match):        
        rhythmsInBinary.append(binaryVal)
    match = True


print(rhythmsInBinary)

rhythmString = ""
lilyPondString = ""
lilyPondArray = []
for i in range(len(rhythmsInBinary)):
    rhythmString = rhythmsInBinary[i]
    for j in range(len(rhythmString)):
        if(rhythmString[j] == "0"):
            lilyPondString = lilyPondString + "r8 "
        else:
            lilyPondString = lilyPondString + "b8 "
    
    lilyPondArray.append(lilyPondString)
    lilyPondString = ""
print(lilyPondArray[0])


#writes to ly file to be compiled into sheet music
outfile = open('Rhythms.ly','w')

#format syntax 
outfile.write("\\header{\n")
outfile.write("\ttitle = \"Rhythmic Combinations\"\n")
outfile.write("}\n")
outfile.write("\\relative c'' {\n")

for i in range(len(lilyPondArray)):
    outfile.write(lilyPondArray[i]+"\n")

outfile.write("}")

outfile.close()

