print("Welcome to the tip calculator")

user_bill_amount = float(input("What was the total bill amount.?"))
user_tip_amount = float(input("how much tip would you like to give.10 or 12 or 15?"))
amount_split = int(input("How many people to split the bill.?"))

total_amount =  (user_bill_amount /100) * user_tip_amount
final_amount = (total_amount + user_bill_amount) /amount_split
print(total_amount)
print(f"Each person should pay..={round(final_amount)}")
print("Each person should pay..=" + str(round(final_amount,4)))