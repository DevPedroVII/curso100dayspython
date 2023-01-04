print("welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12 or 15?"))
people = int(input("how many people split the bill?"))
#bill_with_tip = bill *(1 + tip/100)

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = total_tip_amount + bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)

print(f"each person should pay :{final_amount}")
