# Question: ------->>>>>>>>>
'''Write a Python program to generate all unique substrings of a given string.
Take a string as input.
Remove duplicate characters.
Generate and print all substrings in order of length.'''


# Input
input_string = input("Enter a string: ")

# Remove duplicate characters and sort them
unique_chars = ''.join(sorted(set(input_string)))

# Generate all substrings
substrings = []
for i in range(len(unique_chars)):
    for j in range(i + 1, len(unique_chars) + 1):
        substrings.append(unique_chars[i:j])

# Sort the substrings by length and alphabetically
sorted_substrings = sorted(substrings, key=lambda x: (len(x), x))

# Print the substrings
print("Unique substrings:")
for substring in sorted_substrings:
    print(substring)
print(f"Total No.of Strings are: {len(sorted_substrings)}")
