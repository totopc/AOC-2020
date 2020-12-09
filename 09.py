with open ('input9.txt', 'r') as reader:
    numberList = [l for l in reader.read().split('\n')]

def errCheck(nL):
    preList = []
    checker=[]
    counter = 0
    for n in nL:
        if counter <= 26:
            preList.append(n)
        if counter >= 26:
            preList[counter%26]=n
            for x in preList:
                for y in preList:  
                    if int(x)+int(y)==int(n) and  preList.index(x)!=preList.index(y):
                        if n not in checker:
                            checker.append(n)
                        break
        counter+=1
    q= 26 
    set1 = set(nL[q:])
    set2= set(checker)
    return(set1-set2) 


invalid=int(min(errCheck(numberList)))
print(invalid) 

def contagion(nL):
    x=0
    pointer=0
    sumSet=[]
    while x+pointer < len(nL):
        sumSet.append(nL[x+pointer])
        sumCheck=sum(set(map(int, sumSet)))
        sMin=min(set(map(int, sumSet)))
        sMax=max(set(map(int, sumSet)))
        if sumCheck > invalid:
            sumSet=[]
            x=0
            pointer+=1
        if sumCheck == invalid:
            return (sMin+sMax)
            break
        x+=1
print(contagion(numberList))
    

