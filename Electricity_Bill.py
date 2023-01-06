units=int(input())
surcharge=0
surcharge=0
if units<=199:
    cpu=1.20
elif units>=200 and units <400:
    cpu=1.40
elif units>=400 and units <600:
    cpu=1.60
elif units>=600 and units <800:
    cpu=1.80
else:
    cpu=2.00
bill=units*cpu
if bill>400:
    surcharge=bill*.15
total=bill+surcharge
    
print("Units Consumed: {}".format(units))
print("Cost per Unit: {:.2f}".format(cpu))
print("Bill: {:.2f}".format(bill))
print("Surcharge: {:.2f}".format(surcharge))
print("Total Amount: {:.2f}".format(total))