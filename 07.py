import collections
with open ('input7.txt','r' ) as reader:
    bagInfo = [l.replace('contain ', ':') for l in reader.read().split('\n') ] 
    
setChildBag = collections.defaultdict(set)
setMasterBag= collections.defaultdict(list)
contains_gold = set()

for i in bagInfo:
    masterBag = i[0:i.find(":")-6]
    childBag = i[i.find(":")+1:]
    childBag = childBag.split(", ")
    setMasterBag[masterBag]=[]
    for bags in childBag:
        if bags[0:1].isnumeric():
            setMasterBag[masterBag].append((int(bags[0:1]),bags[2:bags.find("bag")-1]))
            setChildBag[bags[2:bags.find(" bag")]].add(masterBag)

def getGoldBag(gold):
    for gold in setChildBag[gold]:
        contains_gold.add(gold)
        getColor(gold)
        
sg = "shiny gold"
getGoldBag(sg)  

print(len(contains_gold))


def bagCount(color):
    total=0
    for value,inner in setMasterBag[color]:
        total += value * (1+bagCount(inner))
    return total

print(bagCount("shiny gold"))

