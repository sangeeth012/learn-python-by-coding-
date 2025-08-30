#Day-2
#Date Types, Numbers, Operation, Type conversion ,f strings
#subscripting
print("hello"[-1])
print("***********************************************")
#string
print("123" + "456") #so it basically just concatenated these two
# string together just as we have done with other strings
print("***********************************************")
#1 Data types
#Integer = whole nuber
print(123 +456)
#Large Integers
print(123_456_789)  #In python, we can replace those commas simply with underscore and it
#will be interpreted by the computer ** so the computer actually those underscore and ignores it
print("***********************************************")
#float = Floating point number
print(324.223)
print("***********************************************")
#Boolean
print(True)
print(False)
print("***********************************************")
#one function python that allows us to check the data type of any piece of data
# keyword type(" any_type_of data")
print("Checking data different data type using type function ")
print(type(12345))
print(type("python_automation"))
print(type(234.23))
print(type(True))
print("***********************************************")

#converting data type in python
#what we want to convert a piece of data into a different data type??
# we need to learn type casting
print("***********************************************")
#converting string data type into integer data type
print(int("123456789"))
print(int("123") + int("456"))
print("***********************************************")
#Now one of the dangerous things about this is of course sometimes you can't convert the
#things into a different data type
#print(int("abc") + int("234"))
print("***********************************************")
#coverting float data type into integer data type
print(int(1234.234))

#converting integer data type into float data type
print(float(2342345))

#Practice by different type
#Getting the name fromm the user
name_of_the_user =input("Enter your name:")
#calculatig number of words in the name_of_the_user by using len function
number_of_character = len("Enter your name:")
#Checking the type of the data type
print(type(name_of_the_user))
print(type(number_of_character))

#By using the f<string>
print(f"Number of letters in your name: {number_of_character} ")
#normal
print("Number of letters in your name:" + str(number_of_character))
print("***********************************************")
#Mathematical operation
print(7-3)
print(3*2)
print("***********************************************")
#complete divide its shows float data type // it somthing called implicit typecasting,
#because python is implicity converting the result here into a floating point number
print("***********************************************")
print(6/3)
print(type(6/3))
#So there is another python division operator that might be worth knowing about
#and it simply done with two slashes (//)
print(6//3)
print(type(6//3))
print("***********************************************")
print(2**3)
print("***********************************************")
#And the rule that you might know something called PEMDAS
print("#parentheses,Exponents,Multiplication,division,addition.subtraction")

#basic bmi calculator

height_of_the_user = float(input("Enter the height of the user.."))
weight_of_the_user = float(input("Enter the height of the user.."))

bmi = weight_of_the_user / (height_of_the_user ** 2)
print(bmi)

print(round(bmi,2))
print(round(bmi,5))
print(int(bmi))
print(float(bmi))