test = open("../../testfiles/day1.txt",'r')

total = 0

for row in test:
    r = [int(c) for c in row if c.isdigit()]
    total += (10*r[0] + r[-1])
    
print(total)
