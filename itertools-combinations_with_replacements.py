#to sorted the combinations 
from itertools import combinations_with_replacement
data = (input().strip())
s,n = data.split()
n = int(n)
combinations_result = combinations_with_replacement(sorted(s),n)
for combo in combinations_result:
    print(''.join(combo))



#input:
#HACK 2

#output:
#AA
#AC
#AH
#AK
#CC
#CH
#CK
#HH
#HK
#KK


