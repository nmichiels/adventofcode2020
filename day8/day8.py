import numpy as np
from enum import IntEnum 
import copy

# https://adventofcode.com/2020/day/8

# class Operation(IntEnum):
    # acc = 0
    # jmp = 1
    # nop = 2

class Instruction():
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument
        self.count = 0
        
    
        

def load_instructions():
    
    file = open('input.txt', 'r')
    lines = file.readlines()
    
    instructions = []
    for i, instruction in enumerate(lines):
        ins = instruction[:-1].split(' ')
        # print(instruction[:-1])
        instructions.append(Instruction(ins[0],int(ins[1])))
        # instructions.append([ins[0],int(ins[1]),0])
        # operator = -1
        # if ins[0] == 'acc':
            # operator = Operation.acc
        # elif ins[0] == 'jmp':
            # operator = Operation.jmp
        # elif ins[0] == 'nop':
            # operator = Operation.nop
        # else:
            # print('Unknown operator')
            
            
        
    return instructions
  



def print_instructions(instructions):
    for i in range(len(instructions)):
        print(i, instructions[i].operation, instructions[i].argument)
        
        
# returns if terminated and accumulator
def run(instructions):
    instructions = copy.deepcopy(instructions)
    acc = 0
    pc = 0
    while True:
        # print(pc)
        if pc > len(instructions)-1:
            return True, acc
        instruction = instructions[pc]
        
        
        # loop detection
        if instruction.count > 0: 
            return False, acc
            
        # print(pc, instruction.operation, instruction.argument)
        if instruction.operation == 'acc':
            acc += instruction.argument
            pc += 1
        elif instruction.operation == 'jmp':
            pc += instruction.argument
        elif instruction.operation == 'nop':
            pc += 1
        else:
            print('Error: unknown operator', instruction.operation)
            
        instruction.count += 1
        
def find_corruption(instructions):

    
    for i in range(len(instructions)):
        altered_instructions = copy.deepcopy(instructions)

        terminated = False
        if altered_instructions[i].operation == 'nop':
            altered_instructions[i].operation = 'jmp'
            terminated, acc =  run(altered_instructions)
        elif altered_instructions[i].operation == 'jmp':
            altered_instructions[i].operation = 'nop'
            terminated, acc =  run(altered_instructions)


        if terminated:
            return acc
            
    return None

        
instructions = load_instructions()
terminated, acc =  run(instructions)
print('Result part 1: ', acc)


print('Result part 2: ', find_corruption(instructions))

