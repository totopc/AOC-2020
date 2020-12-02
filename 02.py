fake = 0
passed = 0
with open('input2.txt','r') as reader:
    for line in reader.read().strip().split('\n'):
        lowerbound = int(line[0:line.find('-')])
        upperbound = int(line[line.find('-')+1:line.find(' ')])
        charcheck = line[line.find(' ')+1: line.find(':')]
        strcheck = line[line.find(':')+2:]

        fake += lowerbound <= strcheck.count(charcheck) <= upperbound
        passed += (strcheck[lowerbound-1] == charcheck) ^ (strcheck[upperbound-1]==charcheck)

print ("this is a fake total valid " + str(fake))
print ("this is a true total valid " + str(passed))

