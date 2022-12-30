unit=int(input())
if unit<=199:
    bill_amt=unit*1.20
elif unit>=200 and unit<400:
    bill_amt=unit*1.50
elif unit>=400 and unit<600:
    bill_amt=unit*1.80
elif unit>=600:
    bill_amt=unit*2
if bill_amt>400:
    bill_amt=bill_amt+bill_amt*.15
else:
    bill_amt+=100
print("{:.2f}".format(bill_amt))