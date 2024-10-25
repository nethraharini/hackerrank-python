#idea is to use combinations function and print set of characters combined in set of respcted length

from itertools import combinations
user_input = (input())
string_part, number_part = user_input.split()
number_part= int(number_part)
sorted_string = ''.join(sorted(string_part))


for i in range(1, number_part+1 ):     # Outer loop we set lenght frok 1 to 2 so it prints ACHK. 
    combo = combinations(sorted_string, i)
    for c in combo:                     # Inner loop ,we join the combination of length 2 prints the folllowing output
        print(''.join(c))


#input
#HACK 2
#output
#A
#C
#H
#K
#AC
#AH
#AK
#CH
#CK
#HK
