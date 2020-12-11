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

prev_results = {}
def get_arrangements(chain, i, prev_jolt):
    if i+1 < len(chain):
        total_arrangements = 0
        
        if "(%d,%d)"%(i+1, chain[i]) in prev_results:   
            total_arrangements += prev_results["(%d,%d)"%(i+1, chain[i])]
        else:
            arrangements = get_arrangements(chain, i+1, chain[i])
            prev_results["(%d,%d)"%(i+1, chain[i])] = arrangements
            total_arrangements += arrangements
    
        if chain[i+1] <= prev_jolt + 3:
            if "(%d,%d)"%(i+1, prev_jolt) in prev_results:
                total_arrangements += prev_results["(%d,%d)"%(i+1, prev_jolt)]
            else:
                arrangements = get_arrangements(chain, i+1, prev_jolt)
                prev_results["(%d,%d)"%(i+1, prev_jolt)] = arrangements
                total_arrangements += arrangements
        return total_arrangements
            
    return 1
    


num_arrangements = get_arrangements(chain, 0, 0)
print("Result part 1: ",num_arrangements)
