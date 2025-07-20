# str
# is a dt that store a sequence of character

# str1 = 'Hello world'
# str2 = "Hello world"
# str3 = '''Hello world'''

# str1 = "this is a apna collages's' titoriual"
# print(str1)

# str1 = "this is a apna collages's' titoriual.\nwe are crativity"
# print(str1)

# escape sequence charcater
# \n 

# concatenation
# str1 = "Apna"
# str2 = "College"
# finalString = str1 + str2
# print(finalString)

# length of str
# str1 = "Apna"
# len1 = len(str1)
# print(len1)

# str2 = "College"
# len2 = len(str2)
# print(len2)

# final = str1+ " "+ str2
# print(len(final))

# indexing
# strat the 0
# index acces the str  []

# name = "Madiha"
# print(name[0])

# index are not assig 

# name = "Madiha"
# ch = name[0]
# name[0] = "B"  not allowed acces kar sakata ha maniuplate nh kar sakat 
# print(ch)

# slicing
# acces part of str
# name1 = "APNACOLLEGE"
# name2 = name1[0:4]            
# name2 = name1[0:len(name1)]   
# name2 = name1[0:]             
# name2 = name1[:4]             
# print(name2)

# nagative
# str = "APPLE"
     #  -1
# str1 = str[-3:-1]
# str1 = str[-5:-2]
# print(str1)


# string method names in Python:

# upper()
# lower()
# title()
# strip()
# replace()
# find()
# split()
# join()
# startswith()
# endswith()
# capitalize()
# count()
# isalpha()
# isdigit()
# islower()
# isupper()
# isspace()
# istitle()
# rfind()
# rstrip()
# lstrip()
# zfill()
# center()
# format()

# code with example

# ✅ 1. upper()
# name = "hello"
# result = name.upper()
# print(result)


# ✅ 2. lower()
# text = "HELLO"
# result = text.lower()
# print(result)

# ✅ 3. title()
# text = "hello world"
# print(text.title())  # Output: Hello World

# ✅ 4. strip()
# text = "     hello  "
# print(text.strip())  # Output: hello

# ✅ 5. replace()
# text = "hello world"
# result = text.replace("world","python")
# print(result)

# ✅ 6. find()
# text = "hello world"
# result = text.find("world")
# print(result)




# ________________________________________________________________________________________________________________________________
# ✅ 7. split()

# text = "apple,mango,banna"
# result = text.split(",")
# print(result)              #['apple', 'mango', 'banna']

# ✅ 8. join()
# text = ['apple', 'banana', 'grapes']
# result = ", ".join(text)
# print(result)  # Output: apple, banana, grapes


# ✅ 9. startswith()
# text = "Madiha Ansari"
# result = text.startswith("Madiha")
# print(result)


# ✅ 10. endswith()
# text = "Madiha Ansari"
# result = text.endswith("Ansari")
# print(result)


# ✅ 11. capitalize()
# text = "hello world"
# result = text.capitalize()
# print(result)







# _____________________________________________________________________________________________________
# ✅ 12. count()
# text = "madiha"
# result = text.count("a")
# print(result)   #count start 1


# ✅ 13. isalpha()
# text = "abc"
# print(text.isalpha())  # Output: True





# ✅ 14. isdigit()
# python
# Copy
# Edit
# text = "12345"
# print(text.isdigit())  # Output: True


# ✅ 15. islower()
# text = "hello"
# print(text.islower())  # Output: True

# ✅ 16. isupper()
# text = "HELLO"
# print(text.isupper())  # Output: True



































# ✅ 17. isspace()
# text = "   "
# print(text.isspace())  # Output: True


# ✅ 18. istitle()
# text = "Hello World"
# print(text.istitle())  # Output: True




# ✅ 19. rfind()
# text = "hello world hello"
# print(text.rfind("hello"))  # Output: 12




# ✅ 20. rstrip()
# text = "hello   "
# print(text.rstrip())  # Output: 'hello'

# ✅ 21. lstrip()
# text = "   hello"
# print(text.lstrip())  # Output: 'hello'

# ✅ 22. zfill()
# text = "42"
# print(text.zfill(5))  # Output: 00042

# ✅ 23. center()
# text = "hi"
# print(text.center(10, "*"))  # Output: ****hi****

# ✅ 24. format()
# name = "Ali"
# age = 22
# text = "My name is {} and I am {} years old.".format(name,age)
# print(text)
# Output: My name is Ali and I am 22 years old.


# ✅ Conditional Statements in Python (if, elif, else)
# Python mein Conditional Statements ka use hota hai kisi condition ke base par decision lene ke liye.

# 🔹 1. if Statement
# Agar condition True hai to block run hoga.


# age = 18
# if age >= 18:
#     print("You are eligible to vote.")

# 🔹 2. if...else Statement
# Agar condition True ho to if block chalega, warna else block.
# age = 16
# if age >= 18:
#     print("You can vote.")
# else:
#     print("You are too young to vote.")
# 🔹 3. if...elif...else Statement
# Multiple conditions check karne ke liye.

# marks = 75
# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# else:
#     print("Fail")
# 🔹 4. Nested if Statements
# if ke andar doosra if.

# python
# Copy
# Edit
age = 20
citizen = "yes"

if age >= 18:
    if citizen == "yes":
        print("You can vote.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You are too young to vote.")
    
# 📌 Note:
# Python mein indentation (spaces) kaafi important hai.
# : colon lagana zaroori hai if, elif, else ke baad.