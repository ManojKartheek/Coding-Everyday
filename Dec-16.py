'''Question: Find Maximum Product of Two Numbers
Write a Python program
to find the maximum product of any two numbers in a given list.'''


# Input: List of integers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Check if the list has fewer than 2 numbers
if len(numbers) < 2:
    print("Need at least two numbers to find a product.")
else:
    # Sort the numbers
    numbers.sort()

    # Maximum product can be:
    # - Product of the two largest positive numbers
    # - Product of the two smallest negative numbers
    max_product = max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

    # Output the result
    print(f"Maximum product is: {max_product}")
