#To permutte the input and join both sorted string_part and number part as length
from itertools import permutations
user_input = (input())
string_part, number_part = user_input.split()
number_part= int(number_part)
sorted_string = ''.join(sorted(string_part))
permutated_string = list(permutations(sorted_string,number_part))
for perm in permutated_string:
    print(''.join(perm))


#input
#HACK 2
#output
#AC
#AH
#AK
#CA
#CH
#CK
#HA
#HC
#HK
#KA
#KC
#KH
