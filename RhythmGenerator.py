

rhythmsInBinary = []

binaryVal =""
for x in range(256):
    binaryVal = str(bin(x)[2:])
    while(len(binaryVal)!= 8):
        binaryVal = "0" + binaryVal
    rhythmsInBinary.append(binaryVal)


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

