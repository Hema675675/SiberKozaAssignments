#A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Create dict
person_iy = {
'first_name': 'John',
'last_name': 'Doe',
'age': 30
}

#Use constructor
#person2_iy = dict(first_name='Sara', last_name='Williams')
#Get value
print(person_iy['first_name'])
print(person_iy.get('last_name'))

#Add key/value
person_iy['phone'] = '555-555-5555'

#Get dict keys
print(person_iy.keys())

#Get dict items
print(person_iy.items())

#Copy dict
person2_iy = person_iy.copy()
person2_iy['city'] = 'Boston'

#Remove item
del(person_iy['age'])
person_iy.pop('phone')

#Clear
person_iy.clear()

#Get length
print(len(person2_iy))

#List of dict
people_iy = [
{'name': 'Martha', 'age': 30},
{'name': 'Kevin', 'age': 25}
]

print(people_iy[1]['name'])
