
with open ('input8.txt','r') as reader: 
    bootCode  = [l for l in reader.read().split('\n')]
    
#Part 1
def noLooping(yourList):
    acc=0
    i=0
    ran=[]
    
    while i < len(yourList):
        b=yourList[i]
        if (b+str(i)) in ran:
            break;
        ran.append(b + str(i))
        if "acc" in b:
            op = b[b.find(' ')+1:b.find(' ')+2]
            num = int(b[b.find(' ')+2:])
            if op == "+":
                acc = acc + num
            elif op == "-":            
                acc = acc - num
        if "jmp" in b:
            op = b[b.find(' ')+1:b.find(' ')+2]
            num = int(b[b.find(' ')+2:])
            if op == "+":
                i = i + num-1
            if op == "-":
                i = i - num-1
        i += 1
    return(acc)

#Part 2
def switcheroo(baseList):
    i=0
    ran=[]
    while i < len(baseList):
        with open ('input8.txt','r') as reader: 
            yourList  = [l for l in reader.read().split('\n')]
        iRow=yourList[i]
        childRan=[]
        acc=0         
        if "nop" in iRow and 0 != int(iRow[iRow.find(' ')+2:]) and  (iRow+str(i)) not in ran:
            ran.append(iRow +":"+str(i))
            yourList[i] = 'jmp ' + iRow[iRow.find(' ')+1:] 
            
        if "jmp" in iRow and 0 != int(iRow[iRow.find(' ')+2:]) and  (iRow+str(i)) not in ran: 
            ran.append(iRow + str(i))
            yourList[i]= 'nop ' + iRow[iRow.find(' ')+1:] 
        #Loop
        q=0
        while q < len(yourList):
            b=yourList[q]

            if (b+str(q)) in childRan:
                break;
            childRan.append(b + str(q))
            if "acc" in b:
                op = b[b.find(' ')+1:b.find(' ')+2]
                num = int(b[b.find(' ')+2:])
                if op == "+":
                    acc = acc + num
                elif op == "-":            
                    acc = acc - num
            if "jmp" in b:
                op = b[b.find(' ')+1:b.find(' ')+2]
                num = int(b[b.find(' ')+2:])
                if op == "+":
                    q = q + num-1
                if op == "-":
                    q = q - num-1
            q += 1
            if q == len(yourList):
                return(acc)
        i += 1
     
    
print(noLooping(bootCode))
print(switcheroo(bootCode))   


    
