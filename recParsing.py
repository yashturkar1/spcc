# E -> TE'
# E'-> +TE'|e
# T -> FT'
# T'-> *FT'|e
# F -> (E) |id
def Error(flag):
    print("Error Occurred")
    flag[1] = 1
    return flag

def E(Str,l):
     #print("E1 ",l[0])
     l=T(Str,l) 
     #print("E2 ",l[0])
     l=Ed(Str,l)
     #print("E3 ",l[0])
     return l
     

def T(Str,l):
    #print("T1 ",l[0])
    l=F(Str,l)
    #print("T2 ",l[0])
    l=Td(Str,l)
    #print("T3 ",l[0])
    return l

def Ed(Str,l):
    if Str[l[0]] == '+':
        l[0] += 1
        #print("Ed1 ",l[0])
        l=T(Str,l)
        #print("Ed2 ",l[0])
        l=Ed(Str,l)
    return l

def Td(Str,l):
    #print('Td')
    if Str[l[0]] == '*':
        l[0] += 1
        #print("Td1 ",l[0])
        l=F(Str,l)
        #print("Td2 ",l[0])
        l=Td(Str,l)
    return l
        
def F(Str,l):
    if Str[l[0]] == '(':
        l[0] += 1
        #print("F1 ",l[0])
        l=E(Str,l)
        #print("F2 ",l[0])
        if Str[l[0]] == ')':
            l[0] += 1
            #print(l[0])
        else:
            l=Error(l)
            
    elif Str[l[0]] == 'd':
        l[0] += 1
        #print("F3 ",l[0])
    else:
        Error(l)
    return l

string = input("Input String Please: ") + '$'
l = [0,0]
l=E(string,l)
if l[1] == 0:
    print(string + " is Valid")
else:
    print(string+" is Invalid")


'''sayali@sayali:~/Desktop$ python3 recParsing.py
Input String Please: d+d
d+d$ is Valid
*************************************************
sayali@sayali:~/Desktop$ python3 recParsing.py
Input String Please: d*d+d
d*d+d$ is Valid
*************************************************
sayali@sayali:~/Desktop$ python3 recParsing.py
Input String Please: d+
Error Occurred
d+$ is Invalid
**************************************************
sayali@sayali:~/Desktop$ python3 recParsing.py
Input String Please: d*(d+d)
d*(d+d)$ is Valid
sayali@sayali:~/Desktop$ 
'''