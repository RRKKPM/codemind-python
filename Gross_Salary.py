basic=int(input())
if (basic<=10000):
    da=basic*0.8
    hra=basic*0.2
elif (basic<=20000):
    da=basic*0.9
    hra=basic*0.25
else:
    da=basic*0.95
    hra=basic*0.30
gross=basic+hra+da
print("{:.2f}".format(gross))