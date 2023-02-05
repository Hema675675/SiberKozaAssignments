# If/ Else conditions are used to decide to do something based on something being true or false

x_iy = 21
y_iy = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x_iy > y_iy:
  print(f'{x_iy} is greater than {y_iy}')

# If/else
if x_iy > y_iy:
  print(f'{x_iy} is greater than {y_iy}')
else:
  print(f'{y_iy} is greater than {x_iy}')  

# elif
if x_iy > y_iy:
  print(f'{x_iy} is greater than {y_iy}')
elif x_iy == y_iy:
  print(f'{x} is equal to {y}')  
else:
  print(f'{y_iy} is greater than {x_iy}')  

# Nested if
if x_iy > 2:
  if x_iy <= 10:
    print(f'{x_iy} is greater than 2 and less than or equal to 10')
    

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x_iy > 2 and x_iy <= 10:
    print(f'{x_iy} is greater than 2 and less than or equal to 10')

# or
if x_iy > 2 or x_iy <= 10:
    print(f'{x_iy} is greater than 2 or less than or equal to 10')

# not
if not(x_iy == y_iy):
  print(f'{x_iy} is not equal to {y_iy}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_iy = [1,2,3,4,5]

#  in
if x_iy in numbers_iy:
  print(x_iy in numbers_iy)

# not in
if x_iy not in numbers_iy:
  print(x_iy not in numbers_iy)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x_iy is y_iy:
  print(x_iy is y_iy)

# is not
if x_iy is not y_iy:
  print(x_iy is not y_iy)
