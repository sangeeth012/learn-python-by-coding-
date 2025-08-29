#Day-1 python class topic to covered
#1) printing 2)commenting, 3)Debugging 4)String manipulation and variable 5)input
#Errors
#name error
#syntax errors
# 1) printing
print("hello_python")

#2)commenting
#commenting multiple line use (ctrl + /)
#string concatenate
print("hello" + "python") # no space
print("hello " + "python") # we are giving one space at the end of the hello word
print("hello" + " python") # we are giving one space at stating of th python word
print(("hello " + " python"))# we are giving two space one at the end of hello another at the starting of python
print("string" + " " + "concatenate")

#5)Getting input from user
# input() print function // input("A prompt for the user") type of data u need
print("hello " + input("what is your name.?"))
print("hello " + input("what is your name.?") + "!")

#variable
name = ("hello " + input("what is your name.?"))
length = len(name)
print(f"Number of word in given name..:{length}")
print(name)

