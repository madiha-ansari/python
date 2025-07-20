# ✅ Functions in Python
# 📌 Kya hai?
# Function ek block of code hota hai jo kisi specific task ko perform karta hai. Hum isay baar baar reuse kar sakte hain.

# 🔹 Function Banane ka Syntax:
# python
# Copy
# Edit
# def function_name(parameters):
#     # code block
#     return result
# 🧪 Example 1: Simple Function
# python
# Copy
# Edit
# def greet():
#     print("Hello, Welcome to Python!")

# greet()  # Output: Hello, Welcome to Python!
# 🧪 Example 2: Function with Parameters
# python
# Copy
# Edit
# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result)  # Output: 8
# 🧪 Example 3: Function with Default Parameter
# python
# Copy
# Edit
# def greet(name="User"):
#     print("Hello", name)

# greet()           # Output: Hello User
# greet("Madiha")   # Output: Hello Madiha
# 🧪 Example 4: Return Multiple Values
# python
# Copy
# Edit
# def calculate(a, b):
#     return a + b, a * b

# sum_, product = calculate(3, 4)
# print(sum_, product)  # Output: 7 12
# ✅ Recursion in Python
# 📌 Kya hai?
# Recursion mein function khud ko call karta hai. Har call mein problem chhoti hoti jati hai, jab tak base case milta hai.

# 🔹 Structure of Recursion:
# Base case — jis par recursion rukta hai

# Recursive case — jahan function khud ko call karta hai

# 🧪 Example 1: Factorial Using Recursion
# python
# Copy
# Edit
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))  # Output: 120
# 🧪 Example 2: Fibonacci Series Using Recursion
# python
# Copy
# Edit
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# for i in range(6):
#     print(fibonacci(i), end=" ")  # Output: 0 1 1 2 3 5
