# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Calculate the sum of all multiples of 3 or 5 below 1000
sum_of_multiples = sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0)

# Print the result
print("The sum of all multiples of 3 or 5 below 1000 is:", sum_of_multiples)


# The OutPut will be : 233168