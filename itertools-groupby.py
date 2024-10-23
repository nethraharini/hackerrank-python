#compress the string!!
#using inbuilt function groupby we separate key and input and prints them, using join we finally join the len of list group and key,
#and we call the function in main function
from itertools import groupby

def compress_string(s):
    grouped = groupby(s)
    result = ' '.join(f"({len(list(group))}, {key})" for key, group in grouped)
    return result

if __name__ == '__main__':
    input_string = input().strip()  
    output = compress_string(input_string)  
    print(output) 

#input
#1222311
#ouput
#(1, 1) (3, 2) (1, 3) (2, 1)

