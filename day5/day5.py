import numpy as np
import re

# https://adventofcode.com/2020/day/5






def decode(bp, seats):
    
    
    # decode row
    row_range = np.arange(128)
    for i in range(7):
        half = int(len(row_range) / 2)
        if bp[i] == 'F':
            row_range = row_range[:half]
        elif bp[i] == 'B':
            row_range = row_range[half:]
        else:
            print("error")
            
        # print(bp[i], row_range)
    row = row_range[0]
        
    # decode col    
    col_range = np.arange(8)
    for i in range(7,10):
        half = int(len(col_range) / 2)
        if bp[i] == 'L':
            col_range = col_range[:half]
        elif bp[i] == 'R':
            col_range = col_range[half:]
        else:
            print("error")
            
        # print(bp[i], col_range)
    col = col_range[0]
    seat_id = row * 8 + col
        
    
    return row, col, seat_id
    
    


file = open('input.txt', 'r')
lines = file.readlines()

seats = np.ones((128,8), dtype='uint8') * -1
print(seats.shape)
highest_seat_id = 0
for bp in lines:
    row, col, seat_id = decode(bp, seats)
    seats[row,col] = seat_id
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id
    

        
        
print("Result part 1: highest seat id: ", highest_seat_id)


print("Part 2: ")
for row in range(128):
    for col in range(8):
        print('{:3d} '.format(seats[row,col]), end='')
    print('')
    



