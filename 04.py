#part1
import re
with open ('input4.txt', 'r') as reader:
    infoData= [l for l in reader.read().split('\n\n') ] 

data = ["byr","iyr","eyr","hgt", "hcl","ecl","pid"]
valid = 0
for line in infoData:
    for i in data:
        if i not in line:
            valid +=1
            
print("first " + str(valid))     
#part2

valid=0
for line in infoData:
    if "byr" in line and "iyr" in line and "eyr" in line and "hgt" in line and "hcl" in line and "ecl" in line and  "pid" in line:
        byr = int(line[int(line.find("byr:")+4):int(line.find("byr:")+8)])
        iyr = int(line[int(line.find("iyr:")+4):int(line.find("iyr:")+8)])
        eyr = int(line[int(line.find("eyr:")+4):int(line.find("eyr:")+8)]) 
        hgt = (line[int(line.find("hgt:")+4):int(line.find("hgt:")+9)])
        hcl = (line[int(line.find("hcl:")+4):int(line.find("hcl:")+12)])
        ecl = (line[int(line.find("ecl:")+4):int(line.find("ecl:")+8)])
        pid =  (line[int(line.find("pid:")+4):int(line.find("pid:")+14)])
        
        passCount = 0
        if  byr <=2002 and byr >=1920: 
            passCount +=1
        if iyr <=2020 and iyr >=2010:
            passCount +=1
        if eyr <=2030 and eyr >= 2020:
            passCount +=1
        if "cm" in hgt or "in" in hgt:            
            if "cm" in hgt:
                height = int(re.search(r'\d+', hgt)[0])
                if height >= 150 and height <= 193:
                    passCount +=1
            if "in" in hgt:
                height = int(re.search(r'\d+', hgt)[0])
                if height >= 59 and height <=76:
                    passCount +=1
        
        if "#" in hcl:
            if len((line[int(line.find("hcl:#")+5):int(line.find("hcl:#")+11)])) == 6:
                checkThis = line[int(line.find("hcl:#")+5):int(line.find("hcl:#")+11)]
                pattern = re.compile("[a-f0-9]+")
                if bool(pattern.fullmatch(checkThis)) is True:
                    passCount +=1
                    
        if "amb" in ecl or "blu" in ecl or "brn" in ecl or  "gry" in ecl or "grn" in ecl or "hzl" in ecl or "oth" in ecl:
            passCount +=1
            
        if len(pid.strip()) == 9:
            passCount +=1
        
        if passCount == 7:
            valid+=1
print("final " + str(valid))           
            
            
