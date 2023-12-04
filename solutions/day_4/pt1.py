test = open("../../testfiles/day4.txt",'r')

total = 0

data = [row for row in test]
data = [row.split(':')[1] for row in data]
data = [row.split('|') for row in data]

for row in data:
    
    score = 0
    l = row[0].split()
    r = row[1].split()
    
    for n in l:
        if n in r:
            score += 1
     
    if score > 0:
        total += 2**(score-1)


print(total)
