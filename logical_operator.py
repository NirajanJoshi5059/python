#Logical Operator :- and, or, not

has_high_income=True
has_good_credit=True

if has_high_income and has_good_credit:
    print("You are eligiable for loan process.")
else:
    print("You are not eligiable for loan process.")

"""
Example 2:
has bank balance, no criminal record and good marks 
visa accepted.


number=bin(int(input("Enter any number to convert in binary.")))
print(number)
"""
has_bank_balance=True
has_criminal_record=True
has_good_marks=True

if has_bank_balance and has_good_marks:
    if not has_criminal_record:
        print('Visa accepted.')
    else:
        print("You have criminal record in past.")
elif has_bank_balance and not has_good_marks:
    print("Your academic background is insufficient.")
elif not has_bank_balance and has_good_marks:
    print("You have insufficient balance.")