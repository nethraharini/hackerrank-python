
n1 = int(input())
english_subscribers = set(map(int, input().split()))
n2 = int(input())
french_subscribers = set(map(int, input().split()))

total_subscribers = english_subscribers.union(french_subscribers)
print(len(total_subscribers))


#input
#9
#1 2 3 4 5 6 7 8 9
#9
#10 1 2 3 11 21 55 6 8

#output
#13
