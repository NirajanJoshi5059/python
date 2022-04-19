
try:
    age=int(input("Age : "))
    income=50000
    income_ratio=income/age
except ValueError as e:
    print('Value error ->', e)
except ZeroDivisionError as z:
    print("Zero division error -> ",z)