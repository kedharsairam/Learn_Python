high_income = True
good_credit = True
criminal_record = False
if high_income and good_credit:
    print("1_Eligible for loan.")
    
if high_income or good_credit:
    print("2_Eligible for loan.")
    
if good_credit and not criminal_record:
    print("3_Eligible for loan.")