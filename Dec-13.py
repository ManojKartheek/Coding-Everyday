def optimized_even_fibonacci_sum(limit):
    # Starting with the first three Fibonacci numbers where the third is even
    a, b, c = 1, 1, 2  # F(n-2), F(n-1), F(n) where F(n) is even
    total = 0
    
    while c <= limit:
        total += c  # Add the even Fibonacci number to the sum
        # Generate the next even Fibonacci number directly
        a, b, c = b + c, c + (b + c), a + 2 * (b + c)
    
    return total

# Limit of 4 million as per the problem
limit = 4000000
result = optimized_even_fibonacci_sum(limit)
print("The sum of even-valued terms is:", result)
