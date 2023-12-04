test = open("../../testfiles/day3.txt",'r')

gears = {}
parts_sum = 0
symbols = ['#','$','+','*','&','=','@','%','/','-']
data = []
for row in test.readlines():
    data.append(row)
    
for row_num in range(len(data)):
    
    curr_num = ''
    for char_num in range(len(data[row_num])):
        
        if data[row_num][char_num].isdigit():
            curr_num += data[row_num][char_num]
        else:
            if curr_num != '':
                
                is_part_num = False
                is_gear = False
                gear_pos = []
                # check for adjacent symbol
                if data[row_num][char_num] in symbols:
                    is_part_num = True
                    if data[row_num][char_num] == '*':
                        gear_pos = [row_num, char_num]
                        is_gear = True      
                
                try:
                    if data[row_num][char_num-len(curr_num)-1] in symbols:
                        is_part_num = True
                        if data[row_num][char_num-len(curr_num)-1] == '*':
                            gear_pos = [row_num, char_num-len(curr_num)-1]
                            is_gear = True
                except IndexError: pass
                
                try:
                    for i in range(len(curr_num)+2):
                        if data[row_num-1][char_num-len(curr_num)-1+i] in symbols:
                            is_part_num = True
                            if data[row_num-1][char_num-len(curr_num)-1+i] == '*':
                                gear_pos = [row_num-1, char_num-len(curr_num)-1+i]
                                is_gear = True
                except IndexError: pass
                
                try:
                    for i in range(len(curr_num)+2):
                        if data[row_num+1][char_num-len(curr_num)-1+i] in symbols:
                            is_part_num = True
                            if data[row_num+1][char_num-len(curr_num)-1+i] == '*':
                                is_gear = True
                                gear_pos = [row_num+1, char_num-len(curr_num)-1+i]
                except IndexError: pass
                
                if is_part_num:
                    parts_sum += int(curr_num)
                if is_gear:
                    if (gear_pos[0], gear_pos[1]) in gears:
                        gears[(gear_pos[0], gear_pos[1])].append(int(curr_num))
                    else:
                        gears[(gear_pos[0], gear_pos[1])] = [int(curr_num)]
                    
                is_gear = False    
                is_part_num = False
                curr_num = ''

gear_sum = 0
for gear in gears:
    if len(gears[gear]) == 2:
        gear_sum += gears[gear][0] * gears[gear][1]
print(gear_sum)
print(parts_sum)

