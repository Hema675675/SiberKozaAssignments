# A List is a collection which is ordered and changeable. Allows duplicate members.

#Create list
numbers_iy = [1, 2, 3, 4, 5]
fruits_iy = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Get a value
print(fruits_iy[1])

#Get the last value
print(fruits_iy[-1])

#Get length
print(len(fruits_iy))

#Append to list
fruits_iy.append('Mangos')

#Remove from list
fruits_iy.remove('Grapes')

#Insert into position
fruits_iy.insert(2, 'Strawberries')

#Change value
fruits_iy[0] = 'Blueberries'

#Remove with pop
fruits_iy.pop(2)

#Reverse list
fruits_iy.reverse()

#Sort list
fruits_iy.sort()

#Reverse sort
fruits_iy.sort(reverse=True)

print(fruits_iy)
