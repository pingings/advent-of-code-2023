test = open("../../testfiles/day2.txt",'r')

roundsSum = 0
limits = {'r':12,'g':13,'b':14}

for row in test:
    print("------")
    game = row.split(":")
    roundNum = int(game[0].split(' ')[1])
    
    game = game[1]
    game = game.replace(';',',')
    game = game.replace(' ','')
    game = game.split(',')
    
    draws = []
    mins = {'r':0,'g':0,'b':0}
    for draw in game:
        for i in reversed(range(len(draw))):
            if draw[i].isdigit():
                draws.append(draw[:i+2])
                break
    
    for d in draws:
        print(d)
        if int(d[:-1]) > mins[d[-1]]:
            print("!")
            mins[d[-1]] = int(d[:-1])
    
    roundsSum += (mins['r'] * mins['g'] * mins['b'])

print(roundsSum)
            
    
