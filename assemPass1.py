import sys

with open(sys.argv[1],'r') as f:
    contents = f.read().splitlines()

#print (contents)

def stateTable(contents):

    count = 0

    sTable = []

    for lines in contents:
        #print (lines)
        if lines.find('START') != -1:
            count = int(lines[lines.find('START')+6:lines.find('START')+10])
            #print (count)
        elif lines.find('USING') != -1:
            count += 3
        elif lines.find('L') != -1:
            count += 4
        elif lines.find('A') != -1:
            count += 3
        elif lines.find('ST') != -1:
            count += 3
        elif lines.find('DC') != -1:
            sTable.append([lines[0:lines.find('DC')],count])
            count += 2
        elif lines.find('DS') != -1:
            sTable.append([lines[0:lines.find('DS')],count])
            count += 2
        elif lines.find('END') != -1:
            break

    #print (sTable)
    State_Table = {}
    for state in sTable:
        State_Table.update({state[0]:state[1]})
    return State_Table

stateTable(contents)