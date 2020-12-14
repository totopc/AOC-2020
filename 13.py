from functools import reduce
import math
import re

from collections import defaultdict 
with open ("input13.txt","r") as reader:
    raw= [l.replace('x','') for l in reader.read().split("\n") ]
with open ("input13.txt","r") as reader:   
    raw2= [l for l in reader.read().split("\n") ]

raw2=raw2[1].split(",")
raw2Num=set()
interval= defaultdict(list)

for value, inner in enumerate (raw2):
    if inner.isnumeric():
        if  int(value) !=0:
            interval[int(value)].append(int(inner))
            interval[int(value)].append(int(inner)-int(value))
            interval[int(value)].append(int(value))
            raw2Num.add(int(inner))
        else:
            interval[int(value)].append(int(inner))
            interval[int(value)].append(int(value))
            interval[int(value)].append(int(value))
            raw2Num.add(int(inner))

    
sched = defaultdict(list)
ref= base = ref2=int(raw[0])
buses = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?!\d)', (raw[1]))
buses = list(map(int, buses)) 
x=0
hiB= ref + max(buses)*2

while base < hiB:
    for bus in buses:
        if base%bus == 0:
            sched[base].append(bus)
    base+=1
while True:
    if ref in sched: 
        print("This is the bus",sched[ref],(ref),"time is to wait is",(ref-ref2) * (sched[ref][0]) )
        break 
    ref+=1

def inverse(num,val):
    while num > val:
        num = int(num % val)
    inversed = 0
    while int((num * inversed) % val) != 1:
        inversed +=1
    return inversed
num = reduce(lambda x,y: x*y,raw2Num)
final=0
for value,inner in  enumerate (interval):
    new_num= num // interval[inner][0]  
    inversed= inverse(new_num, interval[inner][0])
    final+= interval[inner][1]* inversed * new_num
    

print("This is the CRT Value", final%num)
