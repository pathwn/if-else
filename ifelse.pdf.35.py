c_p=int(input("enter num"))
if c_p>100000:
    Tax=c_p*15/100
    print(Tax)
elif c_p>50000 and c_p<=100000:
    Tax=c_p*10/100
    print(Tax)
elif c_p<=50000:
    Tax=c_p*5/100
    print(Tax) 
else:
    print("not Tax")           