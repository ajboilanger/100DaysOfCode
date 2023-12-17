"""
    MY CODE ---
        print("Welcome to the tip calculator.")
        bill_total = input("What was the total bill?\n")
        tip_percent = input("What percentage tip would you like to give? 10, 12, or 15?\n")
        people = input("How many people to split the bill?\n")

        ###tip_total = (int(tip_percent) / 100) * (bill_total)
        ###final_bill = (int(bill_total) + int(tip_total))
        ###split_bill = (int(final_bill) / int(people))
        ###print(tip_total)
        ###print(final_bill)

        tip_total = (int(bill_total) * ((int(tip_percent) / 100) + 1))
        round(tip_total, 2)


        print(tip_total)
        print(type(tip_total))

        ###print(f"Everyone should pay ${split_bill}.")
""" 
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people will be splitting the bill? "))
""" 
    Can also be broken down as the following:
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
"""
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount}.")