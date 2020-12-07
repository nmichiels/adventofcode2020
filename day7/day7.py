import numpy as np
import re

# https://adventofcode.com/2020/day/7


file = open('input.txt', 'r')
lines = file.readlines()

rules = {}
for sentence in lines:

	source_bag = re.findall(r"^[a-z]+ [a-z]+",sentence)[0]
	results = re.findall(r"[0-9]* [a-z]+ [a-z]+ bag[s]?",sentence)

	
	bags = []
	
	if results[0] != ' no other bags':
		for result in results:
			number = int(re.findall(r"\d",result)[0])
			color = re.findall(r"[a-z]+ [a-z]+",result)[0]
			bags.append((color, number))
			
	rules[source_bag] = bags
	
		
		
target_color = 'shiny gold'

found_colors = {}

for source_bag, target_bags in rules.items():
	queue = []
	queue = queue + target_bags

	while len(queue) is not 0:
		bag = queue.pop(0)
		# print(bag)
		if bag[0] == target_color:
			found_colors[source_bag] = True
			break
		else:
			queue = queue + rules[bag[0]]
	
	
print("Result part 1: ", len(found_colors))	
	

def count_bags(bag, count):
	print(bag)
	total = 0
	total += bag[1]*count
	for child_bag in rules[bag[0]]:
		total += count_bags(child_bag, count*bag[1])
		
	return total
		
total = count_bags((target_color,1), 1) -1 # minus one to remove the shiny gold itself
print("Result part 2: ", total)			
			
