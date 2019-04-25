import os

files = os.listdir('.')

mactemp = []

for direc in files:
    if direc[-4:] == '.asm':
        print ("Found file "+direc)
        with open(direc,'r') as f:
            contents = f.read().splitlines()
        for x,lines in enumerate(contents):
            #print (x,lines)
            y = x
            if lines.find() == 'MACRO':
                print ("Found at ",x)
                y += 1
                print(contents[y])
            if lines[0:4] != 'MEND':
                break
            mactemp.append(contents[y])

print ("mactemp is ",mactemp)