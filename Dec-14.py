# Question: ====>>>>>>
'''Write a Python program to find all numbers under 100,000 
where the sum of the factorial of their digits is equal to the number itself.
Print these numbers and their sum.'''


import math

# Initialize total_sum to hold the sum of all valid numbers
total_sum = 0

# Loop numbers from 10 to 100,000
for num in range(10, 100000):
    # Calculate the sum of the factorial of the digits
    digit_factorial_sum = sum(math.factorial(int(digit)) for digit in str(num))
    
    # Check if the sum of digit factorials equals the number
    if digit_factorial_sum == num:
        print(f"Found a number: {num}")
        total_sum += num

# Print the total sum of all numbers
print(f"Sum of all numbers: {total_sum}")
