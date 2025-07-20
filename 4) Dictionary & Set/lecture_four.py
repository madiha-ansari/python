# ✅ 1. Dictionary in Python
# 📌 Kya hai?
# Dictionary ek key-value pair wali collection hoti hai.
# Har value kisi unique key ke sath store hoti hai.

# 📦 Syntax:
# my_dict = {"name": "Ali", "age": 25, "city": "Lahore"}
# 📌 Important Features:
# Key-value format

# Keys unique hote hain

# Mutable hai (change kar sakte ho)

# Order preserved hota hai (Python 3.7+)

# 🧪 Dictionary Examples:
# student = {"name": "Sara", "age": 20, "grade": "A"}

# # Access
# print(student["name"])  # Output: Sara

# # Add new item
# student["city"] = "Karachi"

# # Update existing item
# student["age"] = 28
# print(student)

# # Update existing item
# student["age"] = 21
# print(student)

# 🧪 Dictionary Examples:
# student = {"name": "Sara", "age": 20, "grade": "A"}

# # Remove item
# del student["grade"]
# print(student)

# # Loop through keys
# for key in student:
#     print(key, "=>", student[key])

# # Get all keys
# print(student.keys)

# # Get all values
# print(student.values())

# # Get all items
# print(student.items())


# ✅ 2. Set in Python
# 📌 Kya hai?

# Set ek unordered, unchangeable (immutable elements), aur unique items wali collection hoti hai.

# 📦 Syntax:
# my_set = {1, 2, 3, 4}

# ⚠️ Note: Duplicate values automatically remove ho jaate hain.

# 📌 Important Features:
# Only unique items

# Unordered (no index)

# Mutable hai (items add/remove kar sakte ho)

# Fast membership test (check in)

# 🧪 Set Examples:

# nums = {1, 2, 3, 2, 1}
# print(nums)  # Output: {1, 2, 3}

# # Add item
# nums.add(4)

# # Remove item
# nums.remove(2)
# print(nums)

# # Check item
# print(3 in nums)  # Output: True

# # Union
a = {1, 2}
b = {2, 3}
print(a | b)  # Output: {1, 2, 3}

# # Intersection
print(a & b)  # Output: {2}

# # Difference
print(a - b)  # Output: {1}
