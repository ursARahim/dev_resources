high_income = True
good_credit = False

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")


high_income = True
good_credit = False

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")
    
    
high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")