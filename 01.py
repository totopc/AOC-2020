from itertools import combinations_with_replacement
import math 
with open('input.txt', 'r') as reader:
    myList=[int(l) for l in reader.read().split()]

n=2
n2=3

def sumTwo(listName):
    for number in combinations_with_replacement (listName[::-1], n):
  
        if sum(number) == 2020:
            results =math.prod(number[::-1])
            return results
        
def sumThree(listName):
    for number in combinations_with_replacement(listName[::-1],n2):
        if sum(number)==2020:
            results=math.prod(number[::-1])
            return results
       
print (sumTwo(myList))
print (sumThree(myList))



