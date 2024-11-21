
asize = input()
set1 = set(map(int, input().split()))
bsize = input()
set2 = set(map(int, input().split()))

result = set1 ^ set2 #
sorted_list = sorted(result)

print("\n".join(map(str, sorted_list)))

#input
#4
#2 4 5 9
#4
#2 4 11 12
# Output
#5
#9
#11
#12
