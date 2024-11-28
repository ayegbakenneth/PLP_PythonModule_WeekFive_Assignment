# A class representing a book

class Books:
# Attributes and methods to bring the class to life!   
    def ready_to_read(self):
        print("The book is ready to be selected for reading")
# Use constructors to initialize each object with unique values.
    def __init__(self, color, pageSize):
        self.color = color,
        self.pageSize = pageSize
# An inheritance layer to explore polymorphism or encapsulation.

class DerivedBooks(Books):
    pass
# An example of polymorphism

class changeMethodOfBooks(Books):
    def ready_to_read(self):
        print("The book is ready for reading")
# An example of encapsulation
class EncapsulationExample:
    def __init__(self, firstName, lastName):
        self.__firstName = firstName  # Private attribute
        self.__lastName = lastName   # Private attribute

    def fullName(self):
# Access private attributes using self.__attributeName
        return self.__firstName + " " + self.__lastName
# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Vehicles:
    def move(self):
        print("The vehicle is now moving")
class Car(Vehicles):
    def move(self):
        print("Driving")
class Plane(Vehicles):
    def move(self):
        print("Flying")
# This part of the code is use for testing the logic above.       
firstBook = Books("Blue", 50)
print(firstBook.color)
print(firstBook.ready_to_read())
print(firstBook.pageSize)
secondBook = DerivedBooks("Yellow", 80)
print(secondBook.color)
print(secondBook.pageSize)
thirdBook = changeMethodOfBooks("Black", 30)
print(thirdBook.color)
print(thirdBook.pageSize)
print(thirdBook.ready_to_read())
person = EncapsulationExample("Kenneth", "Ayegba")
print(person.fullName())
corolla = Vehicles()
print(corolla.move())
corolla = Car()
print(corolla.move())
jet = Vehicles()
print(jet.move)
jet = Plane()
print(jet.move())
