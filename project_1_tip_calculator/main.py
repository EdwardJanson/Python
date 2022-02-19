print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people_number = input ("How many people to split the bill? ")

total_bill_float = float(total_bill)
tip_int = int(tip)
people_number_int = int(people_number)
tip_percentage = tip_int / 100
bill_with_tip = total_bill_float + (total_bill_float * tip_percentage)
bill_per_person = bill_with_tip / people_number_int
bill_per_person_rounded = round(bill_per_person, 2)

result = f"Each person should pay: ${bill_per_person_rounded}"
print(result)
