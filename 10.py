import collections
with open('input10.txt','r') as reader:
    adaptors=sorted(set(int(l) for l in reader.read().split('\n') if l !=""))
    adapterSet =  collections.defaultdict(set)
def sortAdaptors(aL):
    b=0
    x=0
    for a in aL:
        if a == 1:
            adapterSet[1].add(a)
            b=a 
        if a-b == 1:
            adapterSet[1].add(a)
            b=a
        if a-b == 2:
            adapterSet[2].add(a)
            b=a
        if a-b == 3:
            adapterSet[3].add(a)
            b=a
        if x == len(aL)-1:
            adapterSet[3].add(a+3)
        x+=1
    return (len(adapterSet[1])*len(adapterSet[3]))
    
def daWei(aL):
    aU = aL[1].union(aL[3])
    aU.add(0)
    aU = list(aU)
    arrWays = [1]+[0]*(len(aU)-1)
    for indx, values in enumerate(aU):
        for j in range(indx-3, indx):
            if(values-aU[j]<=3):
                arrWays[indx]= arrWays[indx] + arrWays[j]
    return arrWays[-1]
print(sortAdaptors(adaptors))
print(daWei(adapterSet))




