# Program to count the number of
# each vowel in a string using
# dictionary and list comprehension

# take input from the user
ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# count the vowels
count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)