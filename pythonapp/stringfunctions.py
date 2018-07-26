#STRING FUNCTIONS

myStr='HelloWorld'

#Capitalize
print(myStr.capitalize())

#Swap case
print(myStr.swapcase())

#Get length
print(len(myStr))

#Replace
print(myStr.replace('World', 'Everyone'))

#Count
sub='H'
print(myStr.count(myStr))

#Startswith
print(myStr.startswith('Hello'))

#Endswith
print(myStr.endswith('World'))

#Split to list
print(myStr.split())

#Is all alphanumeric
print(myStr.isalnum())

#Is all alphabetic
print(myStr.isalpha())

#Is all numeric
print(myStr.isnumeric())