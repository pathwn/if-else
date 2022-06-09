unit_charge=int(input("enter unit_charge"))
if unit_charge>=1 and unit_charge<=50:
    total_bill=unit_charge*0.50+20/100
    print(total_bill)
elif unit_charge>=51 and unit_charge<151:
    total_bill=unit_charge*0.75+20/100
    print(total_bill)
elif unit_charge>=152 and unit_charge<=252:
    total_bill=unit_charge*120+20/100
    print(total_bill) 
elif unit_charge>250:
    total_bill=unit_charge*1.50+20/100
    print(total_bill) 
else:
    print("not available")          