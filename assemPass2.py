import assemPass1 as ap
import sys

with open(sys.argv[1],'r') as f:
    contents = f.read().splitlines()

sTable = ap.stateTable(contents)
MOT = {'A':'01','L':'02','ST':'03'}
POT = {'DS':'01','DC':'02','START':'03','USING':'04','END':'05'}
print ("State Table ",sTable)
print ("MOT ",MOT)
print ("POT ",POT)

newContents = []

for x,lines in enumerate(contents):
    print (lines)
    for y,words in enumerate(lines.split(' ')):
        #print (words)
        for keyM,valM in MOT.items():
            if keyM == words:
                newContents.append(lines.replace(keyM,MOT[keyM]))
        for keyP,valP in POT.items():
            if keyP == words:
                newContents.append(lines.replace(keyP,POT[keyP]))
        for keyS,valS in sTable.items():
            if keyS == words:
                newContents.append(lines.replace(keyS,sTable[keyS]))

#print(newContents)

for lines in newContents:
    print (lines)
