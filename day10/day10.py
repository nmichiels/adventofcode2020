from itertools import combinations 
import numpy as np

data = np.loadtxt('input.txt', delimiter='\n', dtype=np.int64)

data = np.sort(data, axis=-1)



effective_jolts = 0
chain = []
differences = {1: 0, 2:0, 3:0}
for i, jolts in enumerate(data):
    if jolts <= effective_jolts + 3:
        differences[jolts-effective_jolts] += 1
        chain.append(jolts)
        effective_jolts = jolts
        
chain.append(jolts+3)
effective_jolts += 3
differences[3] += 1
   
print(chain)   
    

print("Result part 1: ", differences[1] * differences[3])


prev_jolt = 0
num_arrangements = 1
for i in range(len(chain)-1):
    if i+1 < len(chain) and chain[i+1] <= prev_jolt + 3:
        if i+2 < len(chain) and chain[i+2] <= prev_jolt + 3:
            num_arrangements *= 3  # both can be removed, so in total 3 combinations, not 4 because of the next iteration
            print(chain[i], chain[i+1])
        else:
            num_arrangements *= 2  #only this can be removed, so in total 2 combinations
            print(chain[i])
    prev_jolt = chain[i]
        

print(num_arrangements)
# effective_jolts = 0
# chain = []
# num_arrangements = 1
# for i, jolts in enumerate(data):
    # if jolts <= effective_jolts + 3:

        # if i+1 < len(data) and data[i+1] <= effective_jolts + 3:
            # num_arrangements *= 2 
        # if i+2 < len(data) and data[i+2] <= effective_jolts + 3:
            # num_arrangements *= 2 

        # chain.append(jolts)
        # effective_jolts = jolts
            
# print(num_arrangements)