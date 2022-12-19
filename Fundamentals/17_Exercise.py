price = 1000000
is_credit = True
if is_credit:
    payment = price * 0.1
else:
    payment = price * 0.2
print(f"payment: {payment}")