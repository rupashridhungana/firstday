# # Python Assignment: File
# # Handling & Exception Handling
# # Part A: File Handling
# # 1. Create a text file named data.txt and write the following lines into it using
# # Python:
# # Python is fun.
# # File handling makes it powerful.
# # Exception handling makes it reliable.

# with open("data.txt", "w") as f:
#     f.write("Python is fun.\n")
#     f.write("File handling makes it powerful.\n")
#     f.write("Exception handling makes it reliable.\n")

# print("data.txt file created and text written successfully!")



# # 2. Write a Python program to read the entire contents of data.txt and display it on the screen.
# with open('data.txt','r') as f:
#     f_contents =f.read()
#     print(f_contents)


# # 3. Write a program to read only the first 10 characters from data.txt .
# with open("example.txt","r") as f:   
#     f_contents=f.read(10)
#     print(f_contents)

# # 4. Use .readline() to read the first line only

# with open('data.txt','r')as f:
#     f_contents=f.readline()
#     print(f_contents)



# 5. Use a loop with .readline() or .readlines() to display all lines one by one
with open("data.txt","r") as f:   
    size_to_read =10
    f_contents=f.read(size_to_read)

    while len(f_contents) >0 :
        print(f_contents ,)
        f_contents = f.read(size_to_read)


# 6. Write a program that takes user input and appends it to data.txt without overwriting existing "content".

with open("data.txt","a") as f:   
    f.write(input("enter a text:"))
    f_append=f.write("")
    print(f_append)

# 7. Write a program that creates another file named copy.txt and copies all content from data.txt into it.

with open("data.txt","r") as rf:   
    with open("copy.txt",'w') as wf:
        wf.write(rf.read())


# 8. Write a program to count the number of words in data.txt .
with open("data.txt", "r") as f:
    content = f.read()         # Read entire file
    words = content.split()    # Split into words (by spaces/newlines)
    word_count = len(words)    # Count the words

print("Total number of words in data.txt:", word_count)

# 9. Write a program to find and print the longest word in data.txt .



# 10. Use the tell() and seek() methods to:
# Print the current file pointer position.
# Move the file pointer to the beginning and re-read the first line.

with open("example.txt","r") as f:   
   print("cursor is in line:",f.tell())
   size_to_read =10
   f_contents=f.read(size_to_read)
   print("cursor is in the line:",f.tell())






# Part B: Exception Handling
# Python Assignment: File Handling & Exception Handling 1
# 1. Write a program that asks the user to enter a number and divides 100 by that
# number.
# Handle ZeroDivisionError and display an appropriate message


try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# 2. Write a program that tries to open a file named missing.txt .Handle FileNotFoundError gracefully

try:
    with open("missing.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("Error: The file 'missing.txt' was not found!")


# 3. Write a program to take a number from the user and convert it into an integer.Handle ValueError if the user enters invalid input
# Program to convert user input into integer safely

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")




# 4. Combine file handling with exception handling:
# Ask the user to enter a filename.
# Try to open and read the file.
# If the file doesn’t exist, print a message like:
# "File not found. Please check the filename."


filename = input("Enter the filename: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("\nFile contents:\n")
        print(content)

except FileNotFoundError:
    print("File not found. Please check the filename.")




# 5. Create a program that writes a list of numbers into a file. Then read back the
# file and calculate the sum of numbers.
# Add exception handling for ValueError (in case non-numeric data is inside
# the file).

 
#  try:
#     with open('data.txt','r')as f:
#         f_contents =f.read()
#         print(f"file content:{f_contents}")
#         except