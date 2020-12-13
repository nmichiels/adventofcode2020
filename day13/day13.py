import numpy as np
import time
# https://adventofcode.com/2020/day/13



start = time.time()

file = open('input.txt', 'r')
data = file.readlines()

timestamp = int(data[0][:-1])
print(timestamp)

buses = np.asarray(data[1].replace(',x', '').split(','), dtype=int)

fractions = np.modf(timestamp /  buses)[0]
timestamps = np.modf(timestamp /  buses)[1]
next_bus = np.argmax(fractions)
time_stamp_next_bus = int(timestamps[next_bus] + 1) * buses[next_bus]

end = time.time()

print("Result part 1: ", (time_stamp_next_bus-timestamp) * buses[next_bus])




# part 2

buses = np.asarray(data[1].replace(',x', ',-1').split(','), dtype=np.int64)
offsets = np.arange(len(buses), dtype=np.int64)

offsets= offsets[buses>0]
buses = buses[buses>0]


factor = buses[0]
timestamp = 0
for i in range(1,len(buses)):
    bus = buses[i]
    offset = offsets[i]
    while True:
        if (timestamp + offset ) % bus == 0:
            factor *= bus
            break
        
        timestamp += factor

print("Result part 2: ", timestamp)
print(end-start)


# solveset(
# sol = solve([t/bus] )
# print(sol)

# print(offsets)
# for bus in buses:

# 

# print(np.mod(timestamp,buses))
# print(timestamp / buses)
# print(np.argmax(timestamp / buses))

