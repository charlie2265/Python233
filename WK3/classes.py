# create basic class
# class MyClass:
#     x = 5

# p1 = MyClass() 

# Parent or Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print (f"Iam {self.name}, Iam {self.age} years old.")

# Chlid or derived class
class Student(Person):
    def __init__(self, name, age, major):
        # option 1
        # Person.__init__(self, name, age)
        # option 2
        super().__init__(name, age)
        self.major = major
    def student_intro(self):
        print (f"My name is {self.name}, my major is {self.major}")
        






# p1 = Person("Charlie", 38)
# p1.introduction()
# p1 = Person("Charlie", 38)

# print (f"My name is {p1.name}, and I am {p1.age} years old")

# p2 = Person("Tobin", 35)
# print (p2.name)
# print (p2.age)
        