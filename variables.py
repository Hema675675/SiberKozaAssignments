# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x_iy = 1 # int
y_iy = 2.5 # float
name_iy = 'John' # str
is_cool_iy = True # bool

#Multiple assignment

x_iy, y_iy, name_iy, is_cool_iy = (1, 2.5, 'John', True)

#Basic math
a_iy = x_iy + y_iy

#Casting
x_iy = str(x_iy)
y_iy = int(y_iy)
z_iy = float(y_iy)

print(type(z_iy), z_iy)
