import numpy as np
import time
import re
# https://adventofcode.com/2020/day/23

cups = '389125467'
cups = [int(cup) for cup in list(cups)]

# cups = cups + list(range(10,1000001))
num_cups = len(cups)
print(num_cups)
num_moves = 100



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def __repr__(self):
        return self.data

        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_first(self, node):
        
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
    
    def __repr__(self):
        node = self.head
        nodes = []
        count = 0
        while node is not None and (count == 0 or node != self.head):
            nodes.append(str(node.data))
            node = node.next
            count += 1
        if node == self.head:
            nodes.append("head")
        else:
            nodes.append("None")
        return " -> ".join(nodes)
    
llist = LinkedList()


last = None
for i in reversed(range(len(cups))):
    node = Node(cups[i])
    if i == (len(cups) -1):
        last = node
    llist.add_first(node)

# make circular
last.next = llist.head
llist.head.prev = last


start = time.time()
current = llist.head
for move in range(num_moves):
    
    if move % 100 == 0:
        print(move)
    # find destination
    steps = 0
    destination_val = current.data - 1
    if destination_val == 0:
        destination_val += num_cups
    # destination val cannot be any of the next three (picked upped) cups
    while destination_val == current.next.data or destination_val == current.next.next.data or destination_val == current.next.next.next.data:
        destination_val -= 1
        if destination_val == 0:
            destination_val += num_cups
        
    # find destination node
    destination = current.next.next.next.next
    while destination.data != destination_val:
        destination = destination.next
    
        
    # remove pickuped cups
    pickup = current.next
    current.next = current.next.next.next.next
    
    # move picked upped cups just after destination
    pickup.next.next.next = destination.next
    destination.next = pickup
    
    # print(current.data, destination_val)
    # print(llist)
    current = current.next

end = time.time()


# set cup before the cup with value 1 as head node
node = llist.head
while node.next.data != 1:
    node = node.next
llist.head = node

# get result part 1
labels = []
node = llist.head.next.next
while node.data != 1:
    labels.append(str(node.data))
    node = node.next
print("Result part 1: ", "".join(labels))
print("Result part 2: ", llist.head.data, '*', llist.head.next.next.data, "=", llist.head.data*llist.head.next.next.data)
print(end-start)