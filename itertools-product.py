#using product function, in this code we split two input A, B and product them, 
#later we print the output using join and str(item) to avoid excessive brackets.
from itertools import product
A = list(map(int,input().split()))
B = list(map(int,input().split()))
multiply = product(A,B)
print(' '.join(str(item) for item in multiply))


#input:
#1 2
#3 4
#output
#(1, 3) (1, 4) (2, 3) (2, 4)
