# ✅ 1. while Loop in Python

# Jab tak condition True rahegi, tab tak code bar bar chalega.

# 📦 Syntax:
# while condition:
#     # code block
# 🧪 Example 1: Count from 1 to 5

# i = 1
# while i <= 5:
#     print(i)
#     i += 1


i = 1
while i < 6:
  print(i)
  i += 1



# 🧪 Example 2: Infinite Loop (Break se roka gaya)
# i = 1
# while True:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# ✅ 2. for Loop in Python
# 📌 Kya hai?
# for loop kisi sequence (list, tuple, string, range, etc.) ke upar iterate karta hai.

# 📦 Syntax:
# python
# Copy
# Edit
# for variable in sequence:
#     # code block
# 🧪 Example 1: Loop through a list
# python
# Copy
# Edit
# fruits = ["apple", "banana", "mango"]
# for fruit in fruits:
#     print(fruit)
# 🧪 Example 2: Use with range()
# python
# Copy
# Edit
# for i in range(1, 6):  # 1 se 5 tak
#     print(i)
# 🧪 Example 3: Loop through string
# python
# Copy
# Edit
# for letter in "hello":
#     print(letter)
# ✅ Useful Loop Keywords
# 🔹 break
# Loop ko turant rok deta hai.

# python
# Copy
# Edit
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
# 🔹 continue
# Baaki code skip karke next iteration pe chala jata hai.

# python
# Copy
# Edit
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
# 🔹 else with loop
# Loop khatam hone ke baad chalta hai (agar break na ho).

# python
# Copy
# Edit
# for i in range(3):
#     print(i)
# else:
#     print("Loop finished.")
