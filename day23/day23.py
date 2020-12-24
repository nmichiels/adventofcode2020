import numpy as np
import time
import re
# https://adventofcode.com/2020/day/23

cups = '215694783'
cups = [int(cup) for cup in list(cups)]

cups = cups + list(range(10,1000001))
num_cups = len(cups)
print(num_cups)
num_moves = 10000000



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
        self.tail = None
        
    def add_first(self, node):
        
        node.next = self.head
        if node.next is not None:
            node.next.prev = node
        else:
            self.tail = node
        self.head = node
        
    def print_reversed(self):
        node = self.tail
        nodes = []
        count = 0
        while node is not None and (count == 0 or node != self.tail):
            nodes.append(str(node.data))
            node = node.prev
            count += 1
        if node == self.tail:
            nodes.append("tail")
        else:
            nodes.append("None")
        print(" -> ".join(nodes))
        
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


pointers = {}
for i in reversed(range(len(cups))):
    node = Node(cups[i])
    llist.add_first(node)
    pointers[cups[i]] = node
    

# make circular
llist.tail.next = llist.head
llist.head.prev = llist.tail



start = time.time()
current = llist.head
for move in range(num_moves):
    
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
    destination = pointers[destination_val]
    # destination = current.prev
    # while destination.data != destination_val:
        # destination = destination.prev
    

    # remove pickuped cups
    pickup = current.next
    current.next.next.next.next.prev = current
    current.next = current.next.next.next.next
    
    
    # move picked upped cups just after destination
    pickup.next.next.next = destination.next
    destination.next.prev = pickup.next.next
    
    destination.next = pickup
    pickup.prev = destination
    
    # print(current.data, destination_val)
    # print(llist)
    current = current.next

end = time.time()


# get result part 1
labels = []
node = pointers[1].next
while node.data != 1:
    labels.append(str(node.data))
    node = node.next
print("Result part 1: ", "".join(labels))

# print(pointers[4013].next.data)
print(pointers[1].next.data, pointers[1].next.next.data)
print("Result part 2: ", pointers[1].next.data, '*', pointers[1].next.next.data, "=", pointers[1].next.data*pointers[1].next.next.data)
print(end-start)