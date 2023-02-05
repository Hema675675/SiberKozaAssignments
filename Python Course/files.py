# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile_iy = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile_iy.name)
print('Is Closed : ', myFile_iy.closed)
print('Opening Mode: ', myFile_iy.mode)

# Write to file
myFile_iy.write('I love Python')
myFile_iy.write(' and JavaScript')
myFile_iy.close()

# Append to file
myFile_iy = open('myfile.txt', 'a')
myFile_iy.write(' I also like PHP')
myFile_iy.close()

# Read from file
myFile_iy = open('myfile.txt', 'r+')
text_iy = myFile_iy.read(100)
print(text_iy)
