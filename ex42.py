from textwrap import dedent

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        #super(Employee, self).__init__(name)
        super().__init__(name)
        self.salary = salary

frank = Employee("Frank", 120000)
print(frank.salary)

print(dedent("""
    This is just a 
    joke
    with stapce
    !
"""))
