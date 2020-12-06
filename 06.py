with open ('input6.txt','r' ) as reader:
    decList = [l.replace('\n', '') for l in reader.read().split('\n\n') ] 
    
total = 0    
for i in decList:
    freq = set()
    for char in set(i):
        freq.add(char)
        

    my_list = list(freq)   
    total = total + (len(my_list))

    
print(total)
with open ('input6.txt','r' ) as reader:
    decList = [l for l in reader.read().split('\n\n') ] 
    
total = 0        
for i in decList:
    
    stringset= i.split()
    x= set.intersection(*map(set,stringset))
    my_list = list(x)
    total = total + (len(my_list))
    
    
print(total)
