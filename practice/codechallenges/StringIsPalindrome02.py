"""
wrte a function to determine if a given string is a plaindrome.
palindrome: word or phrase that reads the same forwards as backwords.
example: level, racecar
input: string to ealuate
output: bool value
only consider letters(A-Z)
ignore case (for example, 'A' =='a')
"""

import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

print(is_palindrome("level"))
print(is_palindrome("racecar"))
print(is_palindrome("hello world"))
print(is_palindrome("Go hang a salami, I'm a lasagna hog."))