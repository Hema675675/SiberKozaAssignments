# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_iy = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person_iy in people_iy:
  print(f'Current Person: {person_iy}')

# Break
for person_iy in people_iy:
  if person_iy == 'Sara':
    break
  print(f'Current Person: {person_iy}')

# Continue
for person_iy in people_iy:
  if person_iy == 'Sara':
    continue
  print(f'Current Person: {person_iy}')

# range
for i in range(len(people_iy)):
  print(people_iy[i])

for i in range(0, 11):
  print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count_iy = 0
while count_iy < 10:
  print(f'Count: {count_iy}')
  count_iy += 1
