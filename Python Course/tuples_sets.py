# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#Create tuple
fruits_iy = ('Apples', 'Oranges', 'Grapes')

#Using a constructor
fruits2_iy = tuple(('Apples', 'Oranges', 'Grapes'))
#Single value needs trailing comma
fruits2_iy = ('Apples',)

#Get value
print(fruits_iy[1])

#Can't change value
fruits_iy[0] = 'Pears'
#Delete tuple
del fruits2_iy

#Get length
print(len(fruits_iy))

#A Set is a collection which is unordered and unindexed. No duplicate members.
#Create set
fruits_set_iy = {'Apples', 'Oranges', 'Mango'}

#Check if in set
print('Apples' in fruits_set_iy)

#Add to set
fruits_set_iy.add('Grape')

#Remove from set
fruits_set_iy.remove('Grape')

#Add duplicate
fruits_set_iy.add('Apples')

#Clear set
fruits_set_iy.clear()

#Delete
del fruits_set_iy

print(fruits_set_iy)
