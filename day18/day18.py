import numpy as np
import time
# https://adventofcode.com/2020/day/18

file = open('input.txt', 'r')
lines = file.readlines()


        
      
def evaluate_expr_addition_first(subexpression):
    
    result = [np.sum(np.asarray(expr.split('+'), dtype=np.int64)) for expr in subexpression.split('*')] 
    result = np.prod(result)
    return result
    
    
def evaluate(expression, i):
    result = 0
    operator = None
    subexpression = ''
    while True:
        
        if i >= len(expression) or expression[i] == ')':
            return result, i+1, evaluate_expr_addition_first(subexpression)
            
        val = expression[i]
        
        if val == '+' or val == '*':
            operator = val
            i += 1
            subexpression = subexpression + operator
            continue

        
        if val.isnumeric() or val == '(':
            if val == '(':
                val, i, subexpression_rec = evaluate(expression, i+1)
                subexpression = subexpression + str(subexpression_rec)
            else:
                subexpression = subexpression + str(val)
                i += 1
             

            if operator == '+':
                result = result + int(val)
            elif operator == '*':
                result = result * int(val)
            else: 
                result = int(val)  #first digit

       


sum_part1 = 0
sum_part2 = 0
for expression in lines:
    expression = expression[:-1].replace(' ', '')
    result_part1,_, result_part2 = evaluate(expression, 0)
    sum_part1 += result_part1
    sum_part2 += result_part2

    
print("Result part 1: ", sum_part1)
print("Result part 2: ", sum_part2)



 