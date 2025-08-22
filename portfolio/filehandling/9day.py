#class and object
# (ooop)
# class home:
#     pass
# my_house =home()
# print(my_house)

# attribute store data about the onject define inside the method ,usually inside _init_ method also(initailize the value)
#  construcotor _inti_ dunder method
# we can make multiple oject in python



# key points to remember 

# class = blueprint
# object =instances of class
#   attribute =varaiables inside the class
#     Method=function inside the class
#       __init__ =constructor,initalize AttributeError
#       delf=refers to the current object




# class House:
#  def __init__(self,color): 
#     print("Inside class self:",self)
#     self.color = color
    
#  def ring_the_bell(self):
#    print("ring the bell!!",self)

#  def chnage_the_color(self,new_color):
#    self.color =new_color
   

# house1 = House("Blue")
# house2 = House("yellow")

# print("house1 initail color:",house1.color)
# print("house2 initail color:",house2.color)


# # Method
# house1.chnage_the_color("Greeen")
# house2.chnage_the_color("orange")

# print("house1 new  color:",house1.color)
# print("house2 new  color:",house2.color)
# print("house1 :",house1.ring_the_bell())
# print("house2 :",house2.ring_the_bell())


# Full Day Class & Object Coding Questions
# Basic
# 1. Create a class Car with attributes brand and color .
# Create two objects and print their attributes


class car:
 def __init__(self,color,brand):
   self.color =color
   self.brand=brand
car1=car("blue","kia")
car2=car("Ash","BYD")
print(car1.brand ,car1.color)
print(car2.color ,car2.brand)



# 2. Create a class Student with attribute name .
# Add a method greet() to print: "Hello, I am <name>" .
# Create three students and call their greet() method.

class student:
  def __init__(self,name):
    self.name=name
    
  def greet(self):
      print(f"Good morning!!{self.name}")
    
student1=student('Rupashri')
student2=student('Aerika')
student3=student('Riya')
student1.greet()
student2.greet()
student3.greet()


# 3. Create a class Dog with an attribute name .
# Add a method bark() that prints: "<name> is barking!" .
# Create two dogs and call their method.

class Dog:
  def __init__(self,name):
    self.name=name
  def bark(self):
      print(f"dog is barking{self.name}")

dog1=Dog('tommy:')
dog2=Dog('lucky:')
dog1.bark()
dog2.bark()
    

# Intermediate
# 1. Create a class BankAccount with attributes account_number and balance=0 .
# Add methods:
# deposit(amount)
# withdraw(amount)
# show_balance()
# Create an account, deposit money, withdraw some, and display the
# balance



class BankAccount:
    def __init__(self,account_number,balance=0.00):
        self.account_number=account_number
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount

        print(f"Deposited: {amount}")


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

            
    def show_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")

account1 = BankAccount("12345")   
account1.deposit(500)             
account1.withdraw(200)            
account1.show_balance()
    
# 2. Create a class Book with:
# Class attribute: category = "Fiction"
# Instance attributes: title , author
# Method: display() to show book details
# Create two books and display their details.




class Book:
    # Class attribute
    category = "Fiction"

    def __init__(self, title, author):
        # Instance attributes
        self.title = title
        self.author = author

    def display(self):
        print(f"Category: {Book.category}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
       

book1 = Book("action", "nirojdai ")
book2 = Book("fiction", "hahah hehe")

book1.title
book1.display()
book2.display()


# 3. Create a class Rectangle with attributes length and width .
# Untitled 1
# Add methods:
# area()
# perimeter()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)



rect1 = Rectangle(10, 5)

print("Area:", rect1.area())         
print("Perimeter:", rect1.perimeter()) 


# Challenging
# 1. Create a class ShoppingCart :
# add_item(item) – adds item to a list
# remove_item(item) – removes item if it exists
# show_cart() – prints the list of items
# Simulate adding, removing, and showing items.

    
class ShoppingCart:
    def __init__(self):
        self.items = []   

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to cart.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from cart.")
        else:
            print(f"{item} not found in cart.")

    def show_cart(self):
        if self.items:
            print("Your cart contains:", self.items)
        else:
            print("Your cart is empty.")

cart = ShoppingCart()

cart.add_item("Apple")
cart.add_item("Banana")
cart.show_cart()

cart.remove_item("Apple")
cart.show_cart()

cart.remove_item("Mango") 





# 2. Create a class Counter with an attribute count=0 .
# Add method increment() – increases count by 1
# Add method reset() – resets count to 0
# Create two counter objects and increment them differently.


class Counter:
    def __init__(self,count=0):
        self.count =count
    def increment(self):
        self.count +=1
        print(self)
    def reset(self):
        self.count +=0
        print(self)
Counter1=Counter()
Counter2=Counter()
Counter2=Counter()
Counter1=Counter()

        


# 3. Create a class TemperatureConverter :
# c_to_f(celsius) → convert Celsius to Fahrenheit
# f_to_c(fahrenheit) → convert Fahrenheit to Celsius
# Test both methods



class TemperatureConverter:
    def __init__(self, value):
        self.value = value 


    def c_to_f(self):
        celc= (self.value * 9/5) + 32
        print(f'celc value' is {celc})

    def f_to_c(self):
        fahr= (self.value - 32) * 5/9
        print(f'fahrenheit value' is {fahr})



t1 = TemperatureConverter(25)     # Celsius


t2 = TemperatureConverter(98.6)   # Fahrenheit



# 4. Create a class Movie with attributes title , genre , and rating .
# Add method is_recommended() → returns True if rating ≥ 8 else False .
# Create three movies and check which ones are recommended.
# class Movie:
#     def __init__(self,title,genre,rating):

        




