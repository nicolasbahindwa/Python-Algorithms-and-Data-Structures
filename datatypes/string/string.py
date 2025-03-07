"""
Python Strings: A Comprehensive Guide with Time Complexity
----------------------------------------------------------

This document explains the various operations, use cases, and time complexities
of Python strings with practical examples.
"""

# 1. Basic String Creation and Access
print("\n--- 1. BASIC STRING OPERATIONS ---")

# Creating strings - O(n) where n is the length of the string
empty_string = ""  # O(1)
simple_string = "Hello"  # O(5) = O(n)
multi_line_string = """This is
a multi-line
string."""  # O(25) = O(n)

print(f"Empty string: {empty_string}")
print(f"Simple string: {simple_string}")
print(f"Multi-line string: {multi_line_string}")

# Accessing characters - O(1)
print(f"First character: {simple_string[0]}")  # O(1)
print(f"Last character: {simple_string[-1]}")  # O(1)
print(f"Slice [1:3]: {simple_string[1:3]}")  # O(k) where k is the slice size

# 2. String Modification (Immutability)
print("\n--- 2. STRING MODIFICATION ---")

# Strings are immutable in Python; they cannot be changed after creation
# Example of creating a new string by modification (O(n))
modified_string = simple_string.replace("l", "z")  # O(n)
print(f"Modified string (replace 'l' with 'z'): {modified_string}")

# Concatenating strings - O(n + m) where n and m are the lengths of the strings
concatenated_string = "Hello" + " World"  # O(n + m)
print(f"Concatenated string: {concatenated_string}")

# String multiplication - O(n * m) where n is the length of the string, m is the multiplier
repeated_string = "Hi! " * 3  # O(n * m)
print(f"Repeated string: {repeated_string}")

# 3. String Operations (Length, Searching, and Membership)
print("\n--- 3. STRING OPERATIONS ---")

# Length of string - O(1)
print(f"Length of simple_string: {len(simple_string)}")  # O(1)

# Checking if a substring exists in a string - O(n) where n is the length of the string
print(f"Is 'ell' in simple_string?: {'yes' if 'ell' in simple_string else 'no'}")  # O(n)
print(f"Is 'xyz' in simple_string?: {'yes' if 'xyz' in simple_string else 'no'}")  # O(n)

# Finding a substring (returns -1 if not found) - O(n) where n is the length of the string
print(f"Index of 'ell' in simple_string: {simple_string.find('ell')}")  # O(n)
print(f"Index of 'xyz' in simple_string: {simple_string.find('xyz')}")  # O(n)

# 4. String Case and Formatting
print("\n--- 4. STRING CASE AND FORMATTING ---")

# Changing case of a string - O(n)
upper_string = simple_string.upper()  # O(n)
print(f"Uppercase string: {upper_string}")

lower_string = simple_string.lower()  # O(n)
print(f"Lowercase string: {lower_string}")

# String formatting - O(n)
formatted_string = f"Hello, {simple_string}"  # O(n)
print(f"Formatted string: {formatted_string}")

# 5. String Splitting and Joining
print("\n--- 5. STRING SPLITTING AND JOINING ---")

# Splitting a string into a list of substrings - O(n)
split_string = simple_string.split("l")  # O(n)
print(f"Split string by 'l': {split_string}")

# Joining a list of strings into a single string - O(n)
joined_string = "-".join(split_string)  # O(n)
print(f"Joined string: {joined_string}")

# 6. String Slicing and Substrings
print("\n--- 6. STRING SLICING AND SUBSTRINGS ---")

# String slicing - O(k) where k is the slice size
substring = simple_string[1:4]  # O(3)
print(f"Substring [1:4]: {substring}")

# Slicing with step - O(k) where k is the length of the slice
step_string = simple_string[::2]  # O(n/2)
print(f"String with step 2: {step_string}")

# 7. String Methods
print("\n--- 7. STRING METHODS ---")

# Removing leading and trailing whitespace - O(n)
stripped_string = "   Hello   ".strip()  # O(n)
print(f"Stripped string: {stripped_string}")

# Checking if a string starts or ends with a specific substring - O(n)
print(f"Does 'Hello' start with 'He'? {'yes' if simple_string.startswith('He') else 'no'}")  # O(n)
print(f"Does 'Hello' end with 'lo'? {'yes' if simple_string.endswith('lo') else 'no'}")  # O(n)

# Replacing a substring in a string - O(n)
replaced_string = simple_string.replace("e", "3")  # O(n)
print(f"Replaced string ('e' with '3'): {replaced_string}")

# 8. String Iteration
print("\n--- 8. STRING ITERATION ---")

# Iterating over each character in the string - O(n)
for char in simple_string:  # O(n)
    print(f"Character: {char}")

# 9. String vs List Performance
print("\n--- 9. STRING VS LIST PERFORMANCE ---")

# Lists are mutable, while strings are immutable
# Operations like appending and modifying elements are much faster with lists than strings
# However, strings are more memory efficient for storing textual data

# Example: Using a list to modify characters
char_list = list(simple_string)  # O(n)
char_list[1] = "a"  # O(1)
modified_string_from_list = ''.join(char_list)  # O(n)
print(f"Modified string from list: {modified_string_from_list}")

# 10. Time Complexity Summary
print("\n--- 10. TIME COMPLEXITY SUMMARY ---")
print("Operation                               | Time Complexity")
print("---------------------------------------- | ----------------")
print("Index access (s[i])                    | O(1)")
print("Concatenation (s + t)                  | O(n + m) where n, m are lengths of strings")
print("Multiplication (s * n)                 | O(n * m) where n is the length of the string, m is the multiplier")
print("Length (len(s))                        | O(1)")
print("Substring check (s in t)               | O(n)")
print("Find substring (s.find(t))             | O(n)")
print("Change case (s.upper(), s.lower())      | O(n)")
print("Format string (f'...{var}...')         | O(n)")
print("Split (s.split())                      | O(n)")
print("Join (s.join())                        | O(n)")
print("Strip (s.strip())                      | O(n)")
print("Replace (s.replace())                  | O(n)")
print("Startswith (s.startswith())            | O(n)")
print("Endswith (s.endswith())                | O(n)")
print("Iterating over string (for c in s)     | O(n)")

print("\nThis guide covers the most common operations and use cases for Python strings.")
