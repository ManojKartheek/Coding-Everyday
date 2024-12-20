# QUESTION : ----> 
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''


def sum_of_multiples(num):
    """
    Calculate the sum of all multiples of 3 or 5 below a given limit.
    """
    return sum(x for x in range(num) if x % 3 == 0 or x % 5 == 0)

# Call the function and print the result
num = 1000
result = sum_of_multiples(num)
print("The sum of all multiples of 3 or 5 below", num, "is:", result)

