# Zaroor! Python mein OOP (Object-Oriented Programming) ek powerful programming approach hai jo real-world concepts (jaise ke objects, classes, attributes, behavior) ko programming mein represent karti hai.

# ✅ What is OOP in Python?
# OOP (Object Oriented Programming) ek style hai jisme hum objects ka use karke program banate hain. Har object ka apna data (attributes) aur functionality (methods) hoti hai.

# 🔹 Core Concepts of OOP:
# Class

# Object

# Constructor (__init__)

# Attributes (properties)

# Methods (functions)

# Inheritance

# Encapsulation

# Polymorphism

# ✅ 1. Class:
# Blueprint ya design hoti hai object banane ke liye.

# python
# Copy
# Edit
# class Car:
#     # attributes and methods will go here
#     pass
# ✅ 2. Object:
# Class ka actual instance hota hai (real object).

# python
# Copy
# Edit
# mycar = Car()
# ✅ 3. Constructor: __init__()
# Object banate waqt chalne wala special method hota hai. Yahan attributes set hote hain.

# python
# Copy
# Edit
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
# ✅ 4. Attributes & Methods
# python
# Copy
# Edit
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def drive(self):
#         print(f"{self.color} {self.brand} is driving.")

# mycar = Car("Toyota", "Red")
# mycar.drive()  # Output: Red Toyota is driving.
# ✅ 5. Inheritance
# Ek class doosri class ke properties inherit karti hai.

# python
# Copy
# Edit
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# d = Dog()
# d.speak()  # Output: Animal speaks
# d.bark()   # Output: Dog barks
# ✅ 6. Encapsulation
# Data ko hide karna (private variables).

# python
# Copy
# Edit
# class Person:
#     def __init__(self, name):
#         self.__name = name  # private variable

#     def get_name(self):
#         return self.__name

# p = Person("Ali")
# print(p.get_name())  # Output: Ali
# ✅ 7. Polymorphism
# Ek method multiple forms mein kaam karta hai.

# python
# Copy
# Edit
# class Bird:
#     def sound(self):
#         print("Bird sounds")

# class Duck(Bird):
#     def sound(self):
#         print("Quack!")

# class Sparrow(Bird):
#     def sound(self):
#         print("Chirp!")

# for bird in [Duck(), Sparrow()]:
#     bird.sound()