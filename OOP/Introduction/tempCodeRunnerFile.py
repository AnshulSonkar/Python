class Employee:

    def __init__(self, name="Unknown", salary=10000):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


emp1 = Employee("Anshul", 50000)
emp2 = Employee("Rahul")
emp3 = Employee()

emp1.display()
print()

emp2.display()
print()

emp3.display()