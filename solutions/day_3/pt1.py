test = open("../../testfiles/day3.txt",'r')

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
                # check for adjacent symbol
                if data[row_num][char_num] in symbols:
                    is_part_num = True
                
                try:
                    if data[row_num][char_num-len(curr_num)-1] in symbols:
                        is_part_num = True
                except IndexError: pass
                
                try:
                    for i in range(len(curr_num)+2):
                        if data[row_num-1][char_num-len(curr_num)-1+i] in symbols:
                            is_part_num = True
                except IndexError: pass
                
                try:
                    for i in range(len(curr_num)+2):
                        if data[row_num+1][char_num-len(curr_num)-1+i] in symbols:
                            is_part_num = True
                except IndexError: pass
                
                if is_part_num:
                    parts_sum += int(curr_num)
                    
                is_part_num = False
                curr_num = ''


print(parts_sum)

