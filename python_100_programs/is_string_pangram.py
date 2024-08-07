import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return set(s.lower()) >= alphabet

input_string = input("Enter a string: ")
if is_pangram(input_string):
    print("Pangram")
else:
    print("Not a pangram")    