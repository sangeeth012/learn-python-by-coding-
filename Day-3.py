#conditional statement ,logical operator,code blocks and scope
# if condition:
    #Do this
# else:
    #Do this

#Nested if /else
# if condition :
    #if another condition:
       #do this
    #else
      #do this
# else:
  #Do this


#Draw io => make floe chart
print("Welcome to the rollercoaster ")
height = int (input("What is your height in cm ?:"))
age_of_user = int(input("Please enter your age..."))

if height >= 120:
    print("you can ride the rollercoaster")
    if age_of_user >= 18:
        print("your ticket amount= $12")
    elif age_of_user <= 12:
        print("your ticket amount= $1")
    else:
        print("your ticket amount= $5")
else:
    print("sorry you have to grow taller before you can ride.")




#compersion operator
#operator      meaning
#1) >           Greater then
#2) <           less then
#3) >=          Greater then or equal to
#4) <=          Less then or equal to
#5) ==          equal
#6) !=          not equal

## Modulo operator %
numbers_to_check = int(input("What is the number do you want to check.."))
if (numbers_to_check%2) == 0:
    print("even number")
else:
    print("odd number")
