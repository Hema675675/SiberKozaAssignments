# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User_iy:

  # Constructor
  def __init__(self_iy, name_iy, email_iy, age_iy):
    self_iy.name_iy = name_iy
    self_iy.email_iy = email_iy
    self_iy.age_iy = age_iy
    
    # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
    self_iy._private = 1000 # Encapsulated variables are declares with '_' in the constructor.

  def greeting(self_iy):
      return f'My name is {self_iy.name_iy} and I am {self_iy.age_iy}'

  def has_birthday(self_iy):
      self_iy.age_iy += 1
 
 #function for encap variable
  def print_encap(self_iy):
      print(self_iy._private)

# Extend class
class Customer_iy(User_iy):
  # Constructor
  def __init__(self_iy, name_iy, email_iy, age_iy):
      User_iy.__init__(self_iy, name_iy, email_iy, age_iy) #Called proper parent class constructor to make this as proper child inehriting all methods.
      self_iy.name_iy = name_iy
      self_iy.email_iy = email_iy
      self_iy.age_iy = age_iy
      self_iy.balance_iy = 0

  def set_balance(self_iy, balance_iy):
      self_iy.balance_iy = balance_iy

  def greeting(self_iy):
      return f'My name is {self_iy.name_iy} and I am {self_iy.age_iy} and my balance is {self_iy.balance_iy}'

#  Init user object
brad_iy = User_iy('Brad Traversy', 'brad@gmail.com', 37)
# Init customer object
janet_iy = Customer_iy('Janet Johnson', 'janet@yahoo.com', 25)

janet_iy.set_balance(500)
print(janet_iy.greeting())

brad_iy.has_birthday()
print(brad_iy.greeting())

#Encapsulation -->
brad_iy.print_encap()
brad_iy._private = 800 #Changing for brad
brad_iy.print_encap()

# Method inherited from parent
janet_iy.print_encap() #Changing the variable for brad doesn't affect janets variable --> Encapsulation
janet_iy._private = 600
janet_iy.print_encap()

#Similary changing janet's doesn't affect brad's variable.
brad_iy.print_encap()

 
