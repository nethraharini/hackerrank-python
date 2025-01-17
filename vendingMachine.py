#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self,num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price
        
    def buy(self, num_items, num_coins):
        # Check if the customer has enough coins and the machine has enough items
        if num_items > self.num_items:
            raise ValueError("Not enough items in the machine.")
        
        total_cost = num_items * self.item_price
        if num_coins < total_cost:
            raise ValueError("Not enough coins.")
        
        self.num_items -= num_items  # Decrease the available items in the machine
        change = num_coins - total_cost  # Calculate the change
        return change
    pass
if __name__ == '__main__':
    
    
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()



"""Input (stdin)
10 2
4
1 5
10 100
7 100
2 3
Your Output (stdout)
3
Not enough items in the machine.
86
Not enough coins.
"""

