# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_iy = 'Brad'
age_iy = 37

#Concatenate
print('Hello, my name is ' + name_iy + ' and I am ' + str(age_iy))

#String Formatting
#Arguments by position
print('My name is {name_iy} and I am {age_iy}'.format(name_iy=name_iy, age_iy=age_iy))

#F-Strings (3.6+)
print(f'Hello, my name is {name_iy} and I am {age_iy}')

#String Methods
s_iy = 'helloworld'

#Capitalize string
print(s_iy.capitalize())

#Make all uppercase
print(s_iy.upper())

#Make all lower
print(s_iy.lower())

#Swap case
print(s_iy.swapcase())

#Get length
print(len(s_iy))

#Replace
print(s_iy.replace('world', 'everyone'))

#Count
sub_iy = 'h'
print(s_iy.count(sub_iy))

#Starts with
print(s_iy.startswith('hello'))

#Ends with
print(s_iy.endswith('d'))

#Split into a list
print(s_iy.split())

#Find position
print(s_iy.find('r'))

#Is all alphanumeric
print(s_iy.isalnum())

#Is all alphabetic
print(s_iy.isalpha())

#Is all numeric
print(s_iy.isnumeric())
