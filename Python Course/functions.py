# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello_iy(name='Sam'):
    print(f'Hello {name}')


# Return values
def getSum_iy(num1, num2):
    total_iy = num1 + num2
    return total_iy


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum_iy = lambda num1, num2: num1 + num2

print(getSum_iy(10, 3))
