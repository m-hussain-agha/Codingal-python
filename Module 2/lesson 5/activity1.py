# parent class
class Person( object ):

                 # __init__ is known as the constructor
                 def __init__(self, name, idumber):
                                self.name = name
                                self.idumber = idumber
                 def display(self):
                                 print(self.name)
                                 print(self.idumber)
# chile class
class Employee( Person ):
                 def __init__(self, name, idumber, salary, post):
                                 self.salary = salary
                                 self.post = post

                                 # invoking the __init__ of the parent class
                                 Person.__init__(self, name, idumber)


# creation of an object variable or an instance
a = Employee('Penguin', 20210401, 15000, "Intern")

# calling a function of the class Person using its instance a.display()