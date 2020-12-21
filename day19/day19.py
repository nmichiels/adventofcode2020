import numpy as np
import time
import re
# https://adventofcode.com/2020/day/19



def build_regex(rule_id, rules):
    rule = rules[rule_id]
    if rule[0] == 'a' or rule[0] == 'b':
        return rule[0]
        
    
    
    reg = ''
    # find loop
    loop = False
    for r in rule:
        if r != '|' and int(r) == rule_id:
            loop = True
            break
            
    if loop:
        print("loop detected", rule)
        if len(rule) < 5:
            reg += '(?:' + build_regex(int(rule[0]), rules) + ')'
            reg += '+'
        else:
            reg += '(' + build_regex(int(rule[0]), rules) + '(?1)?' + build_regex(int(rule[1]), rules) + ')'
        
    else:
        reg += '(?:(?:'
        for r in rule:
            if r == '|':
                reg += ')|(?:'
                pass
            else:
                reg += build_regex(int(r), rules)
                
        reg += '))'
    
    return reg

def load_data():
    file = open('input.txt', 'r')
    lines = file.readlines()
    data = " ".join([line for line in lines]) 

    # data = data.split('your ticket:\n ')
    data = data.split('\n \n ')
    
    rules_data = data[0].split('\n ')
    
    rules = {}
    for rule in rules_data:
        rule = rule.split(': ')
        
        rule_id = int(rule[0])
        rule = rule[1].replace('\"', '').split(' ')
        rules[rule_id] = rule
        
    # print(rules)    
        
    messages = data[1].split('\n ')
        
    return rules, messages
    

    

rules, messages = load_data()

#part 1
reg_ex = build_regex(0, rules)
num_matching = 0
for message in messages:
    if re.fullmatch(reg_ex, message):
        num_matching += 1
        
print("Result part 1: ", num_matching)



rules[8] = ['42', '|', '42', '8']
rules[11] = ['42', '31', '|', '42', '11', '31']
reg_ex = build_regex(0, rules)
reg_ex = '^' + reg_ex + '$'

text_file = open("regex.txt", "w")
text_file.write(reg_ex)
text_file.close()


# print(reg_ex)

print("Result part 2: ", 424)   
print("Evaluate regex on : https://regex101.com/r/17ZPnv/1")




