fp1 = open('input.txt','r')
fp2 = open('mot.txt','r')
fp3 = open('pot.txt','r')
fp4 = open('st.txt','w+')

inputfile = fp1.read().splitlines()
mot = fp2.read().splitlines()
pot = fp3.read().splitlines()
lc = 0

for block in inputfile:
    print (block)
    if block.find('START') != -1:
        print (block.find('START'))
        lc = int(block[block.find('START')+6:block.find('START')+10])
        print ("lc is ",lc)

for block in inputfile:
    if block.find('USING')!=-1:
        lc+= 4
    elif block.find('L')!=-1:
        lc+= 5
    elif block.find('A')!=-1:
        lc+= 6
    elif block.find('ST')!=-1:
        lc+= 7
    elif block.find('DC')!=-1:
        fp4.write(block[0:block.find('DC')]+str(lc)+'\n')
        lc+= 2
    elif block.find('DS')!=-1:
        fp4.write(block[0:block.find('DS')]+str(lc)+'\n')
        lc+= 2
    elif block.find('END')!=-1:
        break
print("Pass 1 successful")