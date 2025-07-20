# Zaroor! Ab hum OOP Part 2 mein Python ke advanced object-oriented concepts ko detail mein samjhenge — jisme aate hain:

# ✅ 1. self keyword
# ✅ 2. Class vs Instance Variables
# ✅ 3. Types of Methods (Instance, Class, Static)
# ✅ 4. Inheritance (Advanced)
# ✅ 5. super() function
# ✅ 6. Encapsulation (Private, Protected)
# ✅ 7. Polymorphism (Method Overriding)
# ✅ 8. Dunder (Magic) Methods
# ✅ 1. self keyword
# self object ka reference hota hai — isse object ke attributes/methods access karte hain.

# python
# Copy
# Edit
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print("Name:", self.name)

# s = Student("Ali")
# s.show()
# ✅ 2. Class Variables vs Instance Variables
# python
# Copy
# Edit
# class Student:
#     school = "City School"  # class variable (shared by all)

#     def __init__(self, name):
#         self.name = name  # instance variable (unique to each)

# s1 = Student("Ali")
# s2 = Student("Sara")

# print(s1.school)  # City School
# print(s1.name)    # Ali
# ✅ 3. Types of Methods
# 🔸 Instance Method (default)
# python
# Copy
# Edit
# class Demo:
#     def say_hello(self):  # self required
#         print("Hello")
# 🔸 Class Method (@classmethod)
# Used to access/modify class variables

# python
# Copy
# Edit
# class Demo:
#     school = "ABC"

#     @classmethod
#     def change_school(cls, name):
#         cls.school = name
# 🔸 Static Method (@staticmethod)
# No access to class/object data — general utility

# python
# Copy
# Edit
# class Demo:
#     @staticmethod
#     def add(a, b):
#         return a + b
# ✅ 4. Inheritance (Advanced)
# python
# Copy
# Edit
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):  # single inheritance
#     def bark(self):
#         print("Dog barks")
# 🔹 Multiple Inheritance
# python
# Copy
# Edit
# class A:
#     def showA(self):
#         print("Class A")

# class B:
#     def showB(self):
#         print("Class B")

# class C(A, B):
#     pass

# obj = C()
# obj.showA()
# obj.showB()
# ✅ 5. super() function
# Used to call parent class constructor or methods.

# python
# Copy
# Edit
# class Person:
#     def __init__(self):
#         print("Person init")

# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         print("Student init")

# s = Student()
# ✅ 6. Encapsulation — Private & Protected
# python
# Copy
# Edit
# class Test:
#     def __init__(self):
#         self._protected = "Can be accessed"
#         self.__private = "Cannot be accessed directly"

#     def get_private(self):
#         return self.__private

# t = Test()
# print(t._protected)
# print(t.get_private())
# ✅ 7. Polymorphism — Method Overriding
# python
# Copy
# Edit
# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark!")

# d = Dog()
# d.sound()  # Output: Bark!
# ✅ 8. Dunder Methods (__str__, __len__, etc.)
# python
# Copy
# Edit
# class Book:
#     def __init__(self, title):
#         self.title = title

#     def __str__(self):
#         return f"Book: {self.title}"

# b = Book("Python Basics")
# print(b)  # Output: Book: Python Basics
