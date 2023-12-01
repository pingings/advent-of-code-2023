test = open("../../testfiles/day1.txt",'r')

total = 0
i = 0
j = 0

digits = ["one","two","three","four","five","six","seven","eight","nine"]
for row in test:
    
    r = []    
    for i in range(len(row)):
        
        # spelled numbers
        for j in range(i):
            if row[j:i+1] in digits:
                r.append(digits.index(row[j:i+1])+1)
                
                
        # number numbers
        if row[i].isdigit():
            r.append(int(row[i]))


    total += (10*r[0] + r[-1])

print(total)
 
            
       
