print("Welcome to the tip calculator!")
# Asking user to input the final bill amount
bill = float(input("What was the final bill? £"))
# Asking user what percentage they would like to tip
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
# Asking user how many people are splitting the bill
people = int(input("How many people are splitting the bill?"))
# Converting the tip into a percentage
tip_as_percent = tip / 100
# Calculating the tip amount by multiplying the bill with the tip amount
total_tip_amount = bill * tip_as_percent
# Calculating the total of the bill by adding the tip amount to the bill
total_bill = bill + total_tip_amount
# Calculating how many people will pay for the bill by dividing the bill by the amount of people.
bill_per_person = total_bill / people
# Calculating the the final amount each person should pay and formatting that sum to two demical places
final_amount = "{:.2f}" .format(bill_per_person)
#Printing the total each person pays
print(f"Each person should pay: £{final_amount} ")
