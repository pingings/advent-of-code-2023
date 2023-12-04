test = open("../../testfiles/day4.txt",'r')

data = [row for row in test]
data = [[int(row.split(':')[0][5:])-1]+ [row.split(':')[1]] for row in data]
data = [[row[0]]+row[1].split('|') for row in data]

i = 0
while i < len(data):
    
    score = 0
    l = data[i][1].split()
    r = data[i][2].split()
    
    for n in l:
        if n in r:
            score += 1
  
    for j in range(score):
        data.append(data[data[i][0]+j+1])              
            
    i += 1
       
print(len(data))
