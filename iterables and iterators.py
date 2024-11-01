def probability_of_a(n, letters, k):
    # Count occurrences of 'a'
    count_a = letters.count('a')
    
    # Total combinations of selecting k indices from n
    total_combinations = comb(n, k)
    
    # If there are no 'a's, the probability is 0
    if count_a == 0:
        return 0.0000
    
    # Calculate combinations without 'a'
    combinations_without_a = comb(n - count_a, k) if n - count_a >= k else 0
    
    # Probability that at least one selected index contains 'a'
    probability = 1 - (combinations_without_a / total_combinations)
    
    return round(probability, 4)

if __name__ == "__main__":
    n = int(input())  # Length of the list
    letters = input().split()  # List of letters
    k = int(input())  # Number of indices to select
    
    result = probability_of_a(n, letters, k)
    print(result)  # Output the result
#input
#4 
#a a c d
#2
#output
#0.8333

