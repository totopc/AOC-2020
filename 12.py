# Part 2
from collections import defaultdict
with open("input12_test.txt", "r") as reader:
    course = [l for l in reader.read().split("\n")]
    

news = defaultdict(list)


# if any((c in chars) for c in s):
#     print('Found')
# else:
#     print('Not Found')
def manDis(cL):
    fwrd="E"
    base = 90
    for x in cL:
        drct = set('NEWS')

        nose= x[0:1]
        step=int(x[1:])

        if any((d in drct ) for d in x):
            if nose == "N":
                news['x'].append(int(step))
            if nose == "S":
                news['x'].append(int("-"+str(step)))
            if nose == "E":
                news['y'].append(int(step))
            if nose == "W":
                news['y'].append(int("-"+str(step)))
                

        if nose == "L" or nose =="R":
            if "L" in x:
                base = base - int(step)
            if "R" in x:
                base = base + int(step)
            if base%360 == 0:
                fwrd="N"
            if base%360 == 90:
                fwrd360="E"
            if base%360 == 180:
                fwrd="S"
            if base%360 == 270:
                fwrd="W"
        if nose == "F":
            if fwrd == "N":
                news['x'].append(int(step))
            if fwrd == "S":
                news['x'].append(int("-"+str(step)))
            if fwrd == "E":
                news['y'].append(int(step))
            if fwrd == "W":
                news['y'].append(int("-"+str(step)))
            

        
    manDist= abs(sum(news['x']))+abs(sum(news['y']))  
    return manDist

        
        

print(manDis(course))

# Part 2
    
from collections import defaultdict
with open("input12.txt", "r") as reader:
    course = [l for l in reader.read().split("\n")]
    

news = defaultdict(list)
def manDis(cL):
    fwrd="E"
    
    news['point'].extend((10, 1))
    news['ship'].extend((0, 0))

    for x in cL:
        drct = set('NEWS')
        nose= x[0:1]
        step=int(x[1:])
        pNS=news['point'][1]
        pEW=news['point'][0]
        sNS=news['ship'][1]
        sEW=news['ship'][0]
        if any((d in drct ) for d in x):
            if nose == "N":
                news['point'][1]= pNS + step
            if nose == "S":
                news['point'][1]= pNS - step
            if nose == "E":
                news['point'][0]= pEW + step
            if nose == "W":
                news['point'][0]= pEW - step

        if nose == "L" or nose =="R":
            rot = step// 90
            if nose == "L":
                for x in range (rot):
                    news['point'][0] = -pNS
                    news['point'][1] = pEW
                    pNS=news['point'][1]
                    pEW=news['point'][0]
            if nose == "R":
                for x in range (rot):
                    news['point'][0] = pNS
                    news['point'][1] = -pEW
                    pNS=news['point'][1]
                    pEW=news['point'][0]

        if nose == "F":
            news['ship'][1]=pNS * step + sNS
            news['ship'][0]=pEW * step + sEW
        
    manDist= abs(news['ship'][0])+ abs(news['ship'][1])  

    
    return manDist


print(manDis(course))


    








