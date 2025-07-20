# Zaroor! Python mein File Input/Output (I/O) ka matlab hai:

# File se data read karna (Input)
# Aur file mein data write karna (Output)

# Yeh feature real-world applications ke liye bohat zaroori hota hai — jaise ke user data save karna, reports generate karna, logs likhna, etc.

# ✅ Steps for File I/O in Python
# 🔹 open() Function — File ko kholta hai
# python
# Copy
# Edit
# file = open("filename.txt", "mode")
# Mode	Description
# "r"	Read (default mode)
# "w"	Write (overwrite)
# "a"	Append (add at end)
# "x"	Create new file
# "b"	Binary mode
# "t"	Text mode (default)

# ✏️ Writing to a File
# 🧪 Example:
# python
# Copy
# Edit
# file = open("myfile.txt", "w")   # Write mode
# file.write("Hello, this is Python!\n")
# file.write("This is a new line.")
# file.close()
# write() function se file mein text likha jata hai.
# close() karna zaroori hai taake file properly save ho jaye.

# 📖 Reading from a File
# 🧪 Example 1: Read full file
# python
# Copy
# Edit
# file = open("myfile.txt", "r")
# content = file.read()
# print(content)
# file.close()
# 🧪 Example 2: Read line by line
# python
# Copy
# Edit
# file = open("myfile.txt", "r")
# for line in file:
#     print(line.strip())  # strip() removes \n
# file.close()
# 🔄 Appending to a File
# python
# Copy
# Edit
# file = open("myfile.txt", "a")
# file.write("\nThis line is appended.")
# file.close()
# ✅ Using with Statement (Best Practice)
# Python mein with block use karne se file automatically close ho jati hai.

# python
# Copy
# Edit
# with open("myfile.txt", "r") as file:
#     print(file.read())

# with open("myfile.txt", "a") as file:
#     file.write("\nUsing with block.")
