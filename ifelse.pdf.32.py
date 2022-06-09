unit=int(input("enter unit"))
if unit<=100:
    print("no charge")
elif unit>100 and unit<=200:
    bill=unit*5
    print(bill) 
elif unit>100:
    a=unit-200
    b=a*10
    c=unit-a-100
    d=c*5
    bill=b+d
    print(bill) 
else:
    print("none")          