
from setuptools import reduce #importing reduce module for using reduce function

l1_iy = [2,3,4,5,6]

mapping_the_l1_iy = list(map(lambda x_iy: x_iy*2, l1_iy)) # MAP FUNCTION APPLIES THE GIVEN COMMAND TO EVERY INDEX OF A LIST
# IN THIS CASE WE ARE MULTIPLYING EVERY CHARACTER IF LIST l1 TO 2 USING LAMBDA FUNCTION

print(mapping_the_l1_iy)


filtering_the_l1_iy = list(filter(lambda x_iy: x_iy%2 ==0)) #FILTER FUNCTION FILTERS THE LIST ACCORDING TO OUR WISH
# IN THIS CASE WE ARE FILERING THE NUMBER WHICH IS DIVISIBLE BY 2 IN l1.

print(filtering_the_l1_iy)

def add(x_iy, y_iy):
   return x_iy+y_iy
   
reducing_the_l1_iy = reduce(add, l1_iy) # REDUCE FUNCTION IS USED FOR DOING MATHEMATICAL OPERATIONS IN A LIST
# HERE, WE ARE ADDING ALL THE CHARACTERS THE LIST l1 

print(reducing_the_l1_iy)
