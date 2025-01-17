#!/bin/python3

import math
import os
import random
import re
import sys



class Item:
    # Implement the Item here
    def __init__(self,name,price):
        self.name = name
        self.price = price
    pass


class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self):
        self.items = []
    def add(self,item):
        self.items.append(item)
    def total(self):
        return sum(item.price for item in self.items)
    def __len__(self):
        return len(self.items)
    pass
if __name__ == '__main__':
    
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()


"""
Input (stdin)
2
bike 1000
headphones 100
8
total
add bike
len
total
add headphones
add headphones
len
total
Your Output (stdout)
0
1
1000
3
1200
"""
