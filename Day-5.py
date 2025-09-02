#For loop ,range and code blocks

fruits = ["apple","peach","pear","banana"]

for fruit in fruits:
    print(fruit)
fruits[0] = "HELLO"
print(fruits)
print("*****************************************************************")
print("Write a program to print numbers from 1 to a given number n.")
number = int(input("Enter the number "))
for i in range (0,number):
    print(i)
print("*****************************************************************")
print("Calculate the sum of the first n natural numbers using a for loop")
#number = int(input("Enter the number "))
sum_1 = 0
for i in range(0,number):
    sum_1 += i
print(sum_1)
print("*****************************************************************")

print('''*
**
***
****
*****''')

for i in range(0, 5):        # Outer loop for rows
    for j in range(0, i + 1):  # Inner loop for columns
        print("*", end=" ")   # Print stars in the same line
    print()  # Move to the next line


