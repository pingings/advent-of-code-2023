test = open("../../testfiles/day2.txt",'r')

roundsSum = 0
limits = {'r':12,'g':13,'b':14}

for row in test:

    game = row.split(":")
    roundNum = int(game[0].split(' ')[1])
    
    game = game[1]
    game = game.replace(';',',')
    game = game.replace(' ','')
    game = game.split(',')
    
    draws = []
    for draw in game:
        for i in reversed(range(len(draw))):
            if draw[i].isdigit():
                draws.append(draw[:i+2])
                break
    
    possible = True
    for draw in draws:
        if limits[draw[-1]] < int(draw[:-1]):
            possible = False
            break
    
    if possible:
        roundsSum += roundNum
    
print(roundsSum)
