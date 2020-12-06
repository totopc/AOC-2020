with open ('input5.txt','r' )as reader:
    rawList = [l for l in reader.read().split("\n")[:-1]]
    
#part 1
def seat_id(initialList):
    rowToBinary =initialList[:7].replace("F","0").replace("B","1")
    rowToDecimal = int(rowToBinary,2)
    
    columnToBinary=initialList[7:].replace("L","0").replace("R","1")
    columnToDecimal = int(columnToBinary,2)
    
    seat_id = rowToDecimal * 8 + columnToDecimal  
    
    return seat_id

#part 2
def missing_id(idList):
    for i in idList:
        if i+1 not in idList and i+2 in idList:
            return i+1
    
final_Id_List=[seat_id(seat) for seat in rawList]
print(max(final_Id_List))

print(missing_id(final_Id_List))
