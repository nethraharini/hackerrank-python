def average(array):
    
    arraylist = set(array)
    sum1 = (sum(arraylist))
    total  = (len(arraylist))
    average = sum1/total
  
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#input
#10
#161 182 161 154 176 170 167 171 170 174
#Output 
#169.375
