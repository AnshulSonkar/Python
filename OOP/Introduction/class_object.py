# First Class
# class Car:
#     brand = "Toyota"
#     color = "Red"
#     speed = 120


# car1 = Car()

# print(car1.brand)
# print(car1.color)
# print(car1.speed)
# 


#Creating Methods Inside a Class 
# class Car:

#     def start(self):
#         print("Car is starting...")

#     def stop(self):
#         print("Car is stopping...")


# car1 = Car()

# car1.start()
# car1.stop()


# Understanding self
# class Student:

#     def display(self):
#         print("Student information")


# student1 = Student()

# student1.display()
# 


# Multiple Objects from One Class
# class Student:

#     def display(self):
#         print("Student:", self.name)
#         print("Age:", self.age)


# student1 = Student()
# student1.name = "Anshul"
# student1.age = 20

# student2 = Student()
# student2.name = "Rahul"
# student2.age = 21

# student1.display()

# print()

# student2.display()
# 


# Practical Example: Bank Account
# class BankAccount:

#     def display(self):
#         print("Account Holder:", self.name)
#         print("Balance:", self.balance)

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient Balance")


# account1 = BankAccount()

# account1.name = "Anshul"
# account1.balance = 5000

# account1.deposit(2000)
# account1.withdraw(1000)

# account1.display() 
# 


# CONSTRUCTOR
# A constructor is a special method that initializes an object when it is created.

# In Python, we use:
# def __init__(self):

# The __init__() method is automatically called when you create an object.
# class Student:

#     def __init__(self):
#         print("Constructor called!")

# student1 = Student()
# student2 = Student()
# 


# Parameterized Constructor
# class Student:
#  def __init__(self, name, age):
#         self.name = name
#         self.age = age

#  def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# student1 = Student("Anshul", 20)
# student2 = Student("Rahul", 21)

# student1.display()

# print()

# student2.display() 
# 


# Default Constructor
# A constructor that doesn't require additional arguments (other than self) is commonly called a default or no-argument constructor.
# class Car:

#     def __init__(self):
#         self.brand = "Toyota"
#         self.color = "Black"

#     def display(self):
#         print("Brand:", self.brand)
#         print("Color:", self.color)


# car1 = Car()

# car1.display()
# 