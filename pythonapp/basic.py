# BASICS OF PRINTING

# This is a single line comment

'''
This is a
multi-line comment
'''
from pip._vendor.pyparsing import line
""" 
This is a
multi-line comment
"""

# Single quotes
print('Hello World')

#Double quotes
print("Hello World")

#TIP- Stay consistent with your quotes

#Triple quotes
print("""Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""" )

#Print substring
print('Hello'[2])
print('Hello'[0:2])

#Print number
print(2)

#Print on the same line
print(1,2,3, 'Hello')

#Print on separate line
print("Line1\nLine2\nLine3")

#Print special character
print(r"c:\\somewhere\n")